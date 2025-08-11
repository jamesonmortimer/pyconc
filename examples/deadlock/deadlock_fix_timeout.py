#!/usr/bin/env python3
"""
Deadlock Fix - Timeout Mechanism
Fixes deadlock by using timeouts and retry logic when acquiring resources.
"""

import threading
import time


class DeadlockFixTimeout:
    """Fixes deadlock by using timeouts and retry logic."""

    def __init__(self, num_philosophers: int = 5):
        self.num_philosophers = num_philosophers
        self.forks = [threading.Lock() for _ in range(num_philosophers)]
        self.philosophers = []
        self.running = True

    def philosopher(self, philosopher_id: int):
        """Philosopher function that avoids deadlock through timeout and retry."""
        left_fork = philosopher_id
        right_fork = (philosopher_id + 1) % self.num_philosophers

        print(f"Philosopher {philosopher_id} starting...")

        while self.running:
            print(f"Philosopher {philosopher_id} thinking...")
            time.sleep(0.1)

            # FIX: Use timeout and retry logic
            while self.running:
                # Try to get left fork with timeout
                if not self.forks[left_fork].acquire(timeout=0.1):
                    print(f"Philosopher {philosopher_id}: Left fork {left_fork} not " f"available, retrying...")
                    continue

                print(f"Philosopher {philosopher_id} got left fork {left_fork}")

                # Try to get right fork with timeout
                if not self.forks[right_fork].acquire(timeout=0.1):
                    print(f"Philosopher {philosopher_id}: Right fork {right_fork} not " f"available, releasing left fork and retrying...")
                    self.forks[left_fork].release()
                    time.sleep(0.05)  # Small delay before retry
                    continue

                print(f"Philosopher {philosopher_id} got right fork {right_fork}")
                break  # Successfully got both forks

            if not self.running:
                break

            print(f"Philosopher {philosopher_id} eating...")
            time.sleep(0.2)

            print(f"Philosopher {philosopher_id} putting down forks")
            self.forks[right_fork].release()
            self.forks[left_fork].release()

            time.sleep(0.1)

    def run(self, duration: int = 5):
        """Run the timeout fix example."""
        print("\n=== DEADLOCK FIX: Timeout Mechanism ===")
        print(f"Running for {duration} seconds...")
        print("This should NOT result in deadlock due to timeout and retry logic!\n")

        # Start philosophers
        for i in range(self.num_philosophers):
            thread = threading.Thread(target=self.philosopher, args=(i,))
            thread.daemon = True
            thread.start()
            self.philosophers.append(thread)

        # Let it run for a while
        time.sleep(duration)
        self.running = False

        print("\nStopping philosophers...")
        for thread in self.philosophers:
            thread.join(timeout=1.0)
        print("Timeout fix example completed.\n")


if __name__ == "__main__":
    # Allow running this file directly for testing
    example = DeadlockFixTimeout()
    example.run(5)
