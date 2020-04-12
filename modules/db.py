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
import sqlite3 #import sqlite3 library

from members import Member
from time_functions import *

from modules.func import quit_or_menu
from modules.func import print_stars
from modules.func import check_input
from modules.func import send_to_dict
from modules.func import from_dict_by_id
from modules.func import yes_no

from definitions import VIEW_MEMBER_SQL
from definitions import SELECT_ALL_SQL
from definitions import INSERT_SQL
from definitions import DELETE_MEMBER_SQL
from definitions import UPDATE_MEMBER_SQL
from definitions import UPDATE_ID_SQL
from definitions import DELETE_ID_SQL

CONNECTION = sqlite3.connect('GYM_DATABASE.db') #connect to db/create new otherwise
CURSOR = CONNECTION.cursor()


def run_sql_script(filename, *args):
    """ execute sql files """
    file = open(filename, 'r')
    sql_file = file.read()
    file.close()
    CURSOR.execute(sql_file, *args)

def attributes(): #get columns description (member_id, first_name, last_name, ecc)
    """ get column description from sql db, id name surname ecc """
    run_sql_script(SELECT_ALL_SQL)
    return [description[0] for description in CURSOR.description]

def get_attributes(arr, att):
    """ pair column description/attributes with values """
    att = attributes()
    print_stars()
    for elm in arr:
        for i, element in enumerate(att):
            print("%s: %s" % (element, elm[i]))
        print_stars()

def member_exists(first_name, last_name):
    members, member_id = members_array_id()
    member_already = member_already()
    if member_already:
        view_matches()
    else:
        return False

def members_array_id():
    """ add all members in array with a separate member id array """
    member_id = []

    run_sql_script(VIEW_MEMBER_SQL, (first_name, last_name))
    members = CURSOR.fetchall()

    for member in members:
        member_id.append(member[0])

    return members, member_id

def member_already():
    """ check if member already exists """
    """ returns true false only"""
    member_already = False
    if member_id: member_already = True
    return member_already

def view_matches():
    if len(member_id) >= 1:
        print("More than 1 member exists with same name and surname.")
        print("To view all matches type 'y'")
        print("Type 'n' to quit or main menu. | ", end=" ")
        user_input = input()
        yes_no(user_input)
        if yes_no:
            get_attributes(members, attributes())
            print("If you wish to delete or update, type 'y'")
            print("Type 'n' to quit or main menu", end=" ")
            user_input = input()
            yes_no(user_input)
            if yes_no:
                id_to_del = id_to_del()
            else:
                print("q to quit, m for main menu")
                quit_or_menu()
        else:
            print("q to quit, m for main menu")
            quit_or_menu()
    else:
        return False

def id_to_del():
    """ id to delete or update """
    id_to_del = None
    print("Type member's ID to delete or update. Select %s | " % member_id)
    user_input = input()
    id_to_del = check_input(user_input, member_id)
    dictionary = send_to_dict(members, attributes())
    from_dict_by_id(dictionary, user_input)
    return id_to_del
id_to_del = id_to_del()

def insert_in_db():
    """ insert member in db """
    first_name = Member.first_name()
    last_name = Member.last_name()
    phone_number = Member.phone_number()
    email = Member.email()
        
    #member_already = member_exists(first_name, last_name)
    #if member_aleady:
    #    print("Do you wish to delete or update? You will be directed to main menu| ", end=" ")
    #    user_input = input()
    #    yes_no(user_input)
    #    if yes_no:
    #        Menu()
    #else:
    run_sql_script(INSERT_SQL, (first_name, last_name, phone_number, email, date_format_dmy(), date_end_membership()))

    CONNECTION.commit()
    CONNECTION.close()

    print("{0} {1} member added to database on {2} at {3}".format(first_name, last_name, date_format_dmy(), time_format_hm()))


def show_members(): #TO DO modify to get only name surname
    """ show list of all members """
    run_sql_script(SELECT_ALL_SQL)
    rows = CURSOR.fetchall()
    get_attributes(rows, attributes())
    print("Total members: %d" % len(rows))

def update():
    print_stars()
    print("Insert NEW details:")
    print_stars()
    first = Member.first_name()
    last = Member.last_name()
    phone = Member.phone_number()
    email = Member.email()
    return first, last, phone, email
    

def update_member(): #TO CHECK IF MEMBER EXISTS ECC
    """ self explanatory """
    print_stars()
    print("Previous first and last name to update")
    print_stars()
    first_name = Member.first_name()
    last_name = Member.last_name()

    member_exists(first_name, last_name)
    if not no_member:
        print("Member doesnt exist. q to quit or m for main menu")
        user_input = input()
        quit_or_menu(user_input)
    elif plus_member:
        new_first_name, new_last_name, new_phone_number, new_email = update()
        run_sql_script(UPDATE_ID_SQL, (new_first_name, new_last_name, new_phone_number, new_email, first_name,
        last_name, id_to_del))
    else:
        new_first_name, new_last_name, new_phone_number, new_email = update()
        run_sql_script(UPDATE_MEMBER_SQL, (new_first_name, new_last_name, new_phone_number, new_email, first_name, last_name))
    CONNECTION.commit()
    CONNECTION.close()

def view_member_details(): #SAME AS ABOVE TO CHECK IF MEMBER EXISTS ECC
    """ self explanatory """
    first_name = Member.first_name()
    last_name = Member.last_name()

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
