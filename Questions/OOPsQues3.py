# Define a Employee class with attributes role, department, and salary. this class also showDetails() method to print the details of the employee.
# create an engineer class that inherits properties from Employee and has an attributes: name and age

class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary
    def showDetails(self):
        print("Role:", self.role)
        print("Department:", self.department)
        print("Salary:", self.salary)

class Engineer(Employee):
    def __init__(self, name, age, role, department, salary):
        super().__init__(role, department, salary)
        self.name = name
        self.age = age

    def showDetails(self):
        super().showDetails()
        print("Name:", self.name)
        print("Age:", self.age)

eng1 = Engineer("Harshit", 22, "Software Engineer", "IT", 80000)
eng1.showDetails()