import threading
import time
import heapq
import random
lock=threading.Lock()
command_heapq=[]
def fun1():
    while True:
        time.sleep(1)
        with lock:
            heapq.heappush(command_heapq,(random.randint(1,3),time.time(),"command"))
t1=threading.Thread(target=fun1)
t1.start()
def fun2():
    while True:
        time.sleep(2)
        if command_heapq:
            with lock:
                print(heapq.heappop(command_heapq)," all:", command_heapq)
t2=threading.Thread(target=fun2)
t2.start()