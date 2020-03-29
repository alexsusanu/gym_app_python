#https://docs.python.org/3/library/sqlite3.html
#Google

from menu import *
from db import *

Menu.show_menu()

user_input = int(input("Select an option: "))
flag = True

while flag:
    if user_input not in Menu.select_list:
        print("Please choose from the options shown")
        user_input = int(input("Select an option: "))
    else: 
        Menu.select(user_input)
        #if user_input == 1:
        #    insert_in_db()
        flag = False


      
