from singlyQueue import SinglyQueue

# creates queue from list of elements
def createQueueFromList(list):
    # create SinglyQueue object and assign it to queue variable 
    queue = SinglyQueue()
    # for each element in the list
    for element in list:
        # enqueue the element
        queue.enqueue(element)
    # after finishing enqueueing, print message
    print("Queue created")
    # print summary of queue
    queue.summary()
    # return the queue
    return queue

# dequeue from queue n times
def dequeueNtimes(queue, n):
    # do this n times
    for _ in range(n):
        # deqeue first element
        queue.dequeue()
    # print helper message
    print("After ", n, " times dequeue()")
    # print summary
    queue.summary()

# pop at a specific index in queue
def popAt(queue, index):
    # pop at index
    queue.pop(index)
    # print helper message
    print("After pop(", index, ")")
    # print queue summary
    queue.summary()


# create queue from list and print messages
queue = createQueueFromList([1,2,3,4,5,6,7,8,9, 10, 11, 12])
# pop at index 0 and print messages
popAt(queue, 0)
# pop at index queue.size - 1 and print messages
popAt(queue, queue.size - 1)
# dequeue n times and print messages
dequeueNtimes(queue, 2)
# pop at index 20 and print messages
popAt(queue, 20)
# pop at index 2 and print messages
popAt(queue, 2)
# dequeue 100 times and print messages
dequeueNtimes(queue, 100)
# pop at index 1 and print messages
popAt(queue, 1)
# pop at index 1 and print messages
popAt(queue, 1)
# pop at index 0 and print messages
popAt(queue, 0)