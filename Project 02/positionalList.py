# Node of Linked List
class Node:
    # constructor with default params
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        # doubly linked list
        self.left = left
        self.right = right

    # getter
    def get_data(self):
        return self.data

    # getter
    def get_right(self):
        return self.right

    # setter
    def set_right(self, right):
        self.right = right

    # getter
    def get_left(self):
        return self.left

    # setter
    def set_left(self, left):
        self.left = left


# Doubly Linked List Class
class DoublyLinkedList:

    # nested Position wrapper to use as positional linked list
    class Position:
        # constructor of Position
        def __init__(self, node):
            self.node = node

        # returns node element
        def element(self):
            return self.node

        # checks if it is equal
        def isEqual(self, other):
            return type(other) is type(self) and other.node is self.node

    # constructor of DoublyLinkedList
    def __init__(self, text=None):
        self.head = None
        self.tail = None
        self.size = 0

        # initialize list by string
        if text is not None:
            for i in text:
                self.push_back(i)

    # checks if list is empty
    def __isEmpty__(self):
        return self.head is None and self.tail is None and self.size == 0

    # getter
    def __get_size__(self):
        return self.size

    # add to the end of the list
    def push_back(self, data):
        # create new node to be added
        new_node = Node(data=data)
        # if list is empty
        if self.__isEmpty__():
            # update head and tail to same new node
            self.head = new_node
            self.tail = new_node
        else:
            # set right
            self.tail.set_right(new_node)
            # set left: doubly linked list
            self.tail.get_right().set_left(self.tail)
            # update tail
            self.tail = new_node
        self.size += 1

    # insert method using positional framework
    def insert(self, position, data):
        # if list is empty
        if self.head is None and self.tail is None:

            # update head and tail to new data
            self.head = self.tail = Node(data=data)
            # update position to point to head
            position = DoublyLinkedList.Position(self.head)
        # otherwise, list is not empty
        else:
            # create new node with left and right links
            node = Node(data=data, left=position.element(), right=position.element().get_right())
            # set right of position element
            position.element().set_right(node)

            # if right is not None
            if node.get_right() is not None:
                # set left of inserted element
                node.get_right().set_left(node)

            # if position was tail
            if position.element() is self.tail:
                # update tail to new node
                self.tail = position.element().get_right()

        # in any case, update size
        self.size += 1
        # return
        return position

    # search for element at index and return tuple (previous, current)
    def __search__(self, index):
        # initialize
        current = None
        previous = None
        # ternary comparison statement
        if self.__get_size__() > index >= 0:
            # start from head
            current = self.head
            # iterate index times
            for _ in range(index):
                # move forward
                previous = current
                current = current.get_right()
        # return tuple (previous, current)
        return previous, current

    # delete method using positional framework
    # we have to pass list as an argument if we need to update head or tail
    def delete(self, position):
        if position.element() is None:
            return position
        else:
            # if left element is not None
            if position.element().get_left() is not None:
                # link left with right element
                position.element().get_left().set_right(position.element().get_right())
            # else, if left-most position
            else:
                # update head to it's right
                self.head = self.head.get_right()

            # if right element is not None
            if position.element().get_right() is not None:
                # link right with left element
                position.element().get_right().set_left(position.element().get_left())
            # else, if right-most position
            else:
                # update tail to it's left
                self.tail = self.tail.get_left()

            # in any case, decrease size if applicable
            if self.size != 0:
                self.size -= 1
            # if not right-most element, move position to right element
            if position.element().get_right() is not None:
                position = DoublyLinkedList.Position(position.element().get_right())
            # if right-most element, move position to left element
            else:
                position = DoublyLinkedList.Position(position.element().get_left())
            return position

    # search for element at index and delete
    def deleteAtIndex(self, index):
        # find previous and current from search
        previous, current = self.__search__(index)
        # if current found some element
        if current is not None:
            # if current left-most element
            if previous is None:
                # move head to the right
                self.head = current.get_right()
                # set left to None
                current.get_right().set_left(None)
            # if current right-most element
            elif current is self.tail:
                # link previous with None
                previous.set_right(current.get_right())
                # update tail
                self.tail = previous
            # otherwise
            else:
                # link previous with next
                previous.set_right(current.get_right())
                # link next with previous
                previous.get_right().set_left(previous)
            # decrease size
            self.size -= 1

    # move position to the left if possible
    def moveLeft(self, position):
        # if position element is None, do nothing
        if position.element() is None:
            return position
        else:
            # if not left-most element
            if position.element().get_left() is not None:
                # return left position
                return DoublyLinkedList.Position(position.element().get_left())
            # otherwise
            else:
                # do not do any changes
                return position

    # move position to the right if possible
    def moveRight(self, position):
        # if position element is None, do nothing
        if position.element() is None:
            return position
        else:
            # if not right-most element
            if position.element().get_right() is not None:
                # return right position
                return DoublyLinkedList.Position(position.element().get_right())
            # otherwise
            else:
                # do not do any changes
                return position

    # print elements as text
    def text(self):
        # start from head
        current = self.head
        # initialize text to empty
        text = ""
        # iterate until last element
        while current is not None:
            # add to text string
            text += current.get_data()
            # move to right
            current = current.get_right()
        # return text string
        return text

# User Interface class
class UserInterface:
    # constructor
    def __init__(self):
        # initialize text
        text = "Hello"
        # create list and initialize it with text string above
        self.list = DoublyLinkedList(text=text)
        # start position from head
        self.position = DoublyLinkedList.Position(self.list.head)

    # interact with user on how to proceed
    def proceed(self, position):
        # print information
        print("Current text:\n", self.list.text())
        cursorData = ''
        if position.element() is None:
            cursorData = None
        else:
            cursorData = position.element().data
        print("Cursor at:\n", cursorData)

        # print action choosing information
        print("Choose action:")
        print("\tMove cursor left: L")
        print("\tMove cursor right: R")
        print("\tInsert at cursor: I")
        print("\tDelete at cursor: D")
        print("\tClose app: C")

        # choose action
        action = input()
        # if "move cursor left" action
        if action == 'L':
            position = self.list.moveLeft(position)
        # if "move cursor right" action
        elif action == 'R':
            position = self.list.moveRight(position)
        # if insert action
        elif action == 'I':
            # specify the character to input
            char = input("Enter character to insert: ")
            position = self.list.insert(position, char)
        # if delete action
        elif action == 'D':
            position = self.list.delete(position)
        # if close terminal action
        # base case
        elif action == 'C':
            # return
            return

        # tail-recursive call
        self.proceed(position=position)

# Driver Code
if __name__ == '__main__':
    # create user interface
    userInterface = UserInterface()
    # start proceed method and interact with user
    userInterface.proceed(userInterface.position)