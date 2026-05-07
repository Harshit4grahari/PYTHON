#File I/O in Python
#File I/O stands for File Input/Output. It allows us to read from and write

#Reading from a file
f = open("C:\\Users\\agrah\\OneDrive\\Desktop\\PYTHON\\Demo.txt", "r")
data = f.read(5) #Reads first 5 characters from the file
print(data)
print(type(data))


#Read line by line
f = open("C:\\Users\\agrah\\OneDrive\\Desktop\\PYTHON\\Demo.txt", "r")
line1 = f.readline() #Reads the first line from the file
print(line1)

line2 = f.readline() #Reads the second line from the file
print(line2)

#Writing to a file
f = open("C:\\Users\\agrah\\OneDrive\\Desktop\\PYTHON\\Demo.txt", "w") #This will overwrite the existing content of the file
f.write("Hello, this is a demo file.\n")
f.write("This file is used to demonstrate File I/O in Python.\n")


#Appending to a file
f = open("C:\\Users\\agrah\\OneDrive\\Desktop\\PYTHON\\Demo.txt", "a") #This will append to the existing content of the file
f.write("This line is appended to the file.\n")
f.close()