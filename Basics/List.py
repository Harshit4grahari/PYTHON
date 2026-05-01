#List in Python
#A list is a collection of items which is ordered and changeable. It allows duplicate members.
#Lists are written with square brackets.

marks = [85, 90, 78, 92, 88]
print("Marks of students:", marks) 
# Accessing elements in a list
print("First mark:", marks[0]) 
print("Last mark:", marks[-1])
# Modifying elements in a list  
marks[2] = 80
print("Modified marks of students:", marks)
# Adding elements to a list
marks.append(95)
print("Marks after adding a new mark:", marks)
# Removing elements from a list
marks.remove(88)
print("Marks after removing a mark:", marks)
# List slicing
print("Marks from index 1 to 3:", marks[1:4])
# List length
print("Number of marks in the list:", len(marks))
# List functions
print("Maximum mark:", max(marks))
print("Minimum mark:", min(marks))
print("Sum of marks:", sum(marks))
print("Average mark:", sum(marks) / len(marks))
print(type(marks)) #<class 'list'>
print(marks.sort()) # This will sort the list in place
print("Sorted marks:", marks)
print(marks.reverse()) # This will reverse the list in place
print("Reversed marks:", marks)

# We can also have a list of different data types
mixed_list = [1, "Hello", 3.14, True]

# We can also have a list of lists (nested list)
nested_list = [[1, 2, 3], ["a", "b", "c"], [True, False]]
print("Nested list:", nested_list)

#They are mutable, which means we can change their content without changing their identity.