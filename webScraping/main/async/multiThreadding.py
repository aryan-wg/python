import threading
import time
from concurrent.futures import ThreadPoolExecutor

def does_something(number):
    start = time.time()
    # print(start)
    print(f"This is the thread number {number}")
    for i in range(20000000):
        i**3
    print(f"Thread no {number} has finished in {time.time()}")

def main():
    with ThreadPoolExecutor(max_workers=6) as thread:
        for i in range(12):
            thread.submit(does_something,i)
        # t1 = threading.Thread(target = does_something,args=(i,))
        # t1.start()

if __name__ == "__main__":
    main()