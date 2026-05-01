#dictionaries are used to store data values in key:value pairs
#A dictionary is a collection which is ordered, changeable and does not allow duplicates.   
#Dictionaries are written with curly brackets, and they have keys and values.

student = {
    "name" : "Harshit Agrahari",
    "age" : 21,
    "course" : "Computer Science"
}
print(student)
print(type(student)) #<class 'dict'>

#Accessing values in a dictionary
print("Name of student:", student["name"])
print("Age of student:", student["age"])
print("Course of student:", student["course"])  

#Modifying values in a dictionary
student["age"] = 22
print("Modified student dictionary:", student)

#Adding new key:value pair to a dictionary
student["grade"] = "A"
print("Student dictionary after adding grade:", student)

#Removing key:value pair from a dictionary
del student["course"]
print("Student dictionary after removing course:", student)

#Dictionary functions   
print("Keys in student dictionary:", student.keys())
print("Values in student dictionary:", student.values())
print("Items in student dictionary:", student.items())
print("Number of key:value pairs in student dictionary:", len(student)) 
