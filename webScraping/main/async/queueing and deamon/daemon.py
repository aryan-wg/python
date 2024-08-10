import threading
import time

def function_of_daemon():
    print("the daemon function is now running will stay alive but will not block the program flow")
    x = 0
    while True:
        x+=1
        for i in range(200000):
            i**3
        print("I am doing stuff")
    print("daemon function finished")

def this_prints_something():
    print("this function ran and will be exiting now")


def this_prints_something_but_stays_alive():
    print("this function ran and is staying alive")
    x=0
    while True:
        x+=1
        break
    print("non daemon thread has now quit")


# def main():
#     thread1 = threading.Thread(target=function_of_daemon,daemon=True)
#     thread1.start()
#     thread2 = threading.Thread(target=this_prints_something)
#     thread2.start()
#     print("the daemon thread is ",thread1.is_alive())
#     print("the normal thread is ",thread2.is_alive())
#     print("the main function will now quit")


def main():
    thread1 = threading.Thread(target=function_of_daemon,daemon=True)
    thread1.start()
    thread2 = threading.Thread(target=this_prints_something_but_stays_alive())
    thread2.start()
    thread1.join()
    thread2.join()
    print("the daemon thread is ",thread1.is_alive())
    print("the normal thread is ",thread2.is_alive())
    print("the main function will now quit")
if __name__ == "__main__":
    main()

