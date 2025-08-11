#!/usr/bin/env python3
"""
Deadlock Example - Dining Philosophers Problem
Demonstrates classic deadlock scenario where philosophers can get stuck.
"""

import threading
import time


class DeadlockExample:
    """Demonstrates deadlock using the dining philosophers problem."""

    def __init__(self, num_philosophers: int = 5):
        self.num_philosophers = num_philosophers
        self.forks = [threading.Lock() for _ in range(num_philosophers)]
        self.philosophers = []
        self.running = True

    def philosopher(self, philosopher_id: int):
        """Philosopher function that can lead to deadlock."""
        left_fork = philosopher_id
        right_fork = (philosopher_id + 1) % self.num_philosophers

        print(f"Philosopher {philosopher_id} starting...")

        while self.running:
            print(f"Philosopher {philosopher_id} thinking...")
            time.sleep(0.1)

            # This can lead to deadlock - all philosophers pick up left fork first
            print(f"Philosopher {philosopher_id} picking up left fork {left_fork}")
            self.forks[left_fork].acquire()

            print(f"Philosopher {philosopher_id} picking up right fork {right_fork}")
            self.forks[right_fork].acquire()

            print(f"Philosopher {philosopher_id} eating...")
            time.sleep(0.2)

            print(f"Philosopher {philosopher_id} putting down forks")
            self.forks[right_fork].release()
            self.forks[left_fork].release()

            time.sleep(0.1)

    def run(self, duration: int = 5):
        """Run the deadlock example for specified duration."""
        print("\n=== DEADLOCK EXAMPLE (Dining Philosophers) ===")
        print(f"Running for {duration} seconds...")
        print("This will likely result in deadlock!\n")

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
        print("Deadlock example completed.\n")


if __name__ == "__main__":
    # Allow running this file directly for testing
    example = DeadlockExample()
    example.run(5)
