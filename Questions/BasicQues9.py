#WAP using nesting conditional statement to check driving age between 18 and 60 else print cannot drive
age = int(input("Enter your age:")) #taking input from user and converting it to integer
if age >= 18:
    if age < 60:
        print("You are eligible to drive.")
    else:
        print("You are too old to drive.")