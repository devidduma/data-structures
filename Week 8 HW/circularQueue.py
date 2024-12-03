class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, next):
        self.next_node = next

class CircularQueue(object):
    def __init__(self):
        self.head = None
        self.last = None
        self.size = 0

    def __isEmpty(self):
        return self.head == None and self.last == None and self.size == 0
    
    def __get_size(self):
        return self.size

    def enqueue(self, data):    #add to the end of the list
        new_node = Node(data=data)
        if self.__isEmpty():
            self.head = new_node
            self.last = new_node
        else:
            self.last.set_next(new_node)
            self.last = new_node
        self.last.set_next(self.head)   # circular
        self.size += 1

    def dequeue(self):      # FIFO
        if not self.__isEmpty():
            self.head = self.head.get_next()
            self.last.set_next(self.head)   #circular
            self.size -= 1
    

    def __search(self, index): # search for element at index and return tuple (previous, current)
        current = None
        previous = None
        if index >= 0:  # no need for index < self.__get_size() since circular
            current = self.head
            for _ in range(index):
                    previous = current
                    current = current.get_next()
        return (previous, current)
    
    def pop(self, index):     # search for element at index and delete
        previous, current = self.__search(index)
        if current is not None:
            if previous is None:
                self.head = current.get_next()
            elif current is self.last:
                previous.set_next(current.get_next())
                self.last = previous
            elif current is self.head:
                previous.set_next(current.get_next())
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())
            self.size -= 1
    
    # print a nice summary
    def summary(self):
        print("Current size is ", self.__get_size())
        current = self.head
        counter = 0
        while counter != self.__get_size():
            print("Element ", counter, ": ", current.get_data())
            current = current.get_next()
            counter += 1
        print("")


    