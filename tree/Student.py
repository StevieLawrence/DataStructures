class Student:
    def __init__(self, id=None, name=""):
        self.__id = id
        self.__name = name

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getName(self):
        return self.__name


    def setName(self, name):
        self.__id = name

    def __str__(self):
        if (self is None):
            return ""
        else:
            return str(self.__id) + "(" + self.__name + ")"

    def __cmp__(self, other):
        if (self is None or other is None):
            return 0
        else:
            return self.__id - other.__id

    def __eq__(self, other):
        return self.__cmp__(other) == 0

    def __ne__(self, other):
        return self.__cmp__(other) != 0

    def __lt__(self, other):
        return self.__cmp__(other) < 0

    def __le__(self, other):
        return self.__cmp__(other) <= 0

    def __gt__(self, other):
        return self.__cmp__(other) > 0

    def __ge__(self, other):
        return self.__cmp__(other) >= 0
