"""
Author: Steven Lawrence
Date: 5/25/17
Description: code for a singly linked list
"""

class listNode:
    """Node class"""
    def __init__(self, data, next = None):
        """
        Create a link list
            data - data in the list
            next - pointer to the next node in the link list, defaults to None
        """
        self.__data = data
        self.__next = next

    def getData(self):
        """Returns data"""
        return self.__data

    def setData(self, data):
        """Sets data"""
        self.__data = data

    def getNext(self):
        """Returns next node"""
        return self.__next

    def setNext(self, next):
        """Sets next node"""
        self.__next = next

class myList:
    """Implements a link list"""
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def insert(self, i, x):
        """inserts x into the list at position i"""
        # list is empty, i doesn't matter
        if (self.isEmpty()):
            self.__head = listNode(x)
            self.__tail = self.__head

        #inserting before the head
        elif ( i <= 0) :
            self.__head = listNode(x, self.__head)

        # inserting after the tail
        elif (i >= self.size()):
            self.__tail.setNext(listNode(x))
            self.__tail = self.__tail.getNext()

        # inserting somplace in between
        else:
            # We need to stop at the node previous to i to make
            # it point around the ith one.             
            previous = self.find(i - 1)
            previous.setNext(listNode(x, previous.getNext()))
            if (self.__tail == previous):
                self.__tail = self.__tail.getNext()
        self.__size += 1

    def size(self):
        # By keeping track of the size as we go, we don't have to
        # count the number of nodes, which would be O(N).
        return self.__size

    def isEmpty(self):
        # could also do return self.__size == 0 instead
        return self.__head == None

    def __str__(self):
        """ Returns a string of the values in the list"""
        result = ""
        current = self.__head
        while(current != None) :
            result = result + " " + str(current.getData())
            current = current.getNext()
        return result

    def find(self, i):
        """
        Finds the ith node starting from zero
           i- index position
        """
        # determine if the index is not in range; index starts at 0
        range = (0 <= i) and (i < self.size())
        if self.isEmpty() or not range:
            return "index out of range"
        else:
            # index is within range
            current = self.__head
            count = 0
            while (current != None and count < i):
                count += 1
                current = current.getNext()
            return current

    def append(self, x):
        """
        Add item to the tail of the link list
           x - data being added to the end
        """
        self.insert(self.size(), x)

    def prepend(self, x):
        """
        Add item to the begining of the link list
           x - data being added to the front
        """
        self.insert(0, x)

    def __len__(self):
        """Returns the size of the linked list"""
        return self.__size

    def __getitem__(self, i):
        """
        Gets the payload of the ith node
           i - index position
           return - data stored in the ith node
        """
        node = self.find(i)
        return node.getData()

    def __setitem__(self, i, x):
        """
            Gets the payload of the ith node
               i - index position
               x - data to set for the node
            """
        node = self.find(i)
        node.setData(x)
    
    def front(self):
        """Returns the head"""
        return self.__head.getData()
    
    def back(self):
        """Returns the tail"""
        return self.__tail.getData()    

    def pop(self, i = None):
        """
        Removes and returns the ith node
           i - index position, defaults to None if no position given
        """
        # check if the list is empty
        if (self.isEmpty()):
            return None
        else:
            # check if i is None or index is greater than the size
            if (i == None or i >= self.size()):
                i = self.size() - 1
            # case where we are removing the head
            if (i == 0):
                x = self.__head.getData()
                self.__head = self.__head.getNext()
                self.__size -= 1
                if (self.__head == None):
                    self.__tail = None
                return x
            else:
                # case where we are removing a node between the head and tail
                previous = self.find(i - 1)
                x = previous.getNext().getData()
                previous.setNext(previous.getNext().getNext())
                self.__size -= 1
                if (previous.getNext() == None):
                    self.__tail = previous
                return x
    
    def search(self, value):
        """
        Retrieves a value from the linked list
           value - value we are searching for
           return - the payload of the value if it matches else return None
        """
        current = self.__head
        while(current is not None and current.getData() != value):
            current = current.getNext()

        # If its not in the linked list return None
        if (current is None):
            return None

        else: # return the payload
            return current.getData()    
