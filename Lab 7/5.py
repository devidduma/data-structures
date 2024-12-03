class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def findNode(self, data, node=None, firstCall = False):
        node = node if not firstCall else self

        if(node == None or node.value == None):
            return 0

        if(data < node.value):
            return node.findNode(data, node=node.left_child)
        elif(data > node.value):
            return node.findNode(data, node=node.right_child)
        else:
            return 1
        