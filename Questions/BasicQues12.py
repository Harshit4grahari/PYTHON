# WAP to check if a list contains a palindrome of elements or not
def is_palindrome(lst):
    return lst == lst[::-1]
elements = input("Enter a list of elements (separated by commas): ").split(",")
if is_palindrome(elements):
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")


# 2nd Method using copy() method
list1 = input("Enter the elements of the line separated by commas: ").split(",")
list2 = list1.copy()
list2.reverse()
if list1 == list2:
    print("The list is a Palindrome.")
else:
    print("The list is not a palindrome.")
