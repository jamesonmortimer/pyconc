"""
Starvation package - Contains the starvation problem and various solutions.
Shows how some threads can be perpetually denied access to resources and multiple ways to fix it.
"""

from .starvation_problem import StarvationExample
from .starvation_fix_fair_scheduling import StarvationFixFairScheduling
from .starvation_fix_aging import StarvationFixAging

__all__ = ["StarvationExample", "StarvationFixFairScheduling", "StarvationFixAging"]
