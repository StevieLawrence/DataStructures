"""
Author: Steven Lawrence
Date: 5/24/17
purpose - make a queue class
"""

# import a linked list class
from singleLinkedList import myList

class myQueue:
    """Queue class"""
    def __init__(self):
        """
        Create a queue using a python list
        """
        self.__items = myList()

    def enqueue(self, item):
        self.__items.append(item)

    def dequeue(self):
        if (self.size() == 0):
            return None
        else:
            return self.__items.pop(0)

    def size(self):
        return len(self.__items)

    def peek(self):
        if (self.size() == 0):
            return None
        else:
            return self.__items[0]

    def isEmpty(self):
        return self.size() == 0
