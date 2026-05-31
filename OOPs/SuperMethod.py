#Super() Method is used to call the parent class method in the child class.
# It is used to access the methods of the parent class from the child class.

# Example of Super() Method in Python
# Parent class
class Parent:
    def display(self):
        return "This is the parent class."
    
# Child class that inherits from Parent
class Child(Parent):
    def display(self):
        parent_message = super().display()  # This will call the display method of the parent class
        return f"{parent_message} This is the child class."
child = Child()
print(child.display())
