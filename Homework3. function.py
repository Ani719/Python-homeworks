import os
def WordsCount(path):
    f = open(path, "r")
    string = f.read()

    array = string.split()
    print(len(array))

    for i in array:
        print(i)

WordsCount("Files/Home3.txt")