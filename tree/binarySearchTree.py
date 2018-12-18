"""
Author: Steven Lawrence
Date: 6/6/17
Purpose: To make a binary search tree class
"""

# imports
from binaryTree import BinaryTree

class BinarySearchTree(BinaryTree):
    """binary search tree class"""
    def __init__(self, d = None, leftChild = None, rightChild = None):
        """
        Create a binary search tree. A binary search tree is a binary tree where 
        all of the values on the left of the root are smaller and all of
        the values to the right of the root are larger.
           d - data or payload
           leftChild- left child of binary tree
           rightChild - right child of binary tree
        """
        # call the super constructor
        BinaryTree.__init__(self, d, leftChild, rightChild)

    def maxValue(self):
        """
        The right most value of a BST is the maximum value, so just keep going down the right side until you hit the max.
           return - the payload of the BST containing the max value.
        """
        # check if it is an empty tree
        if self.isEmpty():
            return None

        # if there is no right child then return the current BST's data
        elif (self.getRightChild() is None):
            return self.getData()

        else:
            # return the max value of the right subtree
            return (self.getRightChild().maxValue())

    def minValue(self):
        """
        The left most value of a BST is the minimum value, so go down the left side until you hit the minimum.
           return - the payload of the BST containing the minimum value.
        """
        # check if it is an empty tree
        if self.isEmpty():
            return None

        # if there is no left child then return the current BST's data
        elif (self.getLeftChild() is None):
            return self.getData()

        else:
            # return the minimum value of the left subtree
            return (self.getLeftChild().minValue())

    def isBST(self):
        """
        Check if it is a binary search tree. If the maximum value of the left subtree is less than the root and the
        minimum value of the right subtree is greater than the root then it is a binary search tree.
           return - Boolean value on if it is a binary search tree or not
        """
        # check if it is an empty tree
        if self.isEmpty():
            return True

        else:
            # if There is a left child and it is not a binary search tree or the max value of the left child subtree is
            # greater than or equal to the root then return that it is not a binary search tree.
            if (self.getLeftChild() is not None) and ((not self.getLeftChild().isBST()) or (self.getLeftChild().maxValue() >= self.getData())):
                return False

            # else if there exists a right child that is not a binary search tree or the minimum value of the right child subtree is
            # less than the root then return that it is not a binary search tree.
            elif (self.getRightChild() is not None) and ((not self.getRightChild().isBST()) or (self.getRightChild().minValue() < self.getData())):
                return False

            else:
                # otherwise it is a binary search tree
                return True

    def insert(self, data):
        """
        Insert a single binary search Tree into the binarySearchTree object by comparing the payloads. If it is empty binary
        search tree then just set the data. Otherwise the comparison test will move down the binary search tree until
        it finds its correct position and inserts the data as the correct child.
           data - the payload of the new binary search tree
        """
        # check if it is an empty tree
        if self.isEmpty():
            self.setData(data)

        # Compare the data to the payload; if it is less than the root it goes on the left side
        elif (data < self.getData()):
            
                # if no left child exists then set the data as a BST and left child
                if self.getLeftChild() is None:
                    self.setLeftChild(BinarySearchTree(data))
                else:
                    # insert into the left subtree
                    self.getLeftChild().insert(data)

        else: # if its greater than or equal then it goes on the right side
            
            # if no right child exists set the data as a BST and right child
            if self.getRightChild() is None:
                self.setRightChild(BinarySearchTree(data))
            else:
                # else insert it into the right subtree
                self.getRightChild().insert(data)

    def retrieve(self, data):
        """
        Retrieve the payload of a binary search tree by comparing the payload with the data and moving down the tree
        until it is found or if is determined that it is not in the binary search tree. If it is an empty binary
        search tree then return None.
           data - the payload we are searching for within the tree
           return - None if the data is not within the tree or the payload of the binary search tree if it is in it.
        """
        # check if it is an empty tree
        if self.isEmpty():
            return None

        # if the binary search tree payload is equal to the data then return the payload
        if self.getData() == data:
            return self.getData()

        else:
            
            # Compare the data to the payload; if it is less than then check the left subtree
            if (data < self.getData()):
                
                # if it reaches the end then return None
                if self.getLeftChild() is None:
                    return None
                
                else:
                    # recursive step
                    return self.getLeftChild().retrieve(data)
                
            else: # if its greater than or equal to then check the right side
                
                # return none if it is not in the tree
                if self.getRightChild() is None:
                    return None
                
                else:
                    # recursive step
                    return self.getRightChild().retrieve(data)