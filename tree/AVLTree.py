"""
Author: Steven Lawrence
Date: 6/7/17
Purpose: creat an AVL Tree
"""

# imports
from binarySearchTree import BinarySearchTree


class AVLTree(BinarySearchTree):
    """AVL tree class"""
    def __init__(self, data=None, leftChild=None, rightChild=None):
        """
        Create an AVL tree, which is a binary search tree that has a height component.
        An empty tree has a height of -1. A leaf node has a height of zero, and
        the height of any other node is one more than the max of the heights of
        its two children.
           data - the data being stored as the payload
           leftChild - left child of the tree
           rightChild - right child of the tree
        """
        # call the super constructor
        BinarySearchTree.__init__(self, data, leftChild, rightChild)
        
        # a new AVL tree will either have a height of -1 or zero depending on if 
        # it is empty or not.
        if data == None:
            self.__height = -1
        else:
            self.__height = 0

    def setData(self, d):
        """
        Overload the setData() function to call the original setData of the binary
        tree.  Also if the height of the tree is less than zero (empty trees have
        a height of -1), then set the height equal to zero.
           d - the data
        """
        # perform the super implementation
        BinarySearchTree.setData(self, d)

        # if it was an empty tree then update it to a leaf node (not necessary)
        if self.__height < 0:
            self.__height = 0

    def getHeight(self):
        return self.__height

    def setHeight(self, h):
        self.__height = h

    def computeHeight(self):
        """
        Computes the height of an AVL tree. An empty tree has a height of -1. A
        leaf node has a height of zero, and the height of any other node is one
        more than the max of the heights of its two children.
        """
        # check if it is an empty tree
        if (self is None or self.isEmpty()):
            self.setHeight(-1)

        else:

            # determine the height of the left child
            if self.getLeftChild() is None:
                left = -1
            else:
                left = self.getLeftChild().getHeight()

            # determine the height of the right child
            if self.getRightChild() is None:
                right = -1      
            else:
                right = self.getRightChild().getHeight()
                
            # check if it is a leaf node
            if ((left == -1) and (right == -1)):
                self.setHeight(0)                 

            else:
                # else the height is the max height between the two children plus one
                self.setHeight(max(left, right) + 1)

    def balance(self):
        """
        Determines if the AVL tree is balanced. It is balanced if the absolute
        value of the difference in height of the left child and the right child
        is less than 2.
           return - a bolean value if it is balanced or not
        """
        # determine the height of the left child
        if self.getLeftChild() is None:
            left = -1
        else:
            left = self.getLeftChild().getHeight()
        
        # determine the height of the right child
        if self.getRightChild() is None:
            right = -1
        else:
            right = self.getRightChild().getHeight()
        
        # determine if the absolute of the difference is less than 2
        if abs(left - right) < 2:
            return True

        else:  # absolute difference is >= 2
            return False

    def rotateWithLeftChild(self):
        """
        Performs a left rotation.  In this rotation k2 (left child of the root)
        becomes the new root. B (the right child of k2) becomes the left child
        of k1 (the original root) replacing k2.  k1 then becomes the right child
        of k2 in the now vacant spot left by B.
        """
        k2 = self.getLeftChild()  # save k2 in a variable
        self.setLeftChild(k2.getRightChild())  # self is k1; set the left child to B
        k2.setRightChild(self)  # set k1 as k2's new right child

        # compute the new heights
        self.computeHeight()  # compute k1's height first since it is now lower than k2
        k2.computeHeight()

        # return k2 as it is now the new root; important for insert function
        return k2

    def rotateWithRightChild(self):
        """
        Performs a right rotation. In the right rotation k3 (right child of the root)
        becomes the new root. C (the left child of k3) becomes the right child
        of k1 (the original root) replacing k3.  k1 then becomes the left child
        of k3 in the now vacant spot left by C.
        """
        k3 = self.getRightChild()  # save k3 in a variable
        self.setRightChild(k3.getLeftChild())  # self is k1; set the right child to C
        k3.setLeftChild(self)  # set k1 as k3's new left child

        # compute the new heights
        self.computeHeight()  # compute k1's height first since it is now lower than k3
        k3.computeHeight()

        # return k3 as it is now the new root; important for insert function
        return k3

    def insert(self, data):
        """
        Insert a single AVL tree into the AVL tree by comparing the payloads and checking
        the heights of all the trees. If it is empty AVL tree then set the data
        which autimatically updates the height to zero. Else it moves down the tree
        comparing payloads and inserts itself at the correct location corresponding
        to a binary search tree. the heights are calculated along the way. If the
        there is an imbalance then it is rotated dependending on if it is located at
        position A, B, C, or D.
            data- the payload of the new AVL tree
        """
        # check if it is an empty tree
        if self.isEmpty():
            self.setData(data)
            return self

        # Compare the data to the payload
        elif (data < self.getData()):

            # if it is less than it then it goes on the left side
            if self.getLeftChild() is None:
                # if there is no left child insert the data
                self.setLeftChild(AVLTree(data))

                # compute the new height of the parent tree
                self.computeHeight()
                return self

            else:
                # continue moving down the tree, and keep in mind of possible rotations
                self.setLeftChild(self.getLeftChild().insert(data))
                self.computeHeight() # possible new grandpappy height

                # check if the tree is balanced
                if not self.balance():

                    # case 1: insert at position A
                    if data < self.getLeftChild().getData():
                        return self.rotateWithLeftChild()

                    else:  # case 2: insert at position B
                        # have to do two rotations; first a right rotation
                        # with k4 (right child of k2) and set k4 as the new
                        # left child of k1. B1 (left child of k4 is set as the new
                        # right child of k2 in place of k4 and k2 is the left child of k4.
                        self.setLeftChild(self.getLeftChild().rotateWithRightChild())

                        # next do a left rotation setting k4 as the new root,
                        # k1 as the right child of k4, and B2 (right child of
                        # k4) as the new left child of k1.
                        return self.rotateWithLeftChild()

                else: # it is balanced
                    return self

        else:  # data >= self.getData()

            # if it is greater than or equal then it goes on the right side
            if self.getRightChild() is None:
                # if no right child insert the data
                self.setRightChild(AVLTree(data))

                # compute the new height of the now parent tree
                self.computeHeight()
                return self

            else:
                # continue moving down the tree, and keep in mind of possible rotations
                self.setRightChild(self.getRightChild().insert(data))
                self.computeHeight() # compute height of the grandpappy

                # check if the tree is balanced
                if not self.balance():

                    # case 4: insert at position D
                    if data >= self.getRightChild().getData():
                        return self.rotateWithRightChild()

                    else:  # case 3: insert at position C
                        # have to do two rotations; first a left rotation
                        # with k5 (left child of k3) and set k5 as the new right
                        # child of k1 (self). C2 (right child of k5 is set as the new
                        # left child of k3 in place of k5 and k3 is the right child of k5.
                        self.setRightChild(self.getRightChild().rotateWithLeftChild())

                        # next do a right rotation setting k5 as the new root,
                        # k1 as the left child of k5, and C1 (left child of
                        # k5) as the new right child of k1.
                        return self.rotateWithRightChild()

                else: # it is balanced
                    return self

    def isAVLTree(self):
        """
        Check if it is an AVL tree. If the tree is balanced, it is also a valid
        binary search tree, and its right and left sub trees are also valid AVL
        trees then it is an AVL tree.
           return - Boolean value
        """
        # check if it is an empty tree
        if self.isEmpty():
            return True

        else:
            # check if it is a valid binary search tree and that it is balanced
            if (not self.isBST()) or (not self.balance()):
                return False

            # If a left child exists check if it is a valid AVL tree
            elif (self.getLeftChild() is not None) and (not self.getLeftChild().isAVLTree()):
                return False

            # if a right child exists check if it is a valid AVL tree
            elif (self.getRightChild() is not None) and (not self.getRightChild().isAVLTree()):
                return False

            else:  # if everthing checks out then it is a valid AVL tree
                return True

    def inOrderTraversal(self):
        """
        Overload the binary tree inOrderTraversal() to be the same but include
        the height of the tree in parenthesis following the data.
           return - a string of the in-order traversal with the heights of each
                    tree included in parenthesis
        """
        if (self.isEmpty()):
            return "Empty"
        else:
            result = " "
            # left subtree
            if (self.getLeftChild() is not None):
                result += self.getLeftChild().inOrderTraversal()

            # root
            result += " " + str(self.getData()) + "(" + str(self.__height) + ")"

            # right subtree
            if (self.getRightChild() is not None):
                result += " " + self.getRightChild().inOrderTraversal()

            return result.strip()
