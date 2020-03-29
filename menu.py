#https://stackoverflow.com/questions/36849108/calling-a-function-from-within-a-dictionary

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
            1: insert_in_db, #reference the function name
            2: update_member,
            3: delete_member,
            4: exit, #builtin function
        }
        switch.get(arg, "Invalid option")() #calling the function here with ()


