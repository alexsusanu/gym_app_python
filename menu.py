#https://stackoverflow.com/questions/36849108/calling-a-function-from-within-a-dictionary

#elements outside __init__ belong to the class
#elements inside __init__ belong to the object (instance of the class)/(self)
#attribute -> inner data of an object (inside vars, methods)

from db import *

class Menu:
    select_list = [1,2,3,4,5,6]
    def show_menu():
        print("Please select from the following options: \n")
        print("1. Insert new member \t2. Update existing member")
        print("3. Show members  \t4. Select a member to view details")
        print("5. Delete a member \t6. Quit")

    #calling a function from within a dictionary
    def select(arg): #python alternative for switch case
        switch =  {
            1: DB.insert_in_db, #reference the function name
            2: DB.update_member,
            3: DB.show_members,
            4: DB.view_member_details,
            5: DB.delete_member,
            6: exit, #builtin function
        }
        if arg == 2:
            print("Insert name to update: ")
            switch.get(arg, "Invalid option")(input(), input()) #calling the function here with ()
        else:
            switch.get(arg, "Invalid option")() #calling the function here with ()


