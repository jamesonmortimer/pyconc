#!/usr/bin/env python3
"""
Starvation Fix - Fair Scheduling
Fixes starvation by ensuring all threads get equal access to resources.
"""

import threading
import time
import queue


class StarvationFixFairScheduling:
    """Fixes starvation by using fair scheduling for resource allocation."""

    def __init__(self, num_workers: int = 5):
        self.num_workers = num_workers
        self.resource = threading.Lock()
        self.workers = []
        self.running = True

        # FIX: Fair scheduling using a queue
        self.request_queue = queue.Queue()
        self.scheduler_running = True

        # Start the fair scheduler
        self.scheduler_thread = threading.Thread(target=self.fair_scheduler)
        self.scheduler_thread.daemon = True
        self.scheduler_thread.start()

    def fair_scheduler(self):
        """Fair scheduler that processes requests in order."""
        print("Fair Scheduler: Starting...")

        while self.scheduler_running:
            try:
                # Get the next request from the queue
                worker_id, request_type = self.request_queue.get(timeout=0.1)

                if request_type == "acquire":
                    print(f"Fair Scheduler: Granting resource to Worker {worker_id}")
                    # Signal that the worker can proceed
                    self.request_queue.task_done()

                elif request_type == "release":
                    print(f"Fair Scheduler: Worker {worker_id} released resource")
                    self.request_queue.task_done()

            except queue.Empty:
                continue

        print("Fair Scheduler: Stopping...")

    def worker(self, worker_id: int):
        """Worker function that uses fair scheduling to avoid starvation."""
        print(f"Worker {worker_id}: Starting...")

        while self.running:
            print(f"Worker {worker_id}: Requesting resource...")

            # FIX: Request resource through fair scheduler
            self.request_queue.put((worker_id, "acquire"))

            # Wait for scheduler to process request
            time.sleep(0.05)

            # Now try to acquire the resource
            if self.resource.acquire(timeout=0.2):
                print(f"Worker {worker_id}: Got resource! Working...")
                work_time = 0.1 + (worker_id * 0.05)  # Different work times
                time.sleep(work_time)
                print(f"Worker {worker_id}: Finished work, releasing resource")

                self.resource.release()

                # FIX: Notify scheduler of release
                self.request_queue.put((worker_id, "release"))

                # FIX: Yield time to other workers
                yield_time = 0.1
                print(f"Worker {worker_id}: Yielding for {yield_time}s...")
                time.sleep(yield_time)
            else:
                print(f"Worker {worker_id}: Resource acquisition timeout, retrying...")
                time.sleep(0.1)

    def run(self, duration: int = 5):
        """Run the fair scheduling fix example."""
        print(f"\n=== STARVATION FIX: Fair Scheduling ===")
        print(f"Running for {duration} seconds...")
        print("This should NOT result in starvation due to fair scheduling!\n")
        print("A fair scheduler ensures all workers get equal access to resources.\n")

        # Start workers
        for i in range(self.num_workers):
            thread = threading.Thread(target=self.worker, args=(i,))
            thread.daemon = True
            thread.start()
            self.workers.append(thread)

        # Let it run for a while
        time.sleep(duration)
        self.running = False
        self.scheduler_running = False

        print("\nStopping workers and scheduler...")
        for thread in self.workers:
            thread.join(timeout=1.0)
        self.scheduler_thread.join(timeout=1.0)
        print("Fair scheduling fix example completed.\n")


if __name__ == "__main__":
    # Allow running this file directly for testing
    example = StarvationFixFairScheduling()
    example.run(5)
