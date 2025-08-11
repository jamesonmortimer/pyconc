#!/usr/bin/env python3
"""
ThreadPool Example - ThreadPoolExecutor Usage
Demonstrates various ThreadPoolExecutor operations and patterns.
"""

import threading
import time
import concurrent.futures


class ThreadPoolExample:
    """Demonstrates ThreadPoolExecutor usage."""

    def __init__(self, num_workers: int = 3):
        self.num_workers = num_workers
        self.results = []
        self.lock = threading.Lock()

    def worker_function(self, task_id: int, duration: float) -> str:
        """Worker function that simulates work."""
        print(f"Task {task_id}: Starting work for {duration:.1f}s...")
        time.sleep(duration)
        result = f"Task {task_id} completed in {duration:.1f}s"
        print(f"Task {task_id}: Finished!")

        with self.lock:
            self.results.append(result)

        return result

    def run(self, duration: int = 5):
        """Run the threadpool example."""
        print("\n=== THREADPOOL EXAMPLE (ThreadPoolExecutor) ===")
        print(f"Running for {duration} seconds...")
        print("Demonstrating various threadpool operations!\n")

        # Create a thread pool
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            print("Created ThreadPoolExecutor with 4 workers")

            # Submit individual tasks
            print("\n--- Submitting individual tasks ---")
            future1 = executor.submit(self.worker_function, 1, 0.5)
            future2 = executor.submit(self.worker_function, 2, 1.0)
            future3 = executor.submit(self.worker_function, 3, 0.3)

            # Wait for specific futures
            print(f"Future 1 result: {future1.result()}")
            print(f"Future 2 result: {future2.result()}")
            print(f"Future 3 result: {future3.result()}")

            # Submit multiple tasks with map
            print("\n--- Using map for multiple tasks ---")
            task_ids = [4, 5, 6, 7, 8]
            durations = [0.2, 0.4, 0.6, 0.8, 1.0]

            results = list(executor.map(self.worker_function, task_ids, durations))
            print(f"Map results: {results}")

            # Submit tasks with as_completed
            print("\n--- Using as_completed ---")
            futures = []
            for i in range(9, 13):
                future = executor.submit(self.worker_function, i, 0.1 + (i % 3) * 0.2)
                futures.append(future)

            for future in concurrent.futures.as_completed(futures):
                try:
                    result = future.result()
                    print(f"As completed: {result}")
                except Exception as e:
                    print(f"Task failed: {e}")

        print(f"\nAll tasks completed. Total results: {len(self.results)}")
        print("ThreadPool example completed.\n")


if __name__ == "__main__":
    # Allow running this file directly for testing
    example = ThreadPoolExample()
    example.run(5)
