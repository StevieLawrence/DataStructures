from binarySearchTree import BinarySearchTree
from Student import Student


def main():
    BST = BinarySearchTree()
    print("isEmpty() = " + str(BST.isEmpty()))
    print(BST)

    BST.setData(Student(101, "Betty Smith"))
    print("isEmpty() = " + str(BST.isEmpty()))
    print(BST)

    BST.insert(Student(50, "John Adams"))
    print(BST)

    BST.insert(Student(250, "Mike Jones"))
    print(BST)

    BST.insert(Student(42, "Amy Winchester"))
    print(BST)

    BST.insert(Student(31, "Jill Ranger"))
    print(BST)

    BST.insert(Student(315, "Bob Crachet"))
    print(BST)

    BST.insert(Student(200, "Karen Wilkins"))
    print(BST)
    print("\n")

    print()
    print("Inorder traversal: " + str(BST))
    print()
    print("Preorder traversal: \n" + BST.preOrderTraversal())
    print()
    print("Postorder traversal: " + BST.postOrderTraversal())

    print()
    print("minValue: " + str(BST.minValue()))
    print("maxValue: " + str(BST.maxValue()))
    print()
    print("isBST = " + str(BST.isBST()))

    for id in [101, 200, 31, 50, 315, 250, 42]:
        print(BST.retrieve(Student(id)))
main()