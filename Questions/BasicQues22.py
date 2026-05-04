#WAP to find the factorial of a number n using for loop.
n = int(input("Enter a number to find its factorial: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print("The factorial of", n, "is:", factorial)