## this program tests the binary search tree class

# imports
from binarySearchTree import BinarySearchTree
import random

# declaration of constants
NUMBER_OF_TIMES = 100
NUMBER_RANGE = 100

# initialize a binary search tree
BST = BinarySearchTree()

# insert 100 random numbers 
for i in range(NUMBER_OF_TIMES):
    num = random.randint(-NUMBER_RANGE, NUMBER_RANGE)
    BST.insert(num)

# print the binary search tree
print("Binary Search Tree:")
print(BST, "\n")

# search for 100 random numbers
for i in range(NUMBER_OF_TIMES):
    num = random.randint(-NUMBER_RANGE, NUMBER_RANGE)
    retrievedNum = BST.retrieve(num)
    print("number: %i retrieved: %s" % (num, retrievedNum))
    