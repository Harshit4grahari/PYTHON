#Search if the  word "learning" exist in the file or not.

with open("practice.txt", "r") as f:
    data = f.read()

if (data.find("learning") != -1):
    print("The word 'learning' exists in the file.")
else:
    print("The word 'learning' does not exist in the file.")