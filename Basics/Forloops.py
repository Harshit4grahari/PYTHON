#For loops are used to iterate over a sequence (such as a list, tuple, or string) and execute a block of code for each element in the sequence.
#The syntax of a for loop is as follows:
#for variable in sequence:
#    # code to be executed

#Example of a for loop that prints numbers from 1 to 5
for i in range(1, 6):
    print(i)

#Example of a for loop that prints elements of a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

#Example of a for loop that prints characters of a string
for char in "Hello, World!":
    print(char)

#For loop with Else statement
print("Example of a for loop with an else statement:") 
for i in range(1, 6):
    print(i)
else:
    print("Loop completed successfully.")
    