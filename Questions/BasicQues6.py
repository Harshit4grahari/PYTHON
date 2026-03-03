#write a program to find the occurence of $ in a string

#First method
string = input("Enter string: ")
count = 0
for char in string:
    if char == '$':
        count += 1
print("The number of occurrences of '$' in the string is:", count)

#Second method
string = input("Enter a string: ")
print("The number of occurrences of '$' in string:", string.count('$'))