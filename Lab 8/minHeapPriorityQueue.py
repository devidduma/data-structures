import math

class MinHeapPriorityQueue:
    ''' A min-oriented priority queue implemented with a binary heap'''

    def __init__(self):
        '''create a new empty Priority Queue'''
        self.data = []
    
    def __len__(self):
        '''Return the number of items in the priority queue'''
        return len(self.data)
    
    def parent(self, j):
        '''returns the indices j’s parent indices number'''
        if(j < 0):
            j = len(self.data) + j 
        parentIndex = (j-1)//2
        return parentIndex

    def left(self, j):
        '''returns the indices j’s left child indices number'''
        if(j < 0):
            j = len(self.data) + j 
        leftIndex = 2*j + 1
        return leftIndex

    def right(self, j):
        '''returns the indices j’s right child indices number'''
        if(j < 0):
            j = len(self.data) + j 
        rightIndex = 2*j + 2
        return rightIndex
    
    def hasLeft(self, j):
        if(self.left(j) >= len(self.data)):
            return False
        return True

    def hasRight(self, j):
        if(self.right(j) >= len(self.data)):
            return False
        return True
    
    def swap(self, i, j):
        '''swap the elements at indices i and j of array '''
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def upheap(self, j):
        # base case
        if(j == 0):
            return

        if(self.data[j] < self.data[self.parent(j)]):
            self.swap(j, self.parent(j))
            self.upheap(self.parent(j))
    
    def downheap(self, j):
        # base case
        if(not self.hasLeft(j) or not self.hasRight(j)):
            return

        if(self.data[self.left(j)] < self.data[self.right(j)]):
            minValAt = self.left(j)
        else:
            minValAt = self.right(j)

        if(self.data[minValAt] < self.data[j]):
            self.swap(minValAt, j)
            self.downheap(minValAt)

    def add(self, value):
        self.data.append(value)
        self.upheap(-1)
    
    def min(self):
        if(len(self.data) == 0):
            return None
        return self.data[0]
    
    def removeMin(self):
        if(len(self.data) == 0):
            return None
        
        minVal = self.min()
        self.data[0] = self.data[-1]
        self.data.pop(-1)
        self.downheap(0)

        return minVal

    def heightHeap(self):
        return math.floor(math.log(len(self.data), 2))
    
    def kSmallestElement(self, k):
        result = []
        minHeapPriorityQueue = MinHeapPriorityQueue()
        minHeapPriorityQueue.data = self.data[:]

        for _ in range(k):
            result.append(minHeapPriorityQueue.removeMin())
        
        return result


    def kLargestElement(self, k):
        # alternatively sorting the data list gives similar running time complexity

        result = []
        minHeapPriorityQueue = MinHeapPriorityQueue()
        minHeapPriorityQueue.data = self.data[:]

        for _ in range(minHeapPriorityQueue.__len__() - k):
            minHeapPriorityQueue.removeMin()

        for _ in range(k):
            result.append(minHeapPriorityQueue.removeMin())
        
        result.reverse()
        return result


# Driver Code
if __name__ == "__main__":
    
    # exercise 3
    input = [40, 30, 32, 35, 80, 90, 100, 120]

    minHeapPriorityQueue = MinHeapPriorityQueue()
    for i in input:
        minHeapPriorityQueue.add(i)
    print("minheap: ", minHeapPriorityQueue.data)

    # exercise 4
    ex4output = []
    minHeapPriorityQueue2 = MinHeapPriorityQueue()
    minHeapPriorityQueue2.data = minHeapPriorityQueue.data[:]

    while len(minHeapPriorityQueue2.data) > 0:
        ex4output.append(minHeapPriorityQueue2.removeMin())
    print("exercise 4 output: ",ex4output)

    # testing by myself
    print("Size: ", len(minHeapPriorityQueue.data))
    print("Height: ", minHeapPriorityQueue.heightHeap())
    print("5 smallest: ", minHeapPriorityQueue.kSmallestElement(5))
    print("Size: ", len(minHeapPriorityQueue.data))
    print("5 largest: ", minHeapPriorityQueue.kLargestElement(5))