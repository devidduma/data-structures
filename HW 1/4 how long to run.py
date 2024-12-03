import numpy as np
import time

def prefix_average1(S):
    n=len(S)
    A=[0]*n
    for j in range(n):
        total=0
        for i in range(j+1):
            total+=S[i]
            A[j]=total/(j+1)
    return A

def prefix_average2(S):
    n=len(S)
    A=[0]*n
    for j in range(n):
        A[j]=sum(S[0:j+1])/(j+1)
    return A

def prefix_average3(S):
    n=len(S)
    A=[0]*n
    total=0
    for j in range(n):
        total+=S[j]
        A[j]=total/(j+1)
    return A

def how_long_to_run(fun, arg, msg=""):
    start_time = time.time()
    fun(arg)
    return msg, time.time() - start_time

def scoreboard(size):
    print("\n")
    print("For", size, "entries, all 0")
    entries = [0] * size
    print(how_long_to_run(prefix_average1, entries, "prefix_average1: "))
    print(how_long_to_run(prefix_average2, entries, "prefix_average2: "))
    print(how_long_to_run(prefix_average3, entries, "prefix_average3: "))
    print("For", size, "entries, uniform randomly chosen from -1 to 1")
    entries = np.random.uniform(-1, 1, size=size)
    print(how_long_to_run(prefix_average1, entries, "prefix_average1: "))
    print(how_long_to_run(prefix_average2, entries, "prefix_average2: "))
    print(how_long_to_run(prefix_average3, entries, "prefix_average3: "))

for pow in range(2,6):
    scoreboard(10**pow)