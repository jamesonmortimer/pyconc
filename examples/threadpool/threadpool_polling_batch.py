#!/usr/bin/env python3
"""
ThreadPool Example - Batch Polling
Demonstrates using ThreadPoolExecutor for batch processing of collected items.
"""

import threading
import time
import random
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
import queue


class ThreadPoolPollingBatch:
    """Demonstrates batch polling using ThreadPoolExecutor."""

    def __init__(self, num_workers: int = 3):
        self.num_workers = num_workers
        self.executor = ThreadPoolExecutor(max_workers=num_workers)
        self.running = True
        self.tasks = []

        # Batch processing parameters
        self.batch_size = 5
        self.max_wait_time = 2.0  # Maximum time to wait for batch to fill

        # Data collection queue
        self.data_queue = queue.Queue()

        # Batch processor thread
        self.batch_processor = None

        # Statistics
        self.batches_processed = 0
        self.total_items_processed = 0

    def data_collector(self):
        """Collects data items for batch processing."""
        print("Data Collector: Starting...")

        item_id = 0
        while self.running:
            # Simulate data collection
            data_item = {
                "id": item_id,
                "timestamp": datetime.now().strftime("%H:%M:%S.%f")[:-3],
                "value": random.randint(1, 100),
                "source": f"Source_{random.randint(1, 3)}",
            }

            self.data_queue.put(data_item)
            print(f"Data Collector: Collected item {item_id} (value: {data_item['value']})")

            item_id += 1

            # Random delay between collections
            time.sleep(random.uniform(0.1, 0.8))

        print("Data Collector: Stopping...")

    def batch_processor_worker(self):
        """Processes batches of collected data."""
        print("Batch Processor: Starting...")

        while self.running:
            batch = []
            batch_start_time = time.time()

            # Collect items for batch
            while len(batch) < self.batch_size:
                try:
                    # Wait for items with timeout
                    remaining_time = self.max_wait_time - (time.time() - batch_start_time)
                    if remaining_time <= 0:
                        break

                    item = self.data_queue.get(timeout=min(0.1, remaining_time))
                    batch.append(item)

                except queue.Empty:
                    # No more items available
                    break

            if batch:
                # Process the batch
                self.process_batch(batch)
                self.batches_processed += 1
                self.total_items_processed += len(batch)

                # Mark all items as done
                for _ in range(len(batch)):
                    self.data_queue.task_done()
            else:
                # No items to process, wait a bit
                time.sleep(0.1)

        print("Batch Processor: Stopping...")

    def process_batch(self, batch: list):
        """Process a batch of data items."""
        print(f"\nBatch Processor: Processing batch of {len(batch)} items:")

        # Calculate batch statistics
        values = [item["value"] for item in batch]
        total_value = sum(values)
        avg_value = total_value / len(values)
        min_value = min(values)
        max_value = max(values)

        print(f"  Items: {[item['id'] for item in batch]}")
        print(f"  Values: {values}")
        print(f"  Total: {total_value}, Average: {avg_value:.1f}")
        print(f"  Range: {min_value} - {max_value}")

        # Simulate batch processing work
        work_time = 0.1 + (len(batch) * 0.05)
        time.sleep(work_time)

        print(f"  Batch processed in {work_time:.3f}s")

    def individual_processor(self, worker_id: int):
        """Individual worker that processes single items when needed."""
        print(f"Individual Processor {worker_id}: Starting...")

        while self.running:
            try:
                # Try to get an item for individual processing
                item = self.data_queue.get(timeout=0.2)

                print(f"Individual Processor {worker_id}: Processing item {item['id']} " f"(value: {item['value']})")

                # Simulate individual processing
                process_time = 0.05 + (item["value"] * 0.001)
                time.sleep(process_time)

                print(f"Individual Processor {worker_id}: Completed item {item['id']} " f"in {process_time:.3f}s")

                # Mark as done
                self.data_queue.task_done()

            except queue.Empty:
                # No items available, wait a bit
                time.sleep(0.1)

        print(f"Individual Processor {worker_id}: Stopping...")

    def run(self, duration: int = 5):
        """Run the batch polling example."""
        print("\n=== THREADPOOL: Batch Polling ===")
        print(f"Running for {duration} seconds...")
        print(f"Using {self.num_workers} workers for batch processing\n")
        print(f"Batch size: {self.batch_size}, Max wait time: {self.max_wait_time}s")
        print("Data is collected and processed in batches for efficiency.\n")

        # Start data collector
        collector_thread = threading.Thread(target=self.data_collector)
        collector_thread.daemon = True
        collector_thread.start()

        # Start batch processor
        self.batch_processor = threading.Thread(target=self.batch_processor_worker)
        self.batch_processor.daemon = True
        self.batch_processor.start()

        # Submit individual processor tasks
        for i in range(self.num_workers):
            future = self.executor.submit(self.individual_processor, i)
            self.tasks.append(future)

        # Let it run for the specified duration
        time.sleep(duration)
        self.running = False

        print("\nStopping batch polling...")

        # Wait for threads to finish
        collector_thread.join(timeout=1.0)
        if self.batch_processor:
            self.batch_processor.join(timeout=1.0)

        # Wait for all worker tasks to complete
        for future in as_completed(self.tasks, timeout=2.0):
            try:
                future.result()
            except Exception as e:
                print(f"Task completed with exception: {e}")

        self.executor.shutdown(wait=True)

        # Print final statistics
        print("\nFinal Statistics:")
        print(f"  Batches Processed: {self.batches_processed}")
        print(f"  Total Items Processed: {self.total_items_processed}")
        print(f"  Average Batch Size: {self.total_items_processed / max(1, self.batches_processed):.1f}")

        print("Batch polling example completed.\n")


if __name__ == "__main__":
    # Allow running this file directly for testing
    example = ThreadPoolPollingBatch()
    example.run(5)
