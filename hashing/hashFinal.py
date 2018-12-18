"""
Author: Steven Lawrence
Date: 6/14/17
Assignment: 4
Purpose: Create a hash table that uses chaining to resolve collisions and a hash table that uses linear probing to
         solve collisions.
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
        # set the size
        if (size is None):
            self.__size = 151

        else:
            self.__size = size
        
        # make the table
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
        Retrieves a value within the has table.
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

############LINEAR PROBING##################

class HashTableProbing(object):
    """Linear probing hash table class"""

    def __init__(self, size=None, skip=None):
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
            self.__skip = 2

            # if the size is divisible by the skip and the skip is less than half the size increment it
            while self.__size % self.__skip == 0 and self.__skip <= self.__size // 2:
                self.__skip += 1

            # if None of the values in range(2, (self.__size // 2) + 1) work then set the skip to 1
            if self.__skip == (self.__size // 2) + 1:
                self.__skip = 1

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

        else:  # it is an integer
            return value % self.__size

    def put(self, value):
        """
        Inserts a value into the hash table.
           value - what is being inserted into
        """
        # initialize variables
        slot = self.hash(value)  # initial bucket
        originalSlot = slot


        # skip until it finds an empty bucket
        while self.__buckets[slot] is not None:
            slot = (slot + self.__skip) % self.__size

            # if all the buckets are full then exit
            if slot == originalSlot:
                # print("Table is Full")
                return

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
        originalSlot = slot

        # search the the table for the value
        while self.__buckets[slot] != value:
            slot = (slot + self.__skip) % self.__size

            # if the value is not in the table return None
            if slot == originalSlot:
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