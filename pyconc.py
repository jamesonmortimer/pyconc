#!/usr/bin/env python3
"""
Python Concurrency Examples
A command-line tool to demonstrate various concurrency concepts:
- deadlock: Classic dining philosophers problem
- deadlock-fix-*: Various solutions to the deadlock problem
- livelock: Two threads trying to be polite
- livelock-fix-*: Various solutions to the livelock problem
- starvation: Resource allocation that can lead to starvation
- starvation-fix-*: Various solutions to the starvation problem
- threadpool: ThreadPoolExecutor examples
- threadpool-polling-*: Various polling strategies using thread pools
"""

import argparse
from typing import Any

# Import example classes from their respective files in the examples folder
from examples.deadlock import (
    DeadlockExample,
    DeadlockFixResourceOrdering,
    DeadlockFixTimeout,
    DeadlockFixAsymmetricBehavior,
    DeadlockFixWaiter,
)
from examples.livelock import (
    LivelockExample,
    LivelockFixRandomBackoff,
    LivelockFixPriority,
)
from examples.starvation import (
    StarvationExample,
    StarvationFixFairScheduling,
    StarvationFixAging,
)
from examples.threadpool import (
    ThreadPoolExample,
    ThreadPoolPollingPeriodic,
    ThreadPoolPollingAdaptive,
    ThreadPoolPollingEventDriven,
    ThreadPoolPollingBatch,
)


def main() -> int:
    """Main function to handle command line arguments and run examples."""
    parser = argparse.ArgumentParser(
        description="Python Concurrency Examples",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 pyconc.py -e deadlock
  python3 pyconc.py -e deadlock-fix-resource-ordering
  python3 pyconc.py -e deadlock-fix-timeout
  python3 pyconc.py -e deadlock-fix-asymmetric-behavior
  python3 pyconc.py -e deadlock-fix-waiter
  python3 pyconc.py -e livelock
  python3 pyconc.py -e livelock-fix-random-backoff
  python3 pyconc.py -e livelock-fix-priority
  python3 pyconc.py -e starvation
  python3 pyconc.py -e starvation-fix-fair-scheduling
  python3 pyconc.py -e starvation-fix-aging
  python3 pyconc.py -e threadpool
  python3 pyconc.py -e threadpool-polling-periodic
  python3 pyconc.py -e threadpool-polling-adaptive
  python3 pyconc.py -e threadpool-polling-event-driven
  python3 pyconc.py -e threadpool-polling-batch
        """,
    )

    parser.add_argument(
        "-e",
        "--example",
        required=True,
        choices=[
            "deadlock",
            "deadlock-fix-resource-ordering",
            "deadlock-fix-timeout",
            "deadlock-fix-asymmetric-behavior",
            "deadlock-fix-waiter",
            "livelock",
            "livelock-fix-random-backoff",
            "livelock-fix-priority",
            "starvation",
            "starvation-fix-fair-scheduling",
            "starvation-fix-aging",
            "threadpool",
            "threadpool-polling-periodic",
            "threadpool-polling-adaptive",
            "threadpool-polling-event-driven",
            "threadpool-polling-batch",
        ],
        help="Type of concurrency example to run",
    )

    parser.add_argument(
        "-d",
        "--duration",
        type=int,
        default=5,
        help="Duration to run the example in seconds (default: 5)",
    )

    args = parser.parse_args()

    print("Python Concurrency Examples")
    print("=" * 50)

    try:
        if args.example == "deadlock":
            deadlock_example: Any = DeadlockExample()
            deadlock_example.run(args.duration)
        elif args.example == "deadlock-fix-resource-ordering":
            resource_ordering_example: Any = DeadlockFixResourceOrdering()
            resource_ordering_example.run(args.duration)
        elif args.example == "deadlock-fix-timeout":
            timeout_example: Any = DeadlockFixTimeout()
            timeout_example.run(args.duration)
        elif args.example == "deadlock-fix-asymmetric-behavior":
            asymmetric_example: Any = DeadlockFixAsymmetricBehavior()
            asymmetric_example.run(args.duration)
        elif args.example == "deadlock-fix-waiter":
            waiter_example: Any = DeadlockFixWaiter()
            waiter_example.run(args.duration)
        elif args.example == "livelock":
            livelock_example: Any = LivelockExample()
            livelock_example.run(args.duration)
        elif args.example == "livelock-fix-random-backoff":
            backoff_example: Any = LivelockFixRandomBackoff()
            backoff_example.run(args.duration)
        elif args.example == "livelock-fix-priority":
            priority_example: Any = LivelockFixPriority()
            priority_example.run(args.duration)
        elif args.example == "starvation":
            starvation_example: Any = StarvationExample()
            starvation_example.run(args.duration)
        elif args.example == "starvation-fix-fair-scheduling":
            fair_scheduling_example: Any = StarvationFixFairScheduling()
            fair_scheduling_example.run(args.duration)
        elif args.example == "starvation-fix-aging":
            aging_example: Any = StarvationFixAging()
            aging_example.run(args.duration)
        elif args.example == "threadpool":
            threadpool_example: Any = ThreadPoolExample()
            threadpool_example.run(args.duration)
        elif args.example == "threadpool-polling-periodic":
            periodic_example: Any = ThreadPoolPollingPeriodic()
            periodic_example.run(args.duration)
        elif args.example == "threadpool-polling-adaptive":
            adaptive_example: Any = ThreadPoolPollingAdaptive()
            adaptive_example.run(args.duration)
        elif args.example == "threadpool-polling-event-driven":
            event_driven_example: Any = ThreadPoolPollingEventDriven()
            event_driven_example.run(args.duration)
        elif args.example == "threadpool-polling-batch":
            batch_example: Any = ThreadPoolPollingBatch()
            batch_example.run(args.duration)

    except KeyboardInterrupt:
        print("\n\nInterrupted by user. Exiting...")
    except Exception as e:
        print(f"\nError running example: {e}")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
