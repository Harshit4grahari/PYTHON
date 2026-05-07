#Creat a new file "practice.txt" using python. Add the following data in it.

'''Hi everyone
we are learning file I/O
using python
I like programming in python'''

with open("practice.txt", "w") as f:
    f.write("Hi everyone\n")
    f.write("we are learning file I/O\n")
    f.write("using python\n")
    f.write("I like programming in python\n")