from circularQueue import CircularQueue

circularQueue = CircularQueue()
circularQueue.summary()

circularQueue.enqueue(10)
circularQueue.enqueue("Hi")
circularQueue.enqueue(100)
circularQueue.enqueue("There")
circularQueue.summary()

circularQueue.dequeue()
circularQueue.summary()
circularQueue.dequeue()
circularQueue.summary()
circularQueue.dequeue()
circularQueue.summary()

circularQueue.enqueue("ToDelete")
circularQueue.pop(55)
circularQueue.summary()