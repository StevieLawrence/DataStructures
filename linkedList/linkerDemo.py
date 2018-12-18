## This program tests the linkList class

# import
from singleLinkedList import myList

# create a linked list
daList = myList()

print("\nfind() Tests:")
print("find(0) on an empty:", daList.find(0))
print("Len of list is:", len(daList))
print()
print("Insert Data into an Empty List")
daList.insert(0, 20)
print("The list looks like this now:", daList)
print("find(0) test now:", daList.find(0))
print("Len of list is:", len(daList))

for i in range(5):
    daList.insert(0, i * i)
print("inserting some more gives:", daList)
print("find(2) is a node:", daList.find(2))
print("find(100) is out of range:", daList.find(100))
print()

print("Append and Prepend Test:")
daList.append(3)
daList.prepend(3)
print("appending and prepending 3:", daList)
print("Len of list is:", len(daList))
print()

print("Getitem and setitem Tests:")
print("payload at index of 0 is:", daList[0])
print("payload at index of 4 is:", daList[4])
daList[0] = 5
print("set index of 0 to 5:", daList)
print("payload at index of 0 is:", daList[0])
print()

print("Pop Test:")
print(daList)
item1 = daList.pop(2)
print("The list after removing index of 2:", daList)
print("The popped item is:", item1)
item2 = daList.pop()
print("The list after poping the end:", daList)
print("The popped item is:", item2)
item3 = daList.pop(1000)
print("Popping at index of 1000:", daList)
print("The popped item is:", item3)
print()
