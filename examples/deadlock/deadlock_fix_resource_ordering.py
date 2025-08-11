#!/usr/bin/env python3
"""
Deadlock Fix - Resource Ordering
Fixes deadlock by always acquiring resources in a consistent order.
"""

import threading
import time


class DeadlockFixResourceOrdering:
    """Fixes deadlock by always picking up lower-numbered fork first."""

    def __init__(self, num_philosophers: int = 5):
        self.num_philosophers = num_philosophers
        self.forks = [threading.Lock() for _ in range(num_philosophers)]
        self.philosophers = []
        self.running = True

    def philosopher(self, philosopher_id: int):
        """Philosopher function that avoids deadlock through resource ordering."""
        left_fork = philosopher_id
        right_fork = (philosopher_id + 1) % self.num_philosophers

        print(f"Philosopher {philosopher_id} starting...")

        while self.running:
            print(f"Philosopher {philosopher_id} thinking...")
            time.sleep(0.1)

            # FIX: Always pick up lower-numbered fork first
            first_fork = min(left_fork, right_fork)
            second_fork = max(left_fork, right_fork)

            print(f"Philosopher {philosopher_id} picking up fork {first_fork} first (lower-numbered)")
            self.forks[first_fork].acquire()

            print(f"Philosopher {philosopher_id} picking up fork {second_fork} second")
            self.forks[second_fork].acquire()

            print(f"Philosopher {philosopher_id} eating...")
            time.sleep(0.2)

            print(f"Philosopher {philosopher_id} putting down forks")
            self.forks[second_fork].release()
            self.forks[first_fork].release()

            time.sleep(0.1)

    def run(self, duration: int = 5):
        """Run the resource ordering fix example."""
        print("\n=== DEADLOCK FIX: Resource Ordering ===")
        print(f"Running for {duration} seconds...")
        print("This should NOT result in deadlock due to consistent resource ordering!\n")

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
        print("Resource ordering fix example completed.\n")


if __name__ == "__main__":
    # Allow running this file directly for testing
    example = DeadlockFixResourceOrdering()
    example.run(5)
