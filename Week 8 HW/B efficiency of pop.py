import time
from singlyQueue import SinglyQueue

def how_long_to_run(fun, arg, msg=""):
    start_time = time.time()
    fun(arg)
    return msg, time.time() - start_time

singlyQueue = SinglyQueue()
n = int(1e2)
k = (0, int(n//2), int(n))
for idx in range(n+3):
    singlyQueue.enqueue(idx)
for ki in k:
    print(how_long_to_run(singlyQueue.pop, ki, msg="N = " + str(n) + " k = " + str(ki)))