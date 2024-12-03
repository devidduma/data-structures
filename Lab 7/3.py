class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def findMin(self, node = None):
        currentNode = node if node != None else self

        if currentNode.left_child != None:
            currentNode.findMin(currentNode.left_child)
        elif currentNode.value == None:
            print("-1")
        else:
            print(currentNode.value)
    