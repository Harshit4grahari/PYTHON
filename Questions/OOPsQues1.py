#Create students class that takes name and marks of 3 subjects as arguments in constructor.
#  Then create a method to print the average.

class Students:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for marks in self.marks:
            sum += marks
            avg = sum / len(self.marks)
        return f"Average marks of {self.name} is {avg}"

s1 = Students("Harshit", [85, 90, 78])
print(s1.get_avg())
