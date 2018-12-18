"""
Author: Steven Lawrence
Date: 5/31/17
Purpose: This program tests recursion to find the summation value of a list
"""

# imports
import random

def main():
    N = 100
    myList = [random.randint(-500, 500) for i in range(N)]

    print(myList)
    print(mySum(myList))
    print(sum(myList))

def mySum(mylist):
    """
    Uses recursion to find the summation of all the terms in the list by splitting the list into halves
       mylist - list
       return - summation value of the list
    """
    if len(mylist) == 1:
        return mylist[0]
    else:
        a = mySum(mylist[0:len(mylist) // 2])
        b = mySum(mylist[len(mylist) // 2 : ])
        return a + b

# start the program
main()