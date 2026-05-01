#Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#Sets are written with curly brackets.

my_set = {1, 2, 3, 4, 5}
print("My set:", my_set)

# Accessing elements in a set
# We cannot access elements in a set by index because sets are unordered and unindexed.
# Modifying elements in a set
# We cannot modify elements in a set because sets are unchangeable, but we can add or remove elements.
my_set.add(6)
print("My set after adding an element:", my_set)
my_set.remove(3)
print("My set after removing an element:", my_set)

# Set functions
print("Length of my set:", len(my_set))
print("Is 4 in my set?", 4 in my_set)
print("Is 3 in my set?", 3 in my_set)
print("Union of my set and another set {5, 6, 7}:", my_set.union({5, 6, 7}))
print("Intersection of my set and another set {5, 6, 7}:", my_set.intersection({5, 6, 7}))
print("Difference of my set and another set {5, 6, 7}:", my_set.difference({5, 6, 7}))
print("Symmetric difference of my set and another set {5, 6, 7}:", my_set.symmetric_difference({5, 6, 7}))
print(type(my_set)) #<class 'set'>
