import os
path = "Files/Home3.txt"
f = open(path, "r")
string = f.read()

array = string.split(" ");
print(len(array))

for i in array:
    print(i)