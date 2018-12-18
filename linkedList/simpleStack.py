"""
Author: Steven Lawrence
Date: 5/24/17
purpose - make a stack class
"""

class myStack:
    """stack class"""
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if (self.size() == 0):
            return None
        else:
            return self.__items.pop()

    def size(self):
        return len(self.__items)

    def peek(self):
        if (self.size() == 0):
            return None
        else:
            return self.__items[self.size() - 1]

    def isEmpty(self):
        return self.size() == 0