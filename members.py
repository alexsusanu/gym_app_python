#elements outside __init__ belong to the class
#elements inside __init__ belong to the object (instance of the class)/(self)

#object -> instance of a class
#self -> refers to the object that is being worked upon, the instance of the class
#constructor / __init__ -> used to initialize object (to set initial values) 

class Member: #a category of things that have common properties
    #def __init__(self, first_name, last_name, phone_number, email):
    #    self.first_name = first_name
    #    self.last_name = last_name
    #    self.phone_number = phone_number
    #    self.email = email

    @staticmethod
    def first_name():
        print("Insert FIRST NAME: ")
        first_name = input()
        return first_name.title()

    @staticmethod
    def last_name():
        print("Insert LAST NAME: ")
        last_name = input()
        return last_name.title()

    @staticmethod
    def phone_number():
        print("Insert PHONE NUMBER: ")
        phone_number = input()
        return phone_number

    @staticmethod
    def email():
        print("Insert EMAIL ADDRESS: ")
        email = input()
        return email

