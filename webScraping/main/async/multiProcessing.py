import time

import multiprocessing

def print_something():
    start = time.time()
    # name = input("what is your name")
    # print(f"Hello {name}")
    print(f"this is printing something and process took {time.time()-start}")

def this_does_heavy_stuff():
    start = time.time()
    print("claculation is started")
    for x in range(200000000):
        x**3
    print(f"the calculation took {time.time()-start}")

def main():
    print_something()
    processes = []
    for x in range(4):
        p = multiprocessing.Process(target=this_does_heavy_stuff)
        p.start()
        processes.append(p)
    for p in processes:
        p.join()

    # p2 =multiprocessing.Process(target=this_does_heavy_stuff())
    # p3 =multiprocessing.Process(target=this_does_heavy_stuff())
    # p4 =multiprocessing.Process(target=this_does_heavy_stuff())
    # p5 =multiprocessing.Process(target=this_does_heavy_stuff())
    # p6 =multiprocessing.Process(target=this_does_heavy_stuff())
    # p1.start()
    # p2.start()
    # p3.start()
    # p4.start()
    # p5.start()
# if __name__ == '__main__':
#     main()
main()