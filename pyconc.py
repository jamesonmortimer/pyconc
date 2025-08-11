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


def main():
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
            example = DeadlockExample()
            example.run(args.duration)
        elif args.example == "deadlock-fix-resource-ordering":
            example = DeadlockFixResourceOrdering()
            example.run(args.duration)
        elif args.example == "deadlock-fix-timeout":
            example = DeadlockFixTimeout()
            example.run(args.duration)
        elif args.example == "deadlock-fix-asymmetric-behavior":
            example = DeadlockFixAsymmetricBehavior()
            example.run(args.duration)
        elif args.example == "deadlock-fix-waiter":
            example = DeadlockFixWaiter()
            example.run(args.duration)
        elif args.example == "livelock":
            example = LivelockExample()
            example.run(args.duration)
        elif args.example == "livelock-fix-random-backoff":
            example = LivelockFixRandomBackoff()
            example.run(args.duration)
        elif args.example == "livelock-fix-priority":
            example = LivelockFixPriority()
            example.run(args.duration)
        elif args.example == "starvation":
            example = StarvationExample()
            example.run(args.duration)
        elif args.example == "starvation-fix-fair-scheduling":
            example = StarvationFixFairScheduling()
            example.run(args.duration)
        elif args.example == "starvation-fix-aging":
            example = StarvationFixAging()
            example.run(args.duration)
        elif args.example == "threadpool":
            example = ThreadPoolExample()
            example.run(args.duration)
        elif args.example == "threadpool-polling-periodic":
            example = ThreadPoolPollingPeriodic()
            example.run(args.duration)
        elif args.example == "threadpool-polling-adaptive":
            example = ThreadPoolPollingAdaptive()
            example.run(args.duration)
        elif args.example == "threadpool-polling-event-driven":
            example = ThreadPoolPollingEventDriven()
            example.run(args.duration)
        elif args.example == "threadpool-polling-batch":
            example = ThreadPoolPollingBatch()
            example.run(args.duration)

    except KeyboardInterrupt:
        print("\n\nInterrupted by user. Exiting...")
    except Exception as e:
        print(f"\nError running example: {e}")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
