#Recursion is a programming technique where a function calls itself in order to solve a problem.
# It typically involves a base case that stops the recursion and a recursive case that breaks the problem into smaller subproblems.
#Recursive function
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(5) 

#Return n!
def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*factorial(n - 1)
print(factorial(5))