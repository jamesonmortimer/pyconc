#!/usr/bin/env python3
"""
Tests for deadlock examples
"""

import unittest
import time
from examples.deadlock import (
    DeadlockExample,
    DeadlockFixResourceOrdering,
    DeadlockFixTimeout,
    DeadlockFixAsymmetricBehavior,
    DeadlockFixWaiter,
)


class TestDeadlockExamples(unittest.TestCase):
    """Test cases for deadlock examples."""

    def test_deadlock_problem_creation(self):
        """Test that deadlock problem can be created."""
        example = DeadlockExample()
        self.assertIsNotNone(example)
        self.assertEqual(example.num_philosophers, 5)

    def test_deadlock_fix_resource_ordering_creation(self):
        """Test that resource ordering fix can be created."""
        example = DeadlockFixResourceOrdering()
        self.assertIsNotNone(example)
        self.assertEqual(example.num_philosophers, 5)

    def test_deadlock_fix_timeout_creation(self):
        """Test that timeout fix can be created."""
        example = DeadlockFixTimeout()
        self.assertIsNotNone(example)
        self.assertEqual(example.num_philosophers, 5)

    def test_deadlock_fix_asymmetric_behavior_creation(self):
        """Test that asymmetric behavior fix can be created."""
        example = DeadlockFixAsymmetricBehavior()
        self.assertIsNotNone(example)
        self.assertEqual(example.num_philosophers, 5)

    def test_deadlock_fix_waiter_creation(self):
        """Test that waiter fix can be created."""
        example = DeadlockFixWaiter()
        self.assertIsNotNone(example)
        self.assertEqual(example.num_philosophers, 5)

    def test_custom_philosopher_count(self):
        """Test that examples can be created with custom philosopher count."""
        example = DeadlockExample(num_philosophers=10)
        self.assertEqual(example.num_philosophers, 10)

    def test_short_duration_run(self):
        """Test that examples can run for a short duration without errors."""
        example = DeadlockFixResourceOrdering()
        # This should not raise an exception
        example.run(duration=1)
        # Give threads time to clean up
        time.sleep(0.1)


if __name__ == "__main__":
    unittest.main()
