#Search for a specific element in a list using a for loop and print its index if found, otherwise print "Element not found".
numbers = [1,4,9,16,25,36,49,64,81,100]
element = int(input("Enter the element to search for: "))
found = False
for i in range(len(numbers)):
    if numbers[i] == element:
        print(f"Element found at index {i}")
        found = True
        break
if not found:
    print("Element not found")