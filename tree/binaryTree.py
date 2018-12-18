"""
Author: Steven Lawrence
Date: 6/5/17
lab:09
purpose: Create a binary tree class
"""

class BinaryTree:
    """ binary tree class"""
    def __init__(self, data = None, leftChild = None, rightChild = None):
        """
        Create a binary tree that contains:
           data - the data being stored as the payload
           leftChild - left child of the tree
           rightChild - right child of the tree
        """
        self.__data = data
        self.__leftChild = leftChild
        self.__rightChild = rightChild

    def getData(self):
        return self.__data

    def setData(self, d):
        self.__data = d

    def getLeftChild(self):
        return self.__leftChild

    def setLeftChild(self, leftChild):
        self.__leftChild = leftChild

    def getRightChild(self):
        return self.__rightChild

    def setRightChild(self, rChild):
        self.__rightChild = rChild

    def isEmpty(self):
        """Determines if it is an empty tree"""
        if (self is None or self.__data is None):
            return True
        else:
            return False
        
    def __str__(self):
        return self.inOrderTraversal()

    def inOrderTraversal(self):
        """
        Traverses the binary tree in order of left subtree, root, and then the right subtree
           return - a string with the data ordered by in-order traversal
        """
        if (self.isEmpty()):
            return "Empty"
        else:
            result = " "
            # left subtree
            if (self.getLeftChild() is not None):
                result += BinaryTree.inOrderTraversal(self.getLeftChild())

            # root
            result += " " + str(self.getData())

            # right subtree
            if (self.getRightChild() is not None):
                result += " " + BinaryTree.inOrderTraversal(self.getRightChild())

            return result.strip()

    def preOrderTraversal(self):
        """
        Traverses the binary tree in order of root, left subtree, and then the right subtree
           return - a string with the data ordered by pre-order traversal
        """
        if (self.isEmpty()):
            return"Empty"
        else:
            result = " "
            # root
            result += str(self.getData())

            # left subtree
            if (self.getLeftChild() is not None):
                result +=  BinaryTree.preOrderTraversal(self.getLeftChild())

            # right subtree
            if (self.getRightChild() is not None):
                result += BinaryTree.preOrderTraversal(self.getRightChild())

            return result

    def postOrderTraversal(self):
        """
        Traverses the binary tree in order of left subtree, right subtree, and then the root
            return - a string with the data ordered by post-order traversal
        """
        if (self.isEmpty()):
            return "Empty"
        else:
            result = " "
            # left subtree
            if (self.getLeftChild() is not None):
                result += BinaryTree.postOrderTraversal(self.getLeftChild())

            # right subtree
            if (self.getRightChild() is not None):
                result += " " + BinaryTree.postOrderTraversal(self.getRightChild())

            # root
            result += " " + str(self.getData())

            return result.strip()