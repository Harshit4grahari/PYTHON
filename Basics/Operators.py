A = 15770
B = 125
print("The sum of A and B is:", A + B)
print("The difference of A and B is:", A - B)
print("The product of A and B is:", A * B)
print("The quotient of A and B is:", A / B)
print("The remainder of A and B is:", A % B)
print("The integer quotient of A and B is:", A // B)
print("Check if A and B are equal:", A == B)
print("Check if A and B are not equal:", A != B)
print("Check if A is greater than B:", A > B)
print("Check if A is less than B:", A < B)
print("Check if A is greater than or equal to B:", A >= B)
print("Check if A is less than or equal to B:", A <= B)

c = 10.5
d = 20.3
print("The sum of c and d is:", c + d) 

d = A + B + c + d
print("The sum of A, B, c and d is:", d)  


'''All the above variables are of different types but we can still add or any 
mathemathical operation them together because Python is a dynamically typed language 
and it will automatically convert the types to a common type for the operation.'''

#assingment operators
x = 10
x += 5 # equivalent to x = x + 5
print("Value of x after addition:", x)  
#we can use the same assignment operator for other operations as well
x -= 3 # equivalent to x = x - 3 or other assignment operators like *=, /=, %=, //=, **=

#logical operators
p = 50
q = 30
print("Check if p is greater than q and p is less than 100:", p > q and p < 100)
print("Check if p is greater than q or p is less than 100:", p > q or p < 100)
print("Check if p is not greater than q:", not (p > q))
