#Print the elements of a list using a while loop.
# [1,4,9,16,25,36,49,64,81,100]

i=1
while i <= 10:
    print(i**2)
    i+=1

#Method 2
numbers = [1,4,9,16,25,36,49,64,81,100]
idx = 0
while idx < len(numbers):
    print(numbers[idx])
    idx += 1