# DEL Keyword in Python
# The del keyword is used to delete objects in Python.

# Example 1: Deleting a variable
x = 5
print(x)
del x
# print(x)  # This will raise an error because x is deleted

# Example 2: Deleting an item from a list
my_list = [1, 2, 3, 4, 5]
print(my_list)
del my_list[2]  # Deletes the item at index 2
print(my_list)

# Example 3: Deleting a key from a dictionary
my_dict = {"a": 1, "b": 2, "c": 3}
print(my_dict)
del my_dict["b"]  # Deletes the key-value pair with key "b"
print(my_dict)