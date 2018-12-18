## the purpose of this program is to test the binary search tree class

# imports
from binarySearchTree import BinarySearchTree
from binaryTree import BinaryTree

BST = BinarySearchTree()

print("BST empty Test:")
print("The BST is", BST)
print("The max value is", BST.maxValue())
print("The min value is", BST.minValue())
print("Is it a BST?", BST.isBST())
print("retrieve test:", BST.retrieve(5))
print()

print("filling test:")
BST.insert(20)
print("The BST is", BST)
print("The max value is", BST.maxValue())
print("The min value is", BST.minValue())
print("Is it a BST?", BST.isBST())
BST.insert(34)
BST.insert(5)
BST.insert(6)
BST.insert(33)
BST.insert(90)
print("The BST is", BST)
print("The max value is", BST.maxValue())
print("The min value is", BST.minValue())
print("Is it a BST?", BST.isBST())

print("retrieve tests:")
print("retrieve 20", BST.retrieve(20))
print("retrieve 90", BST.retrieve(90))
print("retrieve 44", BST.retrieve(44))
print("retrieve 5", BST.retrieve(5))
print()