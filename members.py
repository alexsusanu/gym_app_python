#elements outside __init__ belong to the class
#elements inside __init__ belong to the object (instance of the class)/(self)

#object -> instance of a class
#self -> refers to the object that is being worked upon, the instance of the class
#constructor / __init__ -> used to initialize object (to set initial values) 

class Member: #a category of things that have common properties
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def print_name(self):
        return self.name

    def print_surname(self):
        return self.surname


