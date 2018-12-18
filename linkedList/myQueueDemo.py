## This program tests the myQueue class

# imports
from myQueue import myQueue
import random

# create a queue
theQueue = myQueue()

print()
print("Initial IsEmpty Test:")
print("the queue is empty ==", theQueue.isEmpty())
print()

print("Initial Peek Test:")
print("the peak is", theQueue.peek())
print()

print("Initial Size Test:")
print("the size is", theQueue.size())
print()

print("Enqueue Test:")
for i in range(20):
    num = random.randint(-100, 100)
    theQueue.enqueue(num)
    print("added item %02i is %i" % ( i + 1, num))
print()

print("isEmpty Filled Queue Test:")
print("the queue is empty ==", theQueue.isEmpty())
print()

print("Peek Filled Queue Test:")
print("the peak is", theQueue.peek())
print()

print("Size Filled Queue Test:")
print("the size is", theQueue.size())
print()

print("Dequeue Test:")
k = 1
while k <= 20:
    n = theQueue.dequeue()
    print("removed item %02i is %i" % (k, n))
    k += 1
print()

print("End isEmpty Test:")
print("the queue is empty ==", theQueue.isEmpty())
print()

print("End Peek Test:")
print("the peak is", theQueue.peek())
print()

print("End Size Test:")
print("the size is", theQueue.size())