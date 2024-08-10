from concurrent.futures import ThreadPoolExecutor
import time


def task(n):
    print(f"Task {n} started")
    time.sleep(1)
    print(f"Task {n} completed")
    return n


# Create a ThreadPoolExecutor with a maximum of 3 threads
with ThreadPoolExecutor(max_workers=3) as executor:
    # Submit tasks to the executor
    futures = [executor.submit(task, i) for i in range(5)]

    # Retrieve results from futures
    for future in futures:
        result = future.result()
        print(f"Task result: {result}")

print("All tasks completed")
