# Tuple in Python
# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.

my_tuple = (1, 334, 34, 43)
print("My tuple:", my_tuple)    

# Accessing elements in a tuple
print("First element:", my_tuple[0])    
print("Last element:", my_tuple[-1])

# Tuple slicing
print("Elements from index 1 to 3:", my_tuple[1:4])

# Tuple length
print("Number of elements in the tuple:", len(my_tuple))

# Tuple functions
print("Maximum element in the tuple:", max(my_tuple)) 
print("Minimum element in the tuple:", min(my_tuple))  
#Wwe cannot compare different data types
# We can also have a tuple of different data types
mixed_tuple = (1, "Hello", 3.14, True)
print("Mixed tuple:", mixed_tuple)

# They are immutable, which means we cannot change their content after they are created.

# However, we can concatenate two tuples to create a new tuple
tuple1 = (1, 2, 3)
tuple2 = ("a", "b", "c")
concatenated_tuple = tuple1 + tuple2
print("Concatenated tuple:", concatenated_tuple)
