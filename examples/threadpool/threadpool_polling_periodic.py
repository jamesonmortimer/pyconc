#!/usr/bin/env python3
"""
ThreadPool Example - Periodic Polling
Demonstrates using ThreadPoolExecutor for periodic task execution.
"""

import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime


class ThreadPoolPollingPeriodic:
    """Demonstrates periodic polling using ThreadPoolExecutor."""

    def __init__(self, num_workers: int = 3):
        self.num_workers = num_workers
        self.executor = ThreadPoolExecutor(max_workers=num_workers)
        self.running = True
        self.tasks = []

    def periodic_task(self, task_id: int, interval: float):
        """Task that runs periodically at specified intervals."""
        print(f"Periodic Task {task_id}: Starting with {interval}s interval")

        while self.running:
            start_time = time.time()

            # Simulate some work
            work_time = 0.1 + (task_id * 0.05)
            time.sleep(work_time)

            current_time = datetime.now().strftime("%H:%M:%S.%f")[:-3]
            print(
                f"Periodic Task {task_id}: Executed at {current_time} (took {work_time:.3f}s)"
            )

            # Calculate sleep time to maintain interval
            elapsed = time.time() - start_time
            sleep_time = max(0, interval - elapsed)

            if sleep_time > 0:
                time.sleep(sleep_time)

        print(f"Periodic Task {task_id}: Stopping")

    def run(self, duration: int = 5):
        """Run the periodic polling example."""
        print(f"\n=== THREADPOOL: Periodic Polling ===")
        print(f"Running for {duration} seconds...")
        print(f"Using {self.num_workers} workers for periodic tasks\n")

        # Submit periodic tasks with different intervals
        intervals = [0.5, 1.0, 1.5]  # Different polling frequencies

        for i in range(min(self.num_workers, len(intervals))):
            future = self.executor.submit(self.periodic_task, i, intervals[i])
            self.tasks.append(future)

        # Let it run for the specified duration
        time.sleep(duration)
        self.running = False

        print("\nStopping periodic tasks...")

        # Wait for all tasks to complete
        for future in as_completed(self.tasks, timeout=2.0):
            try:
                future.result()
            except Exception as e:
                print(f"Task completed with exception: {e}")

        self.executor.shutdown(wait=True)
        print("Periodic polling example completed.\n")


if __name__ == "__main__":
    # Allow running this file directly for testing
    example = ThreadPoolPollingPeriodic()
    example.run(5)
