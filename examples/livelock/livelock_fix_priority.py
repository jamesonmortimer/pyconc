#!/usr/bin/env python3
"""
Livelock Fix - Priority-Based Lock Acquisition
Fixes livelock by giving one worker priority to break the polite loop.
"""

import threading
import time


class LivelockFixPriority:
    """Fixes livelock by giving one worker priority to break the polite loop."""

    def __init__(self):
        self.lock1 = threading.Lock()
        self.lock2 = threading.Lock()
        self.workers = []
        self.running = True

    def high_priority_worker(self, worker_id: int):
        """High priority worker that always tries lock1 first."""
        print(f"Worker {worker_id} (HIGH PRIORITY): Starting...")

        while self.running:
            print(f"Worker {worker_id} (HIGH PRIORITY): Trying to acquire lock1...")

            # High priority worker always tries lock1 first
            if self.lock1.acquire(timeout=0.1):
                print(f"Worker {worker_id} (HIGH PRIORITY): Got lock1, trying lock2...")

                if self.lock2.acquire(timeout=0.1):
                    print(
                        f"Worker {worker_id} (HIGH PRIORITY): Got both locks! Working..."
                    )
                    time.sleep(0.2)  # Do some work
                    print(f"Worker {worker_id} (HIGH PRIORITY): Released both locks")
                    self.lock2.release()
                    self.lock1.release()
                else:
                    print(
                        f"Worker {worker_id} (HIGH PRIORITY): Couldn't get lock2, releasing lock1 and retrying..."
                    )
                    self.lock1.release()
                    time.sleep(0.1)
            else:
                print(
                    f"Worker {worker_id} (HIGH PRIORITY): Couldn't get lock1, retrying..."
                )
                time.sleep(0.1)

    def low_priority_worker(self, worker_id: int):
        """Low priority worker that yields to high priority worker."""
        print(f"Worker {worker_id} (LOW PRIORITY): Starting...")

        while self.running:
            print(f"Worker {worker_id} (LOW PRIORITY): Trying to acquire lock2...")

            # Low priority worker tries lock2 first (different order)
            if self.lock2.acquire(timeout=0.1):
                print(f"Worker {worker_id} (LOW PRIORITY): Got lock2, trying lock1...")

                if self.lock1.acquire(timeout=0.1):
                    print(
                        f"Worker {worker_id} (LOW PRIORITY): Got both locks! Working..."
                    )
                    time.sleep(0.2)  # Do some work
                    print(f"Worker {worker_id} (LOW PRIORITY): Released both locks")
                    self.lock1.release()
                    self.lock2.release()
                else:
                    print(
                        f"Worker {worker_id} (LOW PRIORITY): Couldn't get lock1, releasing lock2 and yielding..."
                    )
                    self.lock2.release()

                    # FIX: Low priority worker yields more time to high priority worker
                    yield_time = 0.3
                    print(
                        f"Worker {worker_id} (LOW PRIORITY): Yielding for {yield_time}s..."
                    )
                    time.sleep(yield_time)
            else:
                print(
                    f"Worker {worker_id} (LOW PRIORITY): Couldn't get lock2, yielding..."
                )

                # FIX: Low priority worker yields more time
                yield_time = 0.2
                print(
                    f"Worker {worker_id} (LOW PRIORITY): Yielding for {yield_time}s..."
                )
                time.sleep(yield_time)

    def run(self, duration: int = 5):
        """Run the priority-based fix example."""
        print(f"\n=== LIVELOCK FIX: Priority-Based Lock Acquisition ===")
        print(f"Running for {duration} seconds...")
        print("This should NOT result in livelock due to priority-based acquisition!\n")
        print("High priority worker: Always tries lock1 first")
        print("Low priority worker: Always tries lock2 first and yields more time\n")

        # Start workers with different priorities
        high_priority = threading.Thread(target=self.high_priority_worker, args=(1,))
        low_priority = threading.Thread(target=self.low_priority_worker, args=(2,))

        high_priority.daemon = True
        low_priority.daemon = True

        high_priority.start()
        low_priority.start()

        self.workers = [high_priority, low_priority]

        # Let it run for a while
        time.sleep(duration)
        self.running = False

        print("\nStopping workers...")
        for thread in self.workers:
            thread.join(timeout=1.0)
        print("Priority-based fix example completed.\n")


if __name__ == "__main__":
    # Allow running this file directly for testing
    example = LivelockFixPriority()
    example.run(5)
