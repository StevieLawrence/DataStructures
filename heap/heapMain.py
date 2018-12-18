## the purpose of this program is to test the minHeap class

# imports
from heap import minHeap
import random

# declaration of constants
ADDED_VALUES = 20
VALUE_RANGE = 200

# initialize a heap
lilHeap = minHeap()

# Test the getSize(), isEmpty(), and __str__ functions
print("Empty Heap Tests:")
print("the size is", lilHeap.getSize())
print("isEmpty() gives", lilHeap.isEmpty())
print("printing the heap gives:", lilHeap)
print()

# add 20 random values to the heap
for i in range(ADDED_VALUES):
    num = random.randint(-VALUE_RANGE, VALUE_RANGE)
    lilHeap.put(num)

# Test the getSize(), isEmpty(), and __str__ functions
print("Filled Heap Tests:")
print("the size is", lilHeap.getSize())
print("isEmpty() gives", lilHeap.isEmpty())
print("printing the heap gives:", lilHeap)
print()

# Remove and print the minimum values until the heap is empty
print("deleteMin() Test:")
print("Starting with:", lilHeap)
while lilHeap.getSize() > 0:
    minValue = lilHeap.deleteMin()
    print("the heap:", lilHeap)
    print("the value:", minValue)
print()

# Test the getSize(), isEmpty(), and __str__ functions
print("Emptied Heap Tests:")
print("the size is", lilHeap.getSize())
print("isEmpty() gives", lilHeap.isEmpty())
print("printing the heap gives:", lilHeap)
print()

# Test the heapify functions
print("heapify Test:")
print("The heap is currently: ", lilHeap)

# create a randomlist
randList = []
for i in range(ADDED_VALUES):
    number = random.randint(-VALUE_RANGE, VALUE_RANGE)
    randList.append(number)

# heapify it
print("the list is: ", randList)
lilHeap.heapify(randList)
print("After heapify: ", lilHeap)