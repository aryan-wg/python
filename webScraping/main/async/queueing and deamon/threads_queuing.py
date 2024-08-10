import queue
import time
import random
import threading


counter  = 0

def increase_counter_unsafe():
    time.sleep(random.random())
    global counter
    time.sleep(random.random())
    print("original",counter)
    original = counter
    time.sleep(random.random())
    counter = original+1
    time.sleep(random.random())
    print(counter)


job_queue = queue.Queue()
counter_queue = queue.Queue()
counter_queue.put(0)
def increase_counter_safe():
    # this queue.get() method gets the current element in the queue
    # if there is no element available the queue it will wait till there is something in added in the queue
    print("entered the function")
    time.sleep(random.random())
    counterVal = counter_queue.get()
    print("original",counterVal)
    time.sleep(random.random())
    counterVal += 1
    time.sleep(random.random())
    counter_queue.put(counterVal)
    time.sleep(random.random())
    counter_queue.task_done()
    print("updated",counterVal)

if __name__ == "__main__":
    for i in range(10):
        # th = threading.Thread(target=increase_counter_unsafe)
        time.sleep(random.random())
        th = threading.Thread(target=increase_counter_safe)
        time.sleep(random.random())
        th.start()
        time.sleep(random.random())
    print(counter_queue.get())
