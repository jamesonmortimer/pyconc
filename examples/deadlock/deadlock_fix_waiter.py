#!/usr/bin/env python3
"""
Deadlock Fix - Waiter Solution
Fixes deadlock by using a central waiter to coordinate fork allocation.
"""

import threading
import time
import queue


class DeadlockFixWaiter:
    """Fixes deadlock by using a central waiter to coordinate fork allocation."""

    def __init__(self, num_philosophers: int = 5):
        self.num_philosophers = num_philosophers
        self.forks = [threading.Lock() for _ in range(num_philosophers)]
        self.philosophers = []
        self.running = True

        # Waiter coordination
        self.waiter = threading.Lock()
        self.eating_philosophers = set()

    def can_eat(self, philosopher_id: int):
        """Check if philosopher can eat (has access to both forks)."""
        left_fork = philosopher_id
        right_fork = (philosopher_id + 1) % self.num_philosophers

        # Check if adjacent philosophers are eating
        left_philosopher = (philosopher_id - 1) % self.num_philosophers
        right_philosopher = (philosopher_id + 1) % self.num_philosophers

        return (
            left_philosopher not in self.eating_philosophers
            and right_philosopher not in self.eating_philosophers
        )

    def philosopher(self, philosopher_id: int):
        """Philosopher function that avoids deadlock through waiter coordination."""
        left_fork = philosopher_id
        right_fork = (philosopher_id + 1) % self.num_philosophers

        print(f"Philosopher {philosopher_id} starting...")

        while self.running:
            print(f"Philosopher {philosopher_id} thinking...")
            time.sleep(0.1)

            # FIX: Use waiter to coordinate fork allocation
            while self.running:
                with self.waiter:
                    if self.can_eat(philosopher_id):
                        # Mark this philosopher as eating
                        self.eating_philosophers.add(philosopher_id)
                        print(f"Philosopher {philosopher_id}: Waiter approved eating")
                        break
                    else:
                        print(
                            f"Philosopher {philosopher_id}: Waiter says wait, adjacent philosophers are eating"
                        )

                # Wait a bit before asking waiter again
                time.sleep(0.1)

            if not self.running:
                break

            # Now safely acquire both forks (waiter ensures no conflicts)
            print(f"Philosopher {philosopher_id} picking up left fork {left_fork}")
            self.forks[left_fork].acquire()

            print(f"Philosopher {philosopher_id} picking up right fork {right_fork}")
            self.forks[right_fork].acquire()

            print(f"Philosopher {philosopher_id} eating...")
            time.sleep(0.2)

            print(f"Philosopher {philosopher_id} putting down forks")
            self.forks[right_fork].release()
            self.forks[left_fork].release()

            # Notify waiter that we're done eating
            with self.waiter:
                self.eating_philosophers.remove(philosopher_id)
                print(f"Philosopher {philosopher_id}: Notified waiter, done eating")

            time.sleep(0.1)

    def run(self, duration: int = 5):
        """Run the waiter fix example."""
        print(f"\n=== DEADLOCK FIX: Waiter Solution ===")
        print(f"Running for {duration} seconds...")
        print("This should NOT result in deadlock due to waiter coordination!\n")
        print("A central waiter ensures no adjacent philosophers eat simultaneously.\n")

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
        print("Waiter fix example completed.\n")


if __name__ == "__main__":
    # Allow running this file directly for testing
    example = DeadlockFixWaiter()
    example.run(5)
