#While loops are used to repeat a block of code as long as a certain condition is true.
#The syntax of a while loop is as follows:
#while condition:
#    # code to be executed

#Example of a while loop that prints numbers from 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1

#Breaking out of a while loop
print("Example of breaking out of a while loop:")
i = 1
while i <= 5:
    print(i)
    if i == 3:
        break
    i += 1
print("Exited the loop")

#Continuing to the next iteration of a while loop
print("Example of continuing to the next iteration of a while loop:")
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

print("Second Example")
i = 0
while i <= 20:
    if(i%2 == 0):
        i += 1
        continue #skips the rest of the code in the loop and goes to the next iteration
    print(i)
    i += 1