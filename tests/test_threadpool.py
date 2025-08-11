#!/usr/bin/env python3
"""
Tests for threadpool examples
"""

import unittest
import time
from examples.threadpool import (
    ThreadPoolExample,
    ThreadPoolPollingPeriodic,
    ThreadPoolPollingAdaptive,
    ThreadPoolPollingEventDriven,
    ThreadPoolPollingBatch,
)


class TestThreadPoolExamples(unittest.TestCase):
    """Test cases for threadpool examples."""

    def test_threadpool_example_creation(self):
        """Test that basic threadpool example can be created."""
        example = ThreadPoolExample()
        self.assertIsNotNone(example)
        self.assertEqual(example.num_workers, 3)

    def test_periodic_polling_creation(self):
        """Test that periodic polling example can be created."""
        example = ThreadPoolPollingPeriodic()
        self.assertIsNotNone(example)
        self.assertEqual(example.num_workers, 3)

    def test_adaptive_polling_creation(self):
        """Test that adaptive polling example can be created."""
        example = ThreadPoolPollingAdaptive()
        self.assertIsNotNone(example)
        self.assertEqual(example.num_workers, 3)

    def test_event_driven_polling_creation(self):
        """Test that event-driven polling example can be created."""
        example = ThreadPoolPollingEventDriven()
        self.assertIsNotNone(example)
        self.assertEqual(example.num_workers, 3)

    def test_batch_polling_creation(self):
        """Test that batch polling example can be created."""
        example = ThreadPoolPollingBatch()
        self.assertIsNotNone(example)
        self.assertEqual(example.num_workers, 3)

    def test_custom_worker_count(self):
        """Test that examples can be created with custom worker count."""
        example = ThreadPoolPollingPeriodic(num_workers=5)
        self.assertEqual(example.num_workers, 5)

    def test_short_duration_run(self):
        """Test that examples can run for a short duration without errors."""
        example = ThreadPoolPollingPeriodic()
        # This should not raise an exception
        example.run(duration=1)
        # Give threads time to clean up
        time.sleep(0.1)

    def test_adaptive_polling_parameters(self):
        """Test that adaptive polling has correct default parameters."""
        example = ThreadPoolPollingAdaptive()
        self.assertEqual(example.base_interval, 1.0)
        self.assertEqual(example.min_interval, 0.2)
        self.assertEqual(example.max_interval, 3.0)

    def test_batch_polling_parameters(self):
        """Test that batch polling has correct default parameters."""
        example = ThreadPoolPollingBatch()
        self.assertEqual(example.batch_size, 5)
        self.assertEqual(example.max_wait_time, 2.0)


if __name__ == "__main__":
    unittest.main()
