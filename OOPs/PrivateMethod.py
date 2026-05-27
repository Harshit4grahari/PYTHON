#Private(like) attributes and methods in Python
# Private attributes and methods are meant to be used only within the class and are not
# accessible from outside the class.
#  In Python, we can indicate that an attribute or method is private by prefixing its name with a double underscore (__).

class Account:
    def __init__(self, acc_no, acc_password):
        self.acc_no = acc_no  # Public attribute
        self.__acc_password = acc_password  # Private attribute
    def get_password(self):
        return self.__acc_password  # Accessing private attribute within the class
    print(self.__acc_password)  # This will cause an error because it's trying to access a private attribute outside of the class   
account = Account("1234567890", "my_secure_password")
print("Account Number:", account.acc_no)  # Accessing public attribute
print("Account Password:", account.get_password())  # Accessing private attribute through a public method