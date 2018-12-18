from AVLTree import AVLTree

''' Main program to test the AVL Tree class '''

def main():
    # Create the tree
    avlBST = AVLTree()

    # Test the boolean functions on an empty tree

    print ("isAVLTree() = " + str(avlBST.isAVLTree()))
    print ("isEmpty() = " + str(avlBST.isEmpty()))
    print ()

    # Building the tree

    values = [41, 72, 9, 59, 86, 62, 2, 46, 52, 55, 57, 58]
    
    for data in values:
        print("inserting: " + str(data))
        avlBST = avlBST.insert(data)
        print(avlBST)
        print ()


    # Test retrieving values 

    print ("\n")
    print ("Retreiving Values")
    for data in values:
        print(avlBST.retrieve(data))

    # Test the boolean functions again

    print ("\n")
    print ("isAVLTree() = " + str(avlBST.isAVLTree()))
    print ("isEmpty() = " + str(avlBST.isEmpty()))
    print ()

main()


