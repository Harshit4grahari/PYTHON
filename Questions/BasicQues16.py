#Print the multiplication table of a number n using while loop.

n=int(input("Enter a number to print its multiplication table: "))
i =1
while i <= 10:
    print(n, "x", i, "=", n*i)
    i+=1