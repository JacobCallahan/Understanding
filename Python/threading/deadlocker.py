"""There are some patterns to be careful to avoid when using threads"""
import threading

LOCK_1 = threading.Lock()
LOCK_2 = threading.Lock()

def thread1():
    LOCK_1.acquire()
    print("Thread 1 acquired lock1")
    LOCK_2.acquire()
    print("Thread 1 acquired lock2")
    LOCK_2.release()
    LOCK_1.release()

def thread2():
    LOCK_2.acquire()
    print("Thread 2 acquired lock2")
    LOCK_1.acquire()
    print("Thread 2 acquired lock1")
    LOCK_1.release()
    LOCK_2.release()

t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)

t1.start()
t2.start()

t1.join()
t2.join()
