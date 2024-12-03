# Nodes for CircularQueue
# singly linked means store only next_node variable
class Node(object):
    # constructor of Node object with default parameters
    def __init__(self, data=None, next_node=None):
        # assign value to data object variable
        self.data = data
        # asign value to next_node object variable
        self.next_node = next_node

    # getter for data
    def get_data(self):
        # return the data variable
        # everything in python is an identifier / pointer to an object
        # so if there is any assignment operator after calling this function, it copies the value of the identifier / pointer
        # same applies to any function returning anything
        return self.data

    # getter for next_node
    def get_next(self):
        # return the next_node variable
        # everything in python is an identifier / pointer to an object
        # so if there is any assignment operator after calling this function, it copies the value of the identifier / pointer
        # same applies to any function returning anything
        return self.next_node

    # setter for next_node
    def set_next(self, next):
        # assign next to next_node
        self.next_node = next

# Circular Queue class definition
class CircularQueue(object):
    # constructor of CircularQueue object
    def __init__(self):
        # save head of queue object
        self.head = None
        # save last element of queue object
        self.last = None
        # save size information
        self.size = 0

    # boolean function
    def __isEmpty(self):
        # return boolean value of expression
        # it is empty if head and last are None and size == 0
        return self.head == None and self.last == None and self.size == 0
    
    # getter for size, intended to be used inside other functions declared here
    # as helper function and not outside the class definition
    def __get_size(self):
        # return size of queue
        return self.size

    #add to the end of the list
    def enqueue(self, data):
        # assign new_node an object created calling the constructor with self.data = data
        new_node = Node(data=data)
        # if self / this object is empty
        if self.__isEmpty():
            # assign new_node object to head
            self.head = new_node
            # assign new_node object to last
            self.last = new_node
        else:
            # assign new_node object to the end of the queue
            self.last.set_next(new_node)
            # update last to point to new_node object
            self.last = new_node
        # make the queue circular
        self.last.set_next(self.head)   # circular
        # increment size
        self.size += 1

    # FIFO
    def dequeue(self):
        # initialize data to None
        data = None
        # if self / this object is not empty
        if not self.__isEmpty():
            # save head.data into a temporary variable data
            data = self.head.get_data()
            # special case: if head is last, then size = 1
            if self.head is self.last:
                # set both head and last to None
                self.head = self.last = None
                # set size to 0
                self.size = 0
            else:
                # update head to point to next node
                # send old head to garbage collection
                self.head = self.head.get_next()
                # make queue circular again
                self.last.set_next(self.head)   #circular
                # decrement size
                self.size -= 1
        # return temporary data variable
        return data
    
    # search for element at index and return tuple (previous, current)
    def __search(self, index):
        # initialize temp variable current to None
        current = None
        # initialize temp variable previous to None
        previous = None
        # if index >= 0
        # if size == 0, we can't find anything
        if index >= 0 and self.size != 0:  # no need for index < self.__get_size() since circular
            # modulo: if we do a full cycle (self.size times iterations), we come back where we started
            index = index % self.size
            # starting from head
            current = self.head
            # do this index times
            for _ in range(index):
                    # move previous to current
                    previous = current
                    # move current to next node
                    current = current.get_next()
        # if current points to head then previous should point to last
        if current is not None and previous is None:    # circular
            # assign last to previous
            previous = self.last
        # return tuple (previous node, node we were searching for)
        # note: either none or both previous and current can be None
        return (previous, current)
    
    # search for element at index and delete
    def pop(self, index):
        # get previous node and node we want to pop
        previous, current = self.__search(index)
        # if node we want to pop is None, we can't pop anything
        if current is not None:
            # if previous is current, then current = head
            if previous is current:
                # send head to garbage collection
                self.head = None
            # otherwise, size > 1 and current is last element
            elif current is self.last:
                # update previous to head
                previous.set_next(current.get_next())
                # move back and send old last element to garbage collection
                self.last = previous
            # otherwise, size > 1 and current is pointing to head.
            # so previous is pointing to last
            elif current is self.head:
                # connect last to 2nd element
                previous.set_next(current.get_next())
                # move head to 2nd element and send old head to garbage collector
                self.head = current.get_next()
            # otherwise we are somewhere in the middle
            else:
                # send current to garbage collector
                previous.set_next(current.get_next())
            # decrement size
            self.size -= 1
    
    # print a nice summary
    def summary(self):
        # current size information
        print("Current size is ", self.__get_size())
        # print information about all other elements, if any
        # initialize temporary variable current to head
        current = self.head
        # initialize temp counter to 0 to represent index
        counter = 0
        # if we are outside of the range of elements
        while counter != self.__get_size():
            # print current element's index and data
            print("Element ", counter, ": ", current.get_data())
            # move to next element
            current = current.get_next()
            # increment counter
            counter += 1
        # print endline
        print("")


    