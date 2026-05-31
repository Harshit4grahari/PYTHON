#Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a new class (called a child or subclass) to inherit properties and behaviors (attributes and methods) 
# from an existing class (called a parent or superclass). This promotes code reusability and establishes a natural hierarchical relationship between classes.

# Example of Inheritance in Python
# Parent class (superclass)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"
# Child class (subclass) that inherits from Animal
class Dog(Animal):
    def speak(self):
        return "Woof!"
# Child class (subclass) that inherits from Animal
class Cat(Animal):
    def speak(self):
        return "Meow!"
    
print("Inheritance Example:")
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(f"{dog.name} says: {dog.speak()}")
print(f"{cat.name} says: {cat.speak()}")
