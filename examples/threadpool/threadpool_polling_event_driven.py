#!/usr/bin/env python3
"""
ThreadPool Example - Event-Driven Polling
Demonstrates using ThreadPoolExecutor for event-driven polling with producer-consumer pattern.
"""

import threading
import time
import random
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
import queue


class ThreadPoolPollingEventDriven:
    """Demonstrates event-driven polling using ThreadPoolExecutor."""

    def __init__(self, num_workers: int = 3):
        self.num_workers = num_workers
        self.executor = ThreadPoolExecutor(max_workers=num_workers)
        self.running = True
        self.tasks = []

        # Event queues for different types of events
        self.high_priority_queue = queue.Queue()
        self.normal_priority_queue = queue.Queue()
        self.low_priority_queue = queue.Queue()

        # Event counters
        self.event_counters = {"high": 0, "normal": 0, "low": 0}

        # Producer thread
        self.producer_thread = None

    def event_producer(self):
        """Produces events at different priorities."""
        print("Event Producer: Starting...")

        while self.running:
            # Generate random events
            event_type = random.choices(
                ["high", "normal", "low"],
                weights=[0.2, 0.5, 0.3],  # Normal events are most common
            )[0]

            event_data = {
                "id": self.event_counters[event_type],
                "type": event_type,
                "timestamp": datetime.now().strftime("%H:%M:%S.%f")[:-3],
                "data": f"Event data {self.event_counters[event_type]}",
            }

            # Add to appropriate queue
            if event_type == "high":
                self.high_priority_queue.put(event_data)
            elif event_type == "normal":
                self.normal_priority_queue.put(event_data)
            else:
                self.low_priority_queue.put(event_data)

            self.event_counters[event_type] += 1

            print(f"Event Producer: Created {event_type} priority event {event_data['id']}")

            # Random delay between events
            time.sleep(random.uniform(0.1, 0.5))

        print("Event Producer: Stopping...")

    def event_consumer(self, worker_id: int):
        """Consumes events from priority queues."""
        print(f"Event Consumer {worker_id}: Starting...")

        while self.running:
            event = None

            # Check queues in priority order (high -> normal -> low)
            try:
                # Try high priority first (non-blocking)
                event = self.high_priority_queue.get_nowait()
                print(f"Event Consumer {worker_id}: Processing HIGH priority event {event['id']}")
            except queue.Empty:
                try:
                    # Try normal priority (non-blocking)
                    event = self.normal_priority_queue.get_nowait()
                    print(f"Event Consumer {worker_id}: Processing NORMAL priority event {event['id']}")
                except queue.Empty:
                    try:
                        # Try low priority (non-blocking)
                        event = self.low_priority_queue.get_nowait()
                        print(f"Event Consumer {worker_id}: Processing LOW priority event {event['id']}")
                    except queue.Empty:
                        # No events available, wait a bit
                        time.sleep(0.1)
                        continue

            if event:
                # Process the event
                self.process_event(worker_id, event)

                # Mark task as done
                if event["type"] == "high":
                    self.high_priority_queue.task_done()
                elif event["type"] == "normal":
                    self.normal_priority_queue.task_done()
                else:
                    self.low_priority_queue.task_done()

        print(f"Event Consumer {worker_id}: Stopping...")

    def process_event(self, worker_id: int, event: dict):
        """Process an individual event."""
        start_time = time.time()

        # Simulate processing time based on priority
        if event["type"] == "high":
            process_time = 0.05  # High priority = fast processing
        elif event["type"] == "normal":
            process_time = 0.1  # Normal priority = standard processing
        else:
            process_time = 0.2  # Low priority = slower processing

        time.sleep(process_time)

        actual_time = time.time() - start_time
        print(f"Event Consumer {worker_id}: Completed {event['type']} priority event {event['id']} " f"in {actual_time:.3f}s")

    def run(self, duration: int = 5):
        """Run the event-driven polling example."""
        print("\n=== THREADPOOL: Event-Driven Polling ===")
        print(f"Running for {duration} seconds...")
        print(f"Using {self.num_workers} workers for event processing\n")
        print("Events are generated with different priorities and processed accordingly.\n")

        # Start event producer
        self.producer_thread = threading.Thread(target=self.event_producer)
        self.producer_thread.daemon = True
        self.producer_thread.start()

        # Submit event consumer tasks
        for i in range(self.num_workers):
            future = self.executor.submit(self.event_consumer, i)
            self.tasks.append(future)

        # Let it run for the specified duration
        time.sleep(duration)
        self.running = False

        print("\nStopping event-driven polling...")

        # Wait for producer to finish
        if self.producer_thread:
            self.producer_thread.join(timeout=1.0)

        # Wait for all consumer tasks to complete
        for future in as_completed(self.tasks, timeout=2.0):
            try:
                future.result()
            except Exception as e:
                print(f"Task completed with exception: {e}")

        self.executor.shutdown(wait=True)

        # Print final statistics
        print("\nFinal Event Counts:")
        print(f"  High Priority: {self.event_counters['high']}")
        print(f"  Normal Priority: {self.event_counters['normal']}")
        print(f"  Low Priority: {self.event_counters['low']}")
        print(f"  Total: {sum(self.event_counters.values())}")

        print("Event-driven polling example completed.\n")


if __name__ == "__main__":
    # Allow running this file directly for testing
    example = ThreadPoolPollingEventDriven()
    example.run(5)
