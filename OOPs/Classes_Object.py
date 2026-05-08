#Classes is a blueprint for creating objects. An object has properties and methods(functions) associated with it.
#  Almost everything in Python is an object, with its properties and methods. A class is like an object constructor, or a "blueprint" for creating objects.
#Defining a class
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"
    
#Creating an object of the class
student1 = Student("Alice", 20, "A")
#Accessing properties and methods of the object
print(student1.name)  # Accessing property
print(student1.display_info())  # Calling method
#Creating another object of the class
student2 = Student("Bob", 22, "B")
print(student2.display_info())