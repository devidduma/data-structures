from singlyQueue import SinglyQueue

singlyQueue = SinglyQueue()
singlyQueue.summary()

singlyQueue.enqueue(10)
singlyQueue.enqueue("Hi")
singlyQueue.enqueue(100)
singlyQueue.enqueue("There")
singlyQueue.summary()

singlyQueue.dequeue()
singlyQueue.summary()
singlyQueue.dequeue()
singlyQueue.summary()
singlyQueue.dequeue()
singlyQueue.summary()

singlyQueue.enqueue("ToDelete")
singlyQueue.pop(1)
singlyQueue.summary()