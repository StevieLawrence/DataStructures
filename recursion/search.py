"""
Author: Steven Lawrence
Date: 5/31/17
Purpose: This program tests recursion to find a value in a list
"""

# imports
import random

def main():
    N = 100
    myList = [random.randint(-100, 100) for i in range(N)]

    print(myList)
    print(mySearch(myList, 2))
    if 2 in myList:
        print(myList.index(2))
    else:
        print(None)


def mySearch(mylist, value):
    """
    Uses recursion to find a value in the list by splitting the list into halves
       mylist - list
       value - the value we are searching for
       return - value
       Or - that the value is not in the list
    """
    if len(mylist) == 1:
        if value == mylist[0]:
            return 0
        else:
            return None

    else:
        a = mySearch(mylist[0:len(mylist) // 2], value)
        size = len(mylist[0:len(mylist) // 2])
        if a == None:
            b = mySearch(mylist[len(mylist) // 2 : ], value)
            if b == None:
                return b
            else:
                return b + size
        return a

# start the program
main()
