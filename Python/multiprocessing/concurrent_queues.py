"""queues allow us to pass data between processes"""
import concurrent.futures
import multiprocessing
import random
import time


def compute_task(task_id, queue):
    """Perform a "computationally intensive" task ;)"""
    count_to = queue.get()
    print(f"Starting task {task_id}. Counting up to {count_to:_}...")
    result = 0
    for i in range(count_to):
        result += i
    print(f"Finished task {task_id}.")
    return result

with multiprocessing.Manager() as manager:
    queue = manager.Queue()
    for _ in range(10):
        queue.put(random.randint(10_000_000, 50_000_000))

    start_time = time.monotonic()
    with concurrent.futures.ProcessPoolExecutor() as exector:
        futures = [exector.submit(compute_task, t_id, queue) for t_id in range(1, 11)]
        print("Submitted all tasks to the process pool.")
        results = []
        for i, future in enumerate(concurrent.futures.as_completed(futures)):
            print(f"Processing task {i+1}/10...")
            result = future.result()
            print(f"Got result from task {i+1}: {result:_}")

print(f"Finished in {(time.monotonic() - start_time):.2f} seconds.")
