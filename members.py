#elements outside __init__ belong to the class
#elements inside __init__ belong to the object (instance of the class)/(self)

#object -> instance of a class
#self -> refers to the object that is being worked upon, the instance of the class
#constructor / __init__ -> used to initialize object (to set initial values)

from modules.func import check_alpha
from modules.func import check_digit
from modules.func import check_email

class Member: #a category of things that have common properties
    #def __init__(self, first_name, last_name, phone_number, email):
    #    self.first_name = first_name
    #    self.last_name = last_name
    #    self.phone_number = phone_number
    #    self.email = email

    @staticmethod
    def first_name():
        print("Insert FIRST NAME: ")
        user_input = input()
        return check_alpha(user_input)

    @staticmethod
    def last_name():
        print("Insert LAST NAME: ")
        user_input = input()
        return check_alpha(user_input)

    @staticmethod
    def phone_number():
        print("Insert PHONE NUMBER: ")
        user_input = input()
        return check_digit(user_input)

    @staticmethod
    def email():
        print("Insert EMAIL ADDRESS: ")
        user_input = input()
        return check_email(user_input)

