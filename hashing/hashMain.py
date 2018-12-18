## the purpose of this program is to test the HashTableChaining class

# imports
from HashTableChaining import HashTableChaining
import random

# declaration of constants
ADDED_VALUES = 100
VALUE_RANGE = 500

# initialize a hashTable
hTable = HashTableChaining(37)

# Empty Hash table tests
print("Empty Hash Table Tests")
print(hTable)
print("retrieve:", hTable.retrieve(5))
print("is hTable a HashingTableChaining object? ", type(hTable) is HashTableChaining)
print()

# add values to the table
for i in range(ADDED_VALUES):
    num = random.randint(-VALUE_RANGE, VALUE_RANGE)
    hTable.put(num)

# now print it
print("filled Hash Table")
print(hTable)

# now test retrieve
for i in range(ADDED_VALUES):
    num = random.randint(-VALUE_RANGE, VALUE_RANGE)
    print("search for " + str(num) + " results in: " + str(hTable.retrieve(num)))