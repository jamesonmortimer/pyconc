#!/usr/bin/env python3
"""
Starvation Example - Resource Starvation
Demonstrates resource starvation where high-priority workers can starve low-priority ones.
"""

import threading
import time
import queue


class StarvationExample:
    """Demonstrates resource starvation."""

    def __init__(self):
        self.resource = threading.Lock()
        self.high_priority_queue = queue.Queue()
        self.low_priority_queue = queue.Queue()
        self.running = True

    def high_priority_worker(self, worker_id: int):
        """High priority worker that can starve others."""
        while self.running:
            try:
                # High priority workers get immediate access
                if self.resource.acquire(timeout=0.01):
                    print(f"High Priority Worker {worker_id}: Got resource!")
                    time.sleep(0.1)  # Hold resource longer
                    self.resource.release()
                    print(f"High Priority Worker {worker_id}: Released resource")
                time.sleep(0.05)  # Very short wait
            except Exception:
                pass

    def low_priority_worker(self, worker_id: int):
        """Low priority worker that may get starved."""
        while self.running:
            try:
                # Low priority workers wait longer
                if self.resource.acquire(timeout=0.1):
                    print(f"Low Priority Worker {worker_id}: Got resource!")
                    time.sleep(0.05)  # Hold resource briefly
                    self.resource.release()
                    print(f"Low Priority Worker {worker_id}: Released resource")
                time.sleep(0.2)  # Longer wait
            except Exception:
                pass

    def run(self, duration: int = 8):
        """Run the starvation example."""
        print(f"\n=== STARVATION EXAMPLE (Resource Starvation) ===")
        print(f"Running for {duration} seconds...")
        print("High priority workers may starve low priority ones!\n")

        # Start workers
        high_workers = []
        low_workers = []

        # Start more high priority workers
        for i in range(3):
            thread = threading.Thread(target=self.high_priority_worker, args=(i,))
            thread.daemon = True
            thread.start()
            high_workers.append(thread)

        # Start fewer low priority workers
        for i in range(2):
            thread = threading.Thread(target=self.low_priority_worker, args=(i,))
            thread.daemon = True
            thread.start()
            low_workers.append(thread)

        # Let them run
        time.sleep(duration)
        self.running = False

        print("\nStopping workers...")
        for thread in high_workers + low_workers:
            thread.join(timeout=1.0)
        print("Starvation example completed.\n")


if __name__ == "__main__":
    # Allow running this file directly for testing
    example = StarvationExample()
    example.run(8)
