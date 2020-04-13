#https://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/

#CURSOR:
#symbol that indicates the CURSOR / iterator
#an object used to pinpoint records in a database
#shows the specific record in the database that is being worked upon

#CURSOR -> static variable
#self.CURSOR -> instance variable
#elements outside methods belong to the class

#used as place holders (?,?,?,?)
#CONNECTION.commit() #save changes to the db
#CONNECTION.close() #close the db
""" functions related to db processing """
import sqlite3 
from definitions import CONNECTION, CURSOR

from members import Member
from time_functions import *

from modules.func import quit_or_menu
from modules.func import print_stars
from modules.func import check_input
from modules.func import check_digit
from modules.func import send_to_dict
from modules.func import from_dict_by_id
from modules.func import yes_no
from modules.class_member_func import MemberFunc
from modules.class_run_sql import run_sql_script, attributes, run_select_all, run_select_name, run_update, run_insert

def com_close(): #to add error checking
    """ commit and close db """
    print_stars()
    CONNECTION.commit()
    print("changes commited to db")
    CONNECTION.close()
    print("connection to db closed. no errors")


def insert_in_db():
    """ insert member in db """
    run_insert()
    com_close()


def show_members(): #TO DO modify to get only name surname
    """ show list of all members """
    print("Select 1 to view all details or 2 for names only", end=" ")
    user_input = input()
    user_input = check_digit(user_input)
    if int(user_input) == 1:
        run_select_all()
    elif int(user_input) == 2:
        run_select_name()
    else:
        print("Invalid number, returning...")
        show_members()

def update_member():
    """ self explanatory """
    print_stars()
    print("Previous first and last name to update")
    print_stars()
    first_name, last_name = Member.ask_name()

    to_be_or_not = MemberFunc(first_name, last_name) 

    if not to_be_or_not.already_member():
        print("Member doesnt exist. q to quit or m for main menu")
        user_input = input()
        quit_or_menu(user_input)
    else:
        to_be_or_not.view_matches()
        id_to_del = to_be_or_not.id_to_del()
        print("Insert NEW details:")
        run_update(first_name, last_name, id_to_del)
        com_close()

def view_member_details(): #SAME AS ABOVE TO CHECK IF MEMBER EXISTS ECC
    """ self explanatory """
    first, last = Member.ask_name()

    run_sql_script(VIEW_MEMBER_SQL, (first_name, last_name))
    rows = CURSOR.fetchall()
    get_attributes(rows, attributes())


def delete_member():
    """ self explanatory """
    first_name = Member.first_name()
    last_name = Member.last_name()
    print_stars()

    one_member, plus_member, id_to_del, no_member = member_exists(first_name, last_name)
    if plus_member:
        run_sql_script(DELETE_ID_SQL, (id_to_del,))
        print("Member deleted")
    if one_member:
        run_sql_script(DELETE_MEMBER_SQL, (first_name, last_name))
        print("Member deleted")
    if no_member:
        print("No member found, check your spelling. [q to quit, m for main menu]")
        quit_or_menu(user_input=input())

    CONNECTION.commit()
    CONNECTION.close()

def expired_memberships(): pass

def soon_to_expire(): pass
