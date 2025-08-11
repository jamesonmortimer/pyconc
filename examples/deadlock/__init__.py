"""
Deadlock package - Contains the original problem and various solutions.
Includes the classic dining philosophers problem and multiple fix implementations.
"""

from .deadlock_problem import DeadlockExample
from .deadlock_fix_resource_ordering import DeadlockFixResourceOrdering
from .deadlock_fix_timeout import DeadlockFixTimeout
from .deadlock_fix_asymmetric_behavior import DeadlockFixAsymmetricBehavior
from .deadlock_fix_waiter import DeadlockFixWaiter

__all__ = [
    "DeadlockExample",
    "DeadlockFixResourceOrdering",
    "DeadlockFixTimeout",
    "DeadlockFixAsymmetricBehavior",
    "DeadlockFixWaiter",
]
