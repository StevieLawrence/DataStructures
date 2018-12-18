"""
Author: Steven Lawrence
Date: 6/12/17
Purpose: Create a minHeap class
"""

class minHeap(object):
    """minHeap class"""
    def __init__(self):
        """
        Create a minimum heap which is a binary tree with the root values being less than the children.  Heaps increase
        left to right across a level before a new level is filled.
        """
        self.__theHeap = [None]
        self.__size = 0

    def getSize(self):
        return self.__size

    def getValue(self, x):
        """
        Returns the payload of a node in the heap given its position. If the position does not exists then return None
           x - position within the heap
        """
        if (x > 0 and x <= self.getSize()):
            return self.__theHeap[x]
        else:
            return None

    def setValue(self, x, value):
        """
        Sets the payload of a positional node within the heap.
            x - position within the heap
            value - new payload
        """
        if (x > 0 and x <= self.getSize()):
            self.__theHeap[x] = value

    def getParent(self, x):
        """
        Gets the parental node of the node at position x if it is a valid position. if the position is one then return
        None.
           x - the position of the within the heap
           return - the parental position of the node x if it is greater than zero and None elsewise.
        """
        if (x is not None and x > 1):
            return x // 2
        else:
            return None

    def getLeftChild(self, x):
        """
        Get the left child of position x.
           x - the position of the heap
           return - the position of the left child
        """
        # check if x is a valid position
        if (x is not None and (2 * x) <= self.getSize()):
            return 2 * x
        else:
            return None

    def getRightChild(self, x):
        """
        Get the right child of position x.
           x - the position of the heap
           return - the position of the right child
        """
        # check if x is a valid position
        if (x is not None and (2 * x) + 1 <= self.getSize()):
            return (2 * x) + 1
        else:
            return None

    def isEmpty(self):
        """ Checks if it is an empty heap; Returns a boolean value"""
        if self.getSize() == 0:
            return True
        else:
            return False

    def swap(self, x, y):
        """
        Swaps the payloads of two positions within the heap if both positions refer to valid heaps.
           x - one position
           y - another position
        """
        if ( x is not None and x >= 1 and x <= self.getSize() and y is not None and y >=1 and y <= self.getSize()):
            temp = self.getValue(x)
            self.setValue(x, self.getValue(y))
            self.setValue(y, temp)

    def percolateUp(self, x):
        """
        Continously swap position x with its parent and its parent's parent... until the payload is smaller than the children.
           x - position within the heap
        """
        # initialize parent
        parent = self.getParent(x)
        
        # if parent is none then it can't go back any farther 
        while (parent is not None):
            
            # if the value of the child is less than the parent then swap them
            if (self.getValue(parent) > self.getValue(x)):
                self.swap(parent, x)
                x = parent
                parent = self.getParent(x)
            else:
                parent = None # exit the loop

    def percolateDn(self, x):
        """
            Continously swap position x with its parent and its parents parent... until the payload is smaller than the children.
               x - position within the heap
            """
        # initialize the children variables
        lChild = self.getLeftChild(x)
        rChild = self.getRightChild(x)
        
        # left child is filled before right child; if left child is None then its a leaf
        while (lChild is not None):
            
            # Go left if there is no right child or if the left child is smaller than the right child
            if (rChild is None or (self.getValue(lChild) < self.getValue(rChild))):
                
                # if the parent value is greater than the left child then swap them
                if (self.getValue(x) > self.getValue(lChild)):
                    self.swap(x, lChild)
                    x = lChild
                    
                else: # exit the loop
                    x = None 

            else: # Go right; rChild is not None and rChild <= lChild
                
                # swap the parent and the right child if the parent is greater than it
                if (self.getValue(x) > self.getValue(rChild)):
                    self.swap(x, rChild)
                    x = rChild
                    
                else: # exit the loop
                    x = None 

            # reset lChild and rChild
            lChild = self.getLeftChild(x)
            rChild = self.getRightChild(x)

    def put(self, value):
        """
        insert a value into the heap
           value - the payload of the new node
        """
        self.__size += 1 # increment the size
        self.__theHeap.append(value) # add the value to the heap
        self.percolateUp(self.getSize()) #percolate up from the newly added position

    def deleteMin(self):
        """
        return the value of the root or minimum value.  The root is the replaces with the last leaf of the heap and is
        percolated down until it is a valid heap.
        """
        # check if it is an empty heap
        if self.isEmpty():
            return None
        
        else: 
            value = self.getValue(1) # store the minimum value
            self.swap(1, self.getSize()) # swap it with the last position
            self.__theHeap.pop() # delete it
            self.__size -= 1 # decrement the size
            self.percolateDn(1) # re-structure the heap
            return value

    def __str__(self):
        """
        Make the heap object printable
           return - a string representation of the heap
        """
        if self.isEmpty():
            return "Empty"
        else:
            return str(self.__theHeap[1:])
        
    def heapify(self, aList):
        """
        This program accpets a random list and turns it into a heap. Inorder to
        do that it adds the elements to the heap.  It then finds the last parent
        in the list (parent of the size).  From there it percolates down that 
        position and then moves up a position to the next parent and percolates
        down from there.  It continues this all the way up until it hits the roof.
        The complexity is O(log N).
           aList - a list of random elements
        """
        # add the list to the list in the heap
        self.__theHeap += aList
        
        # calculate the new size
        self.__size += len(aList)
        
        # get the the parent of the size and then count down from that position
        # to zero (exlusive)
        for i in range(self.getParent(self.getSize()), 0, -1):
            self.percolateDn(i)
