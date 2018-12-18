## This program tests the linkList class

# import
from doubleLinkedList import doubleList

# create a linked list
dList = doubleList()

print("\nfind() Tests:")
print("find(0) on an empty:", dList.find(0))
print("Len of list is:", len(dList))
print()
print("Insert Data into an Empty List")
dList.insert(0, 20)
print("The list looks like this now:", dList)
print("find(0) test now:", dList.find(0))
print("Len of list is:", len(dList))

for i in range(5):
    dList.insert(0, i * i)
print("inserting some more gives:", dList)
print("find(2) is a node:", dList.find(2))
print("find(100) is out of range:", dList.find(100))
print()

print("Append and Prepend Test:")
dList.append(3)
dList.prepend(3)
print("appending and prepending 3:", dList)
print("Len of list is:", len(dList))
print()

print("Getitem and setitem Tests:")
print("payload at index of 0 is:", dList[0])
print("payload at index of 4 is:", dList[4])
dList[0] = 5
print("set index of 0 to 5:", dList)
print("payload at index of 0 is:", dList[0])
print()

print("Pop Test:")
print(dList)
item1 = dList.pop(2)
print("The list after removing index of 2:", dList)
print("The popped item is:", item1)
item2 = dList.pop()
print("The list after poping the end:", dList)
print("The popped item is:", item2)
item3 = dList.pop(1000)
print("Popping at index of 1000:", dList)
print("The popped item is:", item3)
print()
