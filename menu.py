#https://stackoverflow.com/questions/36849108/calling-a-function-from-within-a-dictionary

#elements outside __init__ belong to the class
#elements inside __init__ belong to the object (instance of the class)/(self)
#attribute -> inner data of an object (inside vars, methods)

from db import *

class Menu:
    select_list = [0,1,2,3,4,5,6,7,8]
    def __init__(self):
        print(60 * "-")
        print("\tPlease select from the following options:")
        print(60 * "-")
        print("\t*** 0 (zero) to return to main menu ***")
        print("1. Insert new member \t\t2. Update existing member")
        print("3. Show members  \t\t4. Select a member to view details")
        print("5. Delete a member \t\t6. Expired memberships")
        print("7. Soon to expire memberships \t8. Quit")

    #calling a function from within a dictionary
    def select(arg): #python alternative for switch case
        switch =  {
            1: DB.insert_in_db, #reference the function name
            2: DB.update_member,
            3: DB.show_members,
            4: DB.view_member_details,
            5: DB.delete_member,
            6: DB.expired_memberships,
            7: DB.soon_to_expire,
            8: exit, #builtin function
            0: Menu.main_menu
        }
        switch.get(arg, "Invalid option")() #calling the function here with ()


    def main_menu():#TO DO
        Menu()
        user_input = int(input("Select an option: "))
        flag = True
        while flag:
            if user_input not in Menu.select_list:
                print("Please choose from the options shown")
                user_input = int(input("Select an option: "))
            else: 
                Menu.select(user_input)
                flag = False
