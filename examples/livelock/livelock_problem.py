#!/usr/bin/env python3
"""
Livelock Example - Too Polite Workers
Demonstrates livelock where threads are too polite and may not make progress.
"""

import threading
import time


class LivelockExample:
    """Demonstrates livelock where threads are too polite."""

    def __init__(self):
        self.lock1 = threading.Lock()
        self.lock2 = threading.Lock()
        self.running = True

    def worker1(self):
        """Worker 1 that tries to be polite."""
        while self.running:
            print("Worker 1: Trying to acquire lock1...")
            if self.lock1.acquire(timeout=0.1):
                print("Worker 1: Got lock1, trying lock2...")
                time.sleep(0.1)  # Simulate work

                if self.lock2.acquire(timeout=0.1):
                    print("Worker 1: Got both locks! Working...")
                    time.sleep(0.2)
                    self.lock2.release()
                    self.lock1.release()
                    print("Worker 1: Released both locks")
                    break
                else:
                    print(
                        "Worker 1: Couldn't get lock2, releasing lock1 and retrying..."
                    )
                    self.lock1.release()
                    time.sleep(0.1)  # Be polite, wait a bit
            time.sleep(0.05)

    def worker2(self):
        """Worker 2 that tries to be polite."""
        while self.running:
            print("Worker 2: Trying to acquire lock2...")
            if self.lock2.acquire(timeout=0.1):
                print("Worker 2: Got lock2, trying lock1...")
                time.sleep(0.1)  # Simulate work

                if self.lock1.acquire(timeout=0.1):
                    print("Worker 2: Got both locks! Working...")
                    time.sleep(0.2)
                    self.lock1.release()
                    self.lock2.release()
                    print("Worker 2: Released both locks")
                    break
                else:
                    print(
                        "Worker 2: Couldn't get lock1, releasing lock2 and retrying..."
                    )
                    self.lock2.release()
                    time.sleep(0.1)  # Be polite, wait a bit
            time.sleep(0.05)

    def run(self, duration: int = 10):
        """Run the livelock example."""
        print(f"\n=== LIVELOCK EXAMPLE (Too Polite Workers) ===")
        print(f"Running for {duration} seconds...")
        print("Workers will keep being polite and may not make progress!\n")

        # Start workers
        thread1 = threading.Thread(target=self.worker1)
        thread2 = threading.Thread(target=self.worker2)

        thread1.daemon = True
        thread2.daemon = True

        thread1.start()
        thread2.start()

        # Let them run
        time.sleep(duration)
        self.running = False

        print("\nStopping workers...")
        thread1.join(timeout=1.0)
        thread2.join(timeout=1.0)
        print("Livelock example completed.\n")


if __name__ == "__main__":
    # Allow running this file directly for testing
    example = LivelockExample()
    example.run(10)
