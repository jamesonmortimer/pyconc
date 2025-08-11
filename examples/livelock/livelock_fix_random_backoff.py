#!/usr/bin/env python3
"""
Livelock Fix - Random Backoff
Fixes livelock by adding randomness to break the polite loop.
"""

import threading
import time
import random


class LivelockFixRandomBackoff:
    """Fixes livelock by adding random backoff to break the polite loop."""

    def __init__(self):
        self.lock1 = threading.Lock()
        self.lock2 = threading.Lock()
        self.workers = []
        self.running = True

    def worker(self, worker_id: int):
        """Worker function that avoids livelock through random backoff."""
        print(f"Worker {worker_id}: Starting...")

        while self.running:
            print(f"Worker {worker_id}: Trying to acquire lock1...")

            # Try to get first lock
            if self.lock1.acquire(timeout=0.1):
                print(f"Worker {worker_id}: Got lock1, trying lock2...")

                # Try to get second lock
                if self.lock2.acquire(timeout=0.1):
                    print(f"Worker {worker_id}: Got both locks! Working...")
                    time.sleep(0.2)  # Do some work
                    print(f"Worker {worker_id}: Released both locks")
                    self.lock2.release()
                    self.lock1.release()
                else:
                    print(
                        f"Worker {worker_id}: Couldn't get lock2, releasing lock1 and retrying..."
                    )
                    self.lock1.release()

                    # FIX: Add random backoff to break the polite loop
                    backoff_time = random.uniform(0.1, 0.5)
                    print(f"Worker {worker_id}: Backing off for {backoff_time:.2f}s...")
                    time.sleep(backoff_time)
            else:
                print(f"Worker {worker_id}: Couldn't get lock1, retrying...")

                # FIX: Add random backoff here too
                backoff_time = random.uniform(0.05, 0.3)
                print(f"Worker {worker_id}: Backing off for {backoff_time:.2f}s...")
                time.sleep(backoff_time)

    def run(self, duration: int = 5):
        """Run the random backoff fix example."""
        print(f"\n=== LIVELOCK FIX: Random Backoff ===")
        print(f"Running for {duration} seconds...")
        print("This should NOT result in livelock due to random backoff!\n")

        # Start workers
        for i in range(1, 3):
            thread = threading.Thread(target=self.worker, args=(i,))
            thread.daemon = True
            thread.start()
            self.workers.append(thread)

        # Let it run for a while
        time.sleep(duration)
        self.running = False

        print("\nStopping workers...")
        for thread in self.workers:
            thread.join(timeout=1.0)
        print("Random backoff fix example completed.\n")


if __name__ == "__main__":
    # Allow running this file directly for testing
    example = LivelockFixRandomBackoff()
    example.run(5)
