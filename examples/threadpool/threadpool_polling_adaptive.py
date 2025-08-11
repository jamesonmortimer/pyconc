#!/usr/bin/env python3
"""
ThreadPool Example - Adaptive Polling
Demonstrates using ThreadPoolExecutor for adaptive polling based on system conditions.
"""

import threading
import time
import random
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime


class ThreadPoolPollingAdaptive:
    """Demonstrates adaptive polling using ThreadPoolExecutor."""

    def __init__(self, num_workers: int = 3):
        self.num_workers = num_workers
        self.executor = ThreadPoolExecutor(max_workers=num_workers)
        self.running = True
        self.tasks = []

        # Adaptive polling parameters
        self.base_interval = 1.0
        self.min_interval = 0.2
        self.max_interval = 3.0
        self.adaptation_factor = 0.1

        # Shared state for adaptation
        self.response_times = {}
        self.system_load = 0.0
        self.load_lock = threading.Lock()

    def update_system_load(self):
        """Simulate system load changes."""
        while self.running:
            with self.load_lock:
                # Simulate varying system load (0.0 = idle, 1.0 = overloaded)
                self.system_load = 0.5 + 0.5 * random.random()
                print(f"System Load: {self.system_load:.2f}")
            time.sleep(2.0)

    def adaptive_task(self, task_id: int):
        """Task that adapts its polling interval based on system conditions."""
        print(f"Adaptive Task {task_id}: Starting")

        current_interval = self.base_interval

        while self.running:
            start_time = time.time()

            # Simulate work that varies with system load
            with self.load_lock:
                load = self.system_load

            # Work time increases with system load
            work_time = 0.1 + (load * 0.3)
            time.sleep(work_time)

            # Calculate response time
            response_time = time.time() - start_time

            # Store response time for this task
            self.response_times[task_id] = response_time

            current_time = datetime.now().strftime("%H:%M:%S.%f")[:-3]
            print(
                f"Adaptive Task {task_id}: Executed at {current_time} "
                f"(load: {load:.2f}, work: {work_time:.3f}s, interval: {current_interval:.2f}s)"
            )

            # Adapt interval based on system load and response time
            if load > 0.7:  # High load - poll less frequently
                current_interval = min(current_interval * (1 + self.adaptation_factor), self.max_interval)
                print(f"Adaptive Task {task_id}: High load detected, increasing interval to {current_interval:.2f}s")
            elif load < 0.3:  # Low load - poll more frequently
                current_interval = max(current_interval * (1 - self.adaptation_factor), self.min_interval)
                print(f"Adaptive Task {task_id}: Low load detected, decreasing interval to {current_interval:.2f}s")

            # Also adapt based on response time
            if response_time > current_interval * 0.8:  # Work taking too long
                current_interval = min(current_interval * 1.2, self.max_interval)
                print(f"Adaptive Task {task_id}: Slow response, increasing interval to {current_interval:.2f}s")

            time.sleep(current_interval)

        print(f"Adaptive Task {task_id}: Stopping")

    def run(self, duration: int = 5):
        """Run the adaptive polling example."""
        print("\n=== THREADPOOL: Adaptive Polling ===")
        print(f"Running for {duration} seconds...")
        print(f"Using {self.num_workers} workers for adaptive polling\n")
        print("Polling intervals will adapt based on system load and response times.\n")

        # Start system load monitor
        load_monitor = threading.Thread(target=self.update_system_load)
        load_monitor.daemon = True
        load_monitor.start()

        # Submit adaptive tasks
        for i in range(self.num_workers):
            future = self.executor.submit(self.adaptive_task, i)
            self.tasks.append(future)

        # Let it run for the specified duration
        time.sleep(duration)
        self.running = False

        print("\nStopping adaptive tasks...")

        # Wait for all tasks to complete
        for future in as_completed(self.tasks, timeout=2.0):
            try:
                future.result()
            except Exception as e:
                print(f"Task completed with exception: {e}")

        self.executor.shutdown(wait=True)
        print("Adaptive polling example completed.\n")


if __name__ == "__main__":
    # Allow running this file directly for testing
    example = ThreadPoolPollingAdaptive()
    example.run(5)
