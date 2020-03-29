#https://stackoverflow.com/questions/36849108/calling-a-function-from-within-a-dictionary

#elements outside __init__ belong to the class
#elements inside __init__ belong to the object (instance of the class)/(self)
#attribute -> inner data of an object (inside vars, methods)

from db import *

class Menu:
    select_list = [1,2,3,4]
    def show_menu():
        print("Please select from the following options: \n")
        print("1. Insert new member \t2. Update existing member")
        print("3. Delete a member \t4. Quit")

    #calling a function from within a dictionary
    def select(arg): #python alternative for switch case
        switch =  {
            1: DB.insert_in_db, #reference the function name
            2: DB.update_member,
            3: DB.delete_member,
            4: exit, #builtin function
        }
        switch.get(arg, "Invalid option")() #calling the function here with ()


