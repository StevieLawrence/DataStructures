"""
Author: Steven Lawrence
Date: 6/13/17
Purpose: Create a hash table that uses chaining with a linked list to solve collisions
"""

# imports
from SingleLinkedList import myList
from Student import Student

class HashTableChaining(object):
    """Chaining hash table class"""
    def __init__(self, size = None):
        """
        Create a hash table with buckets of a certain size.
           size - the number of buckets in the table, defaults to 151
        """
        if (size is None):
            self.__size = 151

        else:
            self.__size = size

        self.__buckets = []
        for i in range(self.__size):
            self.__buckets.append(myList())

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
        slot = self.hash(value) # hash the value
        self.__buckets[slot].append(value) # append it to that bucket

    def retrieve(self, value):
        """
        Retrieves a value within the hash table.
           value - the value being retrieved.
           return - the value or None if its not in there
        """
        slot = self.hash(value)
        return self.__buckets[slot].search(value)

    def __str__(self):
        """
        Make the hash table printable
           return - a string representation of the hash table
        """
        result = ""
        for i in range(self.__size):
            result += "bucket" + str(i) + ": " + str(self.__buckets[i].size()) + ": " + str(self.__buckets[i]) + "\n"
        return result
