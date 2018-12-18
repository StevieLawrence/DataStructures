"""
Author: Steven Lawrence
Date: 6/13/17
Purpose: Create a hash table that uses linear probing to solve collisions
"""

# imports
from SingleLinkedList import myList
from Student import Student

class HashTableProbing(object):
    """Linear probing hash table class"""
    def __init__(self, size = None, skip = None):
        """
        Create a hash table with buckets of a certain size.
           size - the number of buckets in the table, defaults to 151
           skip - the number fo buckets being skipped if that bucket is full
        """
        # Set the size
        if (size is None):
            self.__size = 151

        else:
            self.__size = size
        
        # Set the skip
        if (skip is None):
            self.__skip = 3
        
        else:
            self.__skip = skip
        
        # create the buckets
        self.__buckets = [None] * self.__size

    def hash(self, value):
        """
        Codes the values into the hash table
           value - value being entered into the table
           return - the bucket number in the hash table
        """
       # check if it is a None type
        if (value is None):
            return None

        elif type(value) is Student:
            return value.getId() % self.__size

        else: # it is an integer
            return value % self.__size

    def put(self, value):
        """
        Inserts a value into the hash table.
           value - what is being inserted into
        """
        # initialize variables
        slot = self.hash(value) # initial bucket
        numberOfSkips = 0
        
        # skip until find an empty bucket
        while self.__buckets[slot] is not None:
            slot = (slot + self.__skip) % self.__size
            numberOfSkips += 1
            
            # if all the buckets are full then exit
            if numberOfSkips == self.__size:
                # print("Table is Full")
                break
       
       # enter value into the empty bucket
        self.__buckets[slot] = value 

    def retrieve(self, value):
        """
        Retrieves a value within the hash table.
           value - the value being retrieved.
           return - the value or None if its not in there
        """
        # initialize variables
        slot = self.hash(value)
        numberOfSkips = 0
        
        # search the the table for the value
        while self.__buckets[slot] != value:
            slot = (slot + self.__skip) % self.__size
            numberOfSkips += 1
            
            # if the value is not in the table return None
            if numberOfSkips == self.__size:
                return None
        
        return self.__buckets[slot]

    def __str__(self):
        """
        Make the hash table printable
           return - a string representation of the hash table
        """
        result = ""
        for i in range(self.__size):
            result += "bucket" + str(i) + ": " + str(self.__buckets[i]) + "\n"
        return result
