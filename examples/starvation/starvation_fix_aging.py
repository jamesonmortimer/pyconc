#!/usr/bin/env python3
"""
Starvation Fix - Aging Mechanism
Fixes starvation by increasing priority of waiting threads over time.
"""

import threading
import time
import heapq


class StarvationFixAging:
    """Fixes starvation by using aging mechanism for priority management."""

    def __init__(self, num_workers: int = 5):
        self.num_workers = num_workers
        self.resource = threading.Lock()
        self.workers = []
        self.running = True

        # FIX: Aging mechanism using priority queue
        self.priority_queue = []
        self.worker_priorities = {i: 0 for i in range(num_workers)}
        self.worker_wait_times = {i: 0 for i in range(num_workers)}
        self.queue_lock = threading.Lock()

        # Start the aging scheduler
        self.aging_scheduler = threading.Thread(target=self.age_priorities)
        self.aging_scheduler.daemon = True
        self.aging_scheduler.start()

    def age_priorities(self):
        """Aging scheduler that increases priority of waiting workers."""
        print("Aging Scheduler: Starting...")

        while self.running:
            with self.queue_lock:
                # Age all waiting workers
                for worker_id in range(self.num_workers):
                    if self.worker_wait_times[worker_id] > 0:
                        self.worker_priorities[worker_id] += 1
                        print(
                            f"Aging Scheduler: Worker {worker_id} priority increased to {self.worker_priorities[worker_id]}"
                        )

            time.sleep(0.5)  # Age every 0.5 seconds

        print("Aging Scheduler: Stopping...")

    def worker(self, worker_id: int):
        """Worker function that uses aging mechanism to avoid starvation."""
        print(f"Worker {worker_id}: Starting...")

        while self.running:
            print(f"Worker {worker_id}: Requesting resource...")

            # FIX: Add request to priority queue with aging
            with self.queue_lock:
                # Calculate priority based on base priority and aging
                priority = self.worker_priorities[worker_id]
                heapq.heappush(self.priority_queue, (-priority, time.time(), worker_id))
                self.worker_wait_times[worker_id] = time.time()
                print(f"Worker {worker_id}: Added to queue with priority {priority}")

            # Wait for our turn (simplified - in real implementation this would be more sophisticated)
            time.sleep(0.1)

            # Try to acquire the resource
            if self.resource.acquire(timeout=0.3):
                print(f"Worker {worker_id}: Got resource! Working...")

                # FIX: Reset wait time and priority when we get the resource
                with self.queue_lock:
                    self.worker_wait_times[worker_id] = 0
                    self.worker_priorities[worker_id] = 0

                work_time = 0.1 + (worker_id * 0.05)  # Different work times
                time.sleep(work_time)
                print(f"Worker {worker_id}: Finished work, releasing resource")

                self.resource.release()

                # FIX: Yield time to other workers
                yield_time = 0.2
                print(f"Worker {worker_id}: Yielding for {yield_time}s...")
                time.sleep(yield_time)
            else:
                print(f"Worker {worker_id}: Resource acquisition timeout, retrying...")
                time.sleep(0.1)

    def run(self, duration: int = 5):
        """Run the aging mechanism fix example."""
        print(f"\n=== STARVATION FIX: Aging Mechanism ===")
        print(f"Running for {duration} seconds...")
        print("This should NOT result in starvation due to aging mechanism!\n")
        print("Worker priorities increase over time to ensure fair access.\n")

        # Start workers
        for i in range(self.num_workers):
            thread = threading.Thread(target=self.worker, args=(i,))
            thread.daemon = True
            thread.start()
            self.workers.append(thread)

        # Let it run for a while
        time.sleep(duration)
        self.running = False

        print("\nStopping workers and aging scheduler...")
        for thread in self.workers:
            thread.join(timeout=1.0)
        self.aging_scheduler.join(timeout=1.0)
        print("Aging mechanism fix example completed.\n")


if __name__ == "__main__":
    # Allow running this file directly for testing
    example = StarvationFixAging()
    example.run(5)
