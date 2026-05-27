#Abstraction is a process of hiding the implementation details and showing only functionality to the user.
#In Python, we can achieve abstraction by using abstract classes and interfaces.

from abc import ABC, abstractmethod
# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
# Concrete class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius

print("Area of circle with radius 5 is:", Circle(5).area())

# Concrete class
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.acc = True
        self.brk = False
        self.clutch = False
        return "Car started"
    
car1 = Car()
print(car1.start())
    