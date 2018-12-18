"""
Author: Steven Lawrence
Date: 6/14/17 
Puropose: This program implements and tests the various sorting methods including:
Bubble sort, insertion sort, selection sort, heap sort, merge sort, and quick sort.
References:
https://www.toptal.com/developers/sorting-algorithms/
https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html
"""

import random
import time
from heap import minHeap

# initialize the size of the list
N = 10


''' This function will swap the values in the list at positions i and j
'''
def swap(a, i, j):
    """ Swap values of indecies i and j """
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

''' This function will copy the contents of one list to another. The
    purpose is so that we can sort the same list with different sorting
    algorithms.  So we will copy the original list into another before
    each sort.
'''

def copyList(a, b, N):
    """ Copies a list """
    for i in range(N):
        b.append(a[i])

''' This function will verify that the contents of a list are monotonically
    increasing in values.  In other words: sorted.
'''
def isListSorted(a):
    """
    Determines if a list is sorted or not
       a - the list
       return - a boolean on whether or not the list is sorted
    """
    N = len(a)
    for i in range(0,N-1):
        if a[i] > a[i+1]:
            return False

    return True



def bubbleSort(a):
    """
    The bubble sort corresponds with going through the list and swapping neighbors
    as need be N times. 
       a - the list
    """
    n = len(a) 
    for i in range(n):
        swapped = False # flag 
        
        # count down from the last index to the ith index
        for j in range(n - 1, i, -1):
            
            # swap neighbors as needed
            if a[j] < a[j - 1]:
                swap(a, j, j - 1)
                swapped = True # if a swap is performed then we are not done sorting
                
        # if we go through the entire list without swapping then the list is sorted
        if not swapped:
            break # exit out of the for loop
    return

def insertionSort(a):
    """
    Performs insertion sorting on a list. Starting from the begining of the list,
    the values are compared down the list until it is in its correct position. 
    Then we move to the next card and compare its value down the list until we find
    its position and so forth.
       a - the list
    """
    n = len(a)
    
    # don't need to start at the zero index because one card by itself is already sorted
    for i in range(1, n):
        k = i # decrementer
        
        # Move a value down the list until either we hit the begining or hit a
        # value that is smaller than the current value
        while (k > 0 and a[k] < a[k-1]):
            swap(a, k, k-1)
            k -= 1
        # a[0] to a[i] is sorted
    return


def mergeSort_rec(a, left, right):
    """
    Perform merge sorting using recursion. The list is continously split into 
    halves until it reaches down to the lowest levels of single sized lists,
    and pairs.  The pairs are sorted and then merged together to form 4's, then 8's, 
    ... to so be it for as many 2 * k times, where k = log2(N). After each merge
    the lists are sorted.
       a - the list
       left - the left most index
       right - the right most index
    """
    # check if the len(a) < 2
    if (right <= left):
        return
    
    # check if the list is a pair; if it is then sort it.
    if ((right - left) == 1):
        if (a[left] > a[right]):
            swap(a, left, right)
        return
    
    # otherwise:
    m = (left + right) // 2 # find the middle value in the list
    mergeSort_rec(a, left, m - 1) # call the mergeSort function on the first half of the list
    mergeSort_rec(a, m, right) # call mergeSort on the second half of the list
    
    # merge the two halves
    i = left # index starting from the left
    j = m # index starting from the middle term
    b = []
    
    # i is going to traverse the first half and j is going to do the same to the second half
    while (i < m and j < right + 1):
        
        # go down each half and add the terms from increasing order into list b
        if (a[i] <= a[j]):
            b.append(a[i])
            i += 1
        else:
            b.append(a[j])
            j += 1
            
    # if there exist terms in the first half bigger than all the values in the 
    # the second half then add them 
    while (i < m):
        b.append(a[i])
        i += 1

    # if there exist terms in the second half bigger than all the values in the 
    # the first half then add them     
    while (j < right + 1):
        b.append(a[j])
        j += 1

    # copy the ordered b back into the orginal list a
    j = 0
    for i in range (left, right + 1):
        a[i] = b[j]
        j += 1
    return


def mergeSort(a):
    """
    Calls the merge Sort recursive function.
       a - the list
    """
    mergeSort_rec(a, 0, len(a) - 1)

def quickSort_rec(a, left, right):
    """ Recursive process of the quickSort algorithm.  Basically the first term in
    the list is made the pivot value.  The list is then iterated over comapring their
    values to the value in the 0 index. An incrementer is used to determine if a 
    value is greater than the first term.  if it is then its value is swapped with
    the incremnter index's value.  Thus the final incrementer value will be the index
    at which all the values to the left of that index are smaller than the value in
    index zero.  Index zero is then swapped with that position and the process is 
    repeated by sorting the partions from the incrementer position.
       a - the list
       left - left most index
       right - right most index
    """
    #  check to make sure that the right most index is bigger than the left most index
    if (right <= left):
        return
    
    # choose a pivot; the pivot value is the first term in the list (a[0]), if thou wishes 
    # for a randomized pivot then swap the first term's value in the list with a random position's
    # value in the list and that value will be the new pivot
    # swap(a, left, random.randint(left, right)) 
    # Note: The above statement is commented. In this specific program the given 
    #       list is already randomized so this code is redundant (keep to look at later)
    
    # 2-way partition
    k = left
    # loop through the list and compare all the other values to the first term
    for i in range(left + 1, right + 1):
        if a[i] < a[left]:
            k += 1 # k is incremented everytime a value is found to be less than the first term
            swap(a, k, i) # all those values will be in positions left of k
        
    # swap the value in k with the pivot value at a[0]; this way all of the smaller values than the pivot are on its left
    # a new pivot is chosen as well.
    swap(a, left, k) 
    
    # recursive step
    quickSort_rec(a, left, k-1)
    quickSort_rec(a, k + 1, right)
    return


def quickSort(a):
    """ 
    Calls the recursive quickSort function.
       a - the list
    """
    quickSort_rec(a, 0, len(a) - 1)

def selectionSort(a):
    """
    The selection sort goes through the entire list and picks out the smallest
    value.  It then goes through the entire list and picks out the next smallest 
    value.  It continues this until the list is sorted.
       a - the list
    """
    n = len(a)
    
    # go through each element in the list
    for i in range(n):
        # k is the position holding the smallest value of the unsorted terms;set
        # its default equal to i
        k = i 
        
        # check all the other elements for if they are smaller than the default
        for j in range(i + 1, n):
            # if you find a term smaller than the value at the default position 
            # then set that position as the smallest value
            if a[j] < a[k]:
                k = j
        
        # swap the ith position with the position holding the smallest term
        swap(a, i, k)
    return

def heapSort(a):
    """
    This function accepts a lists of values. It converts the list into a heap using
    a heap object and then sorts it by using the deleteMin().
       a- a list 
    """
    # initialize the heap
    theHeap = minHeap()
    
    # heapify the list
    theHeap.heapify(a)
    
    # delete the min value from the heap and translate it to the list until the heap is empty
    i = 0 # index
    while not theHeap.isEmpty():
        minValue = theHeap.deleteMin()
        a[i] = minValue
        i += 1
    
    return   

def main():
    # Create the original list of randome numbers
    myList = [random.randint(-500, 500) for i in range(N)]

    # Prepare list to be sorted
    sortingList = []
    copyList(myList, sortingList, len(myList))
    print("The unsorted list:")
    print(sortingList)
    print("\n")

    ######### BUBBLE SORT ######### 
    startTime = time.time()

    bubbleSort(sortingList)

    endTime = time.time()
    print("Time to bubble sort a list of " + str(N), end="")
    print(" values was " + "{0:.4f}".format(endTime - startTime) + " seconds")

    print("After bubble sort, the list is:")
    print(sortingList)
    print("List is sorted: " + str(isListSorted(sortingList)))
    print("\n")

    # Prepare list to be sorted
    sortingList = []
    copyList(myList, sortingList, len(myList))
    print("The unsorted list:")
    print(sortingList)
    print("\n")

    ######### INSERTION SORT #########
    startTime = time.time()

    insertionSort(sortingList)

    endTime = time.time()
    print("Time to insertion sort a list of " + str(N), end="")
    print(" values was " + "{0:.4f}".format(endTime - startTime) + " seconds")

    print("After insertion sort, the list is:")
    print(sortingList)
    print("List is sorted: " + str(isListSorted(sortingList)))

    # Prepare list to be sorted
    print("\n")
    sortingList = []
    copyList(myList, sortingList, len(myList))
    print("The unsorted list:")
    print(sortingList)
    print("\n")

    ######### MERGE SORT #########
    startTime = time.time()

    mergeSort(sortingList)

    endTime = time.time()
    print("Time to merge sort a list of " + str(N), end="")
    print(" values was " + "{0:.4f}".format(endTime - startTime) + " seconds")

    print("After merge sort, the list is:")
    print(sortingList)
    print("List is sorted: " + str(isListSorted(sortingList)))
    print("\n")

    # Prepare list to be sorted
    sortingList = []
    copyList(myList, sortingList, len(myList))
    print("The unsorted list:")
    print(sortingList)
    print("\n")

    ######### QUICKSORT #########
    startTime = time.time()

    quickSort(sortingList)

    endTime = time.time()
    print("Time to quick sort a list of " + str(N), end="")
    print(" values was " + "{0:.4f}".format(endTime - startTime) + " seconds")

    print("After quick sort, the list is:")
    print(sortingList)
    print("List is sorted: " + str(isListSorted(sortingList)))
    print("\n")
    
    # Prepare list to be sorted
    sortingList = []
    copyList(myList, sortingList, len(myList))
    print("The unsorted list:")
    print(sortingList)
    print("\n")
    
    ######### SELECTIONSORT #########
    startTime = time.time()

    selectionSort(sortingList)

    endTime = time.time()
    print("Time to selection sort a list of " + str(N), end="")
    print(" values was " + "{0:.4f}".format(endTime - startTime) + " seconds")

    print("After selection sort, the list is:")
    print(sortingList)
    print("List is sorted: " + str(isListSorted(sortingList)))
    print("\n")  
    
    # Prepare list to be sorted
    sortingList = []
    copyList(myList, sortingList, len(myList))
    print("The unsorted list:")
    print(sortingList)
    print("\n")
    
    ######### HEAPSORT #########
    startTime = time.time()

    heapSort(sortingList)

    endTime = time.time()
    print("Time to heap sort a list of " + str(N), end="")
    print(" values was " + "{0:.4f}".format(endTime - startTime) + " seconds")

    print("After heap sort, the list is:")
    print(sortingList)
    print("List is sorted: " + str(isListSorted(sortingList)))
    print("\n")    

main()
