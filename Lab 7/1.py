class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_node(self, value, node = None):
        currentNode = node if node != None else self

        if value <= currentNode.value:
            if currentNode.left_child == None:
                currentNode.left_child = BinarySearchTree(value)
            else:
                currentNode.insert_node(value, node=currentNode.left_child)
        else:
            if currentNode.right_child == None:
                currentNode.right_child = BinarySearchTree(value)
            else:
                currentNode.insert_node(value, node=currentNode.right_child)
    