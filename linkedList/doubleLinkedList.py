"""
Author: Steven Lawrence
Date: 5/25/17
Description: code for a doublyk linked list
"""

class listNode:
    """Node class"""
    def __init__(self, data, next = None, previous = None):
        """
        Create a link list
            data - data in the list
            next - pointer to the next node in the link list, defaults to None
        """
        self.__data = data
        self.__next = next
        self.__previous = previous

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
        
    def getPrevious(self):
        """Returns the previous node"""
        return self.__previous
    
    def setPrevious(self, prev):
        """Sets previous node"""
        self.__previous = prev

class doubleList:
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
            # new: set the former heads previous from None to the new head
            self.__head.getNext().setPrevious(self.__head) 

        # inserting after the tail
        elif (i >= self.size()):
            # new: set the tails next to a new node that has None for its next and
            # the previous tail for its previous.
            self.__tail.setNext(listNode(x, None, self.__tail))
            self.__tail = self.__tail.getNext()

        # inserting somplace in between
        else:
            # We need to stop at the node previous to i to make
            # it point to the new node. New: Then fix all of the nexts and previous
            # the previus node, current node, and new node.
            previous = self.find(i - 1)
            newNode = listNode(x, previous.getNext(), previous)
            newNode.getNext().setPrevious(newNode)
            
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
        # determine if the index is not in range; index starts at zero
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
        
        # new: check if i is None or index is greater than the size; here we are popping
        # off the end
        elif (i == None or i >= self.size()):
            x = self.__tail.getData()
            self.__tail = self.__tail.getPrevious()
            self.__size -= 1
            
            # the case where we only have one node in the list
            if (self.__tail == None):
                self.__head = None 
                
            else:
                # new: if its not None then set the tails's next to None
                self.__tail.setNext(None)
            
            return x            
      
        # case where we are removing the head
        elif (i == 0):
            x = self.__head.getData()
            self.__head = self.__head.getNext()
            self.__size -= 1
                
            # the case where we only have one node in the list
            if (self.__head == None):
                self.__tail = None
            else:
                # new: if its not None then set the head's previous to None
                self.__head.setPrevious(None)
                
            return x
            
        else:
            # case where we are removing a node between the head and tail
            previous = self.find(i - 1)
            x = previous.getNext().getData()
            previous.setNext(previous.getNext().getNext())
            self.__size -= 1
            # the case where we are popping off the tail
            if (previous.getNext() == None):
                self.__tail = previous
            else:
                # new: set the new next terms previous to the previous
                previous.getNext().setPrevious(previous)                    
                    
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
