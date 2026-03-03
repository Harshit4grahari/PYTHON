#we use if-elif-else statement for conditional execution in Python

age = int(input("Enter your age:")) #taking input from user and converting it to integer   
if age < 18:
    print("You are a minor.")
elif age>=18 and age<60:
    print("You are an adult.")
else:
    print("You are a senior citizen.") 