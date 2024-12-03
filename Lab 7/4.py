class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def findMax(self, node = None):
        currentNode = node if node != None else self

        if currentNode.right_child != None:
            currentNode.findMax(currentNode.right_child)
        elif currentNode.value == None:
            print("-1")
        else:
            print(currentNode.value)
    