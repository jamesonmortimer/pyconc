"""
Examples package for Python Concurrency demonstrations.
Contains various concurrency examples including deadlock, livelock, starvation, and threadpool.
"""

# Import from the deadlock package
from .deadlock import (
    DeadlockExample,
    DeadlockFixResourceOrdering,
    DeadlockFixTimeout,
    DeadlockFixAsymmetricBehavior,
    DeadlockFixWaiter,
)

# Import from the livelock package
from .livelock import LivelockExample, LivelockFixRandomBackoff, LivelockFixPriority

# Import from the starvation package
from .starvation import (
    StarvationExample,
    StarvationFixFairScheduling,
    StarvationFixAging,
)

# Import from the threadpool package
from .threadpool import (
    ThreadPoolExample,
    ThreadPoolPollingPeriodic,
    ThreadPoolPollingAdaptive,
    ThreadPoolPollingEventDriven,
    ThreadPoolPollingBatch,
)

__all__ = [
    # Deadlock examples
    "DeadlockExample",
    "DeadlockFixResourceOrdering",
    "DeadlockFixTimeout",
    "DeadlockFixAsymmetricBehavior",
    "DeadlockFixWaiter",
    # Livelock examples
    "LivelockExample",
    "LivelockFixRandomBackoff",
    "LivelockFixPriority",
    # Starvation examples
    "StarvationExample",
    "StarvationFixFairScheduling",
    "StarvationFixAging",
    # ThreadPool examples
    "ThreadPoolExample",
    "ThreadPoolPollingPeriodic",
    "ThreadPoolPollingAdaptive",
    "ThreadPoolPollingEventDriven",
    "ThreadPoolPollingBatch",
]
