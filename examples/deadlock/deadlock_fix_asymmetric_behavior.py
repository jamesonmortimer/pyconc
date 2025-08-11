#!/usr/bin/env python3
"""
Deadlock Fix - Asymmetric Behavior
Fixes deadlock by making some philosophers pick up right fork first.
"""

import threading
import time


class DeadlockFixAsymmetricBehavior:
    """Fixes deadlock by using asymmetric behavior for different philosophers."""

    def __init__(self, num_philosophers: int = 5):
        self.num_philosophers = num_philosophers
        self.forks = [threading.Lock() for _ in range(num_philosophers)]
        self.philosophers = []
        self.running = True

    def philosopher(self, philosopher_id: int):
        """Philosopher function that avoids deadlock through asymmetric behavior."""
        left_fork = philosopher_id
        right_fork = (philosopher_id + 1) % self.num_philosophers

        print(f"Philosopher {philosopher_id} starting...")

        while self.running:
            print(f"Philosopher {philosopher_id} thinking...")
            time.sleep(0.1)

            # FIX: Asymmetric behavior - even philosophers pick up right fork first
            if philosopher_id % 2 == 0:
                # Even philosophers: right fork first, then left fork
                first_fork = right_fork
                second_fork = left_fork
                order = "right-then-left"
            else:
                # Odd philosophers: left fork first, then right fork (original behavior)
                first_fork = left_fork
                second_fork = right_fork
                order = "left-then-right"

            print(
                f"Philosopher {philosopher_id} ({order}) picking up fork {first_fork} first"
            )
            self.forks[first_fork].acquire()

            print(
                f"Philosopher {philosopher_id} ({order}) picking up fork {second_fork} second"
            )
            self.forks[second_fork].acquire()

            print(f"Philosopher {philosopher_id} eating...")
            time.sleep(0.2)

            print(f"Philosopher {philosopher_id} putting down forks")
            self.forks[second_fork].release()
            self.forks[first_fork].release()

            time.sleep(0.1)

    def run(self, duration: int = 5):
        """Run the asymmetric behavior fix example."""
        print(f"\n=== DEADLOCK FIX: Asymmetric Behavior ===")
        print(f"Running for {duration} seconds...")
        print(
            "This should NOT result in deadlock due to asymmetric fork picking order!\n"
        )
        print("Even philosophers: right fork first, then left fork")
        print("Odd philosophers: left fork first, then right fork\n")

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
        print("Asymmetric behavior fix example completed.\n")


if __name__ == "__main__":
    # Allow running this file directly for testing
    example = DeadlockFixAsymmetricBehavior()
    example.run(5)
