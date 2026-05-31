#Multiple inheritance is a feature in object-oriented programming (OOP) where a class can inherit attributes
#  and methods from more than one parent class. This allows for greater flexibility and code reuse,
#  but it can also lead to complexity and ambiguity if not used carefully.

# Example of Multiple Inheritance in Python
# Parent class 1
class Father:
    def skills(self):
        return "Gardening, Programming"
# Parent class 2
class Mother:
    def skills(self):
        return "Cooking, Art"
# Child class that inherits from both Father and Mother
class Child(Father, Mother):
    def skills(self):
        father_skills = super().skills()  # This will call the skills method of the first parent class (Father)
        mother_skills = Mother.skills(self)  # This will call the skills method of the second parent class (Mother)
        return f"{father_skills}, {mother_skills}"
child = Child()
print("Child's skills:", child.skills())