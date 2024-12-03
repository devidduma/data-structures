import time
from singlyQueue import SinglyQueue
from circularQueue import CircularQueue

# function that checks the running time of the function fun 
def how_long_to_run(fun, msg=""):
    # save starting time
    start_time = time.time()
    # execute fun
    fun()
    # print message with running time
    return msg, time.time() - start_time

# possible sizes of the queue
allN = [int(1e3), int(1e4), int(1e5), int(1e6)]

# for one possible n
for n in allN:
    # n times
    for idx in range(n):
        # create singlyQueue object
        singlyQueue = SinglyQueue()
        # create circularQueue object
        circularQueue = CircularQueue()
        # enqueue idx to singlyQueue
        singlyQueue.enqueue(idx)
        # enqueue idx to singlyQueue
        circularQueue.enqueue(idx)

    # print running time of singlyQueue.dequeue()
    print(how_long_to_run(singlyQueue.dequeue, msg="N = " + str(n)))
    # print running time of circularQueue.dequeue()
    print(how_long_to_run(circularQueue.dequeue, msg="N = " + str(n)))
    # print endline
    print("")