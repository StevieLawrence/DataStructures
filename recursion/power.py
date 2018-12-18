"""
Author: Steven Lawrence
Date: 5/31/17
Purpose: This program tests recursion to caluculate a power
"""

# imports
import random

def main():
    num = random.randint(1, 10)
    base = random.randint(1,10)

    print("(base: %i, n: %i)" % (base, num))
    print(myPow(base, num))
    print(base ** num)

def myPow(x, n):
    """
    Uses recursion to find the summation of all the terms in the list by splitting the list into halves
       n - the exponent value
       x - base value
       return - x^n
    """
    if n == 1:
        return x

    else:
        pow = (myPow(x, (n//2)))
        if (n % 2) == 0:
            return pow * pow
        else:
            return x * pow * pow

# start the program
main()