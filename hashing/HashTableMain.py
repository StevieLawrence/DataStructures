from HashTableChaining import HashTableChaining
from HashTableProbing import HashTableProbing
from Student import Student
import time

def main():

    
    file = open("listOfNames_short.txt", "r")
    #myTable = HashTableChaining(503)
    myTable = HashTableProbing(503)
    print(myTable)
    i = 0
    for line in file:
        s = line.strip().split("\t")
        p = Student(int(s[0]), s[1])
        # print(p)
        myTable.put(p)
        i += 1
        
    file.close()
    print(myTable)


    searchPeople = []
    file = open("searchIds_short.txt", "r")
    for line in file:
        s = line.strip().split("\t")
        searchPeople.append(Student(int(s[0])))
    file.close()

    startTime = time.time()
    for person in searchPeople:
        searchPerson = myTable.retrieve(person)
        print(searchPerson)
    endTime = time.time()
    print ("Number of seconds = {0:.2f}".format(endTime - startTime))

    
main()