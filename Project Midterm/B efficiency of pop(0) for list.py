import time

# function that checks the running time of the function fun 
def how_long_to_run(fun, arg, msg=""):
    # save starting time
    start_time = time.time()
    # execute fun
    fun(arg)
    # print message with running time
    return msg, time.time() - start_time

# possible sizes of the queue
allN = [int(1e3), int(1e4), int(1e5), int(1e6)]

# for one possible n
for n in allN:
    # create list object
    list = []

    # append to list n+3 times
    for idx in range(n+3):
        # append to list
        list.append(idx)
    
    # possible indices
    allK = [0, n//2, n]

    for k in allK:
        # print running time of singlyQueue.dequeue()
        print(how_long_to_run(list.pop, k, msg="N = " + str(n) + ", K = " + str(k)))
    
    # print endline
    print("")