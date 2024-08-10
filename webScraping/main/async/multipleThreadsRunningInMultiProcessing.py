import time
import threading
import concurrent.futures
import multiprocessing

def thread_inside_process(processNo,threadNo):
    # print(f"this is thread no {threadNo} of process no {processNo}")
    print(f"thread {processNo}.{threadNo} started")
    for i in range(200000000):
        i**3
    print(f"thread {processNo}.{threadNo} finished")
    # print(f"thread no {threadNo} of process no {processNo} has finished")

def process_function (no):
    print(f"process no {no} started")
    for i in range(5):
        t = threading.Thread(target=thread_inside_process, args=(no, i,))
        t.start()
        t.join()
    print(f"process no {no} finished on {time.time()}")

if __name__ == "__main__":
    print("this program will make 12 processes that will have 5 threads each")
    for i in range(2):
        multiprocessing.Process(target=process_function,args = (i,)).start()

