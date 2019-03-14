total = 0


def add():
    # 1.dosomething1
    # 2.io操作
    # 1.dosomething3
    global total
    for i in range(1000000):
        total += 1


def desc():
    global total
    for i in range(1000000):
        total -= 1


import threading
from threading import Lock, RLock #可重入的锁
# 在同一线程里面,可以连续调用多次acquire,一定要注意acquire的次数要与release次数一致

lock = Lock()
thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)
thread1.start()
thread2.start()

def add1(a):
    lock.acquire()
    a += 1
    lock.release()

def desc1(a):
    lock.acquire()
    a -= 1
    lock.release()
"""
1. load a
2. load 1
3. +
4. 赋值给a
"""
import dis
print(dis.dis(add1))
print(dis.dis(desc1))

# thread1.join()
# thread2.join()
#
# print(total)

# 1. 用锁会影响性能
# 2. 会出现死锁
# 死锁的情况A(a, b)
"""
A(a, b)
acquire(a)
acquire(b)
B(b, a)
acquire(b)
acquire(a)
资源竞争
"""