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

from definitions import VIEW_MEMBER_SQL
from definitions import SELECT_ALL_SQL
from definitions import INSERT_SQL
from definitions import DELETE_MEMBER_SQL
from definitions import UPDATE_MEMBER_SQL
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

def insert_in_db():
    """ insert member in db """
    first_name = Member.first_name()
    last_name = Member.last_name()
    phone_number = Member.phone_number()
    email = Member.email()

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

def update_member(): #TO CHECK IF MEMBER EXISTS ECC
    """ self explanatory """
    first_name = Member.first_name()
    last_name = Member.last_name()

    one_member, plus_member, id_to_del, no_member = member_exists(first_name, last_name)
    if not no_member:
        print("Member doesnt exist. q to quit or m for main menu")
        user_input = input()
        quit_or_menu(user_input)
    else:
        new_first_name = Member.new_first_name()
        new_last_name = Member.new_last_name()
        run_sql_script(UPDATE_MEMBER_SQL, (new_first_name, new_last_name, first_name, last_name))
        CONNECTION.commit()
        CONNECTION.close()
        print("Member updated")

def view_member_details(): #SAME AS ABOVE TO CHECK IF MEMBER EXISTS ECC
    """ self explanatory """
    first_name = Member.first_name()
    last_name = Member.last_name()

    run_sql_script(VIEW_MEMBER_SQL, (first_name, last_name))
    rows = CURSOR.fetchall()
    get_attributes(rows, attributes())

def member_exists(first_name, last_name):
    """ main func to check if a member exists, inner func descriptions below """

    def members_array_id():
        """ add all members in array with a separate member id array """
        member_id = []

        run_sql_script(VIEW_MEMBER_SQL, (first_name, last_name))
        members = CURSOR.fetchall()

        for member in members:
            member_id.append(member[0])

        return members, member_id
    members, member_id = members_array_id()

    def one_member():
        """ check if only 1 hit found """
        one_member = False
        if len(member_id) == 1: one_member = True
        return one_member
    one_member = one_member()

    def plus_member():
        """ check if more than one member with same name and surname, return with id to delete """
        plus_member = False
        id_to_del = None
        if len(member_id) > 1:
            print("More than 1 member found.")
            get_attributes(members, attributes())
            print("Type member's ID to delete. Select %s | " % member_id)
            user_input = input()
            id_to_del = check_input(user_input, member_id)
            dictionary = send_to_dict(members, attributes())
            from_dict_by_id(dictionary, user_input)
            plus_member = True
        return plus_member, id_to_del
    plus_member, id_to_del = plus_member()

    def no_member():
        """ evaluates to True if member not in db """
        no_member = False
        if member_id: no_member = True
        return no_member
    no_member = no_member()

    return one_member, plus_member, id_to_del, no_member

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
