"""
Author: Steven Lawrence
Date: 5/31/17
Purpose: This program tests recursion to find the minimum value on a list
"""

# imports
import random

def main():
    N = 100
    myList = [random.randint(-500, 500) for i in range(N)]

    print(myList)
    print(myMin(myList))
    print(min(myList))

def myMin(mylist):
    """
    Uses recursion to find the minimum by splitting the list into halves
       mylist - list
       return - minimum value in the list
    """
    if len(mylist) == 1:
        return mylist[0]
    else:
        a = myMin(mylist[0:len(mylist) // 2])
        b = myMin(mylist[len(mylist) // 2 : ])
        return min(a, b)

# start the program
main()
