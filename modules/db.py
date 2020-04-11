#https://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/

#cursor:
#symbol that indicates the cursor / iterator
#an object used to pinpoint records in a database
#shows the specific record in the database that is being worked upon

#cursor -> static variable
#self.cursor -> instance variable
#elements outside methods belong to the class

#used as place holders (?,?,?,?)
#connection.commit() #save changes to the db
#connection.close() #close the db

import sqlite3 #import sqlite3 library
from collections import defaultdict

from members import *
from time_functions import *

from modules.func import quit_or_menu
from modules.func import print_stars
from modules.func import check_input
from modules.func import send_to_dict
from modules.func import from_dict_by_id

from definitions import SHOW_MEMBERS_SQL
from definitions import VIEW_MEMBER_SQL
from definitions import SELECT_ALL_SQL
from definitions import INSERT_SQL
from definitions import DELETE_MEMBER_SQL
from definitions import UPDATE_MEMBER_SQL
from definitions import DELETE_ID_SQL

connection = sqlite3.connect('GYM_DATABASE.db') #connect to db/create new otherwise
cursor = connection.cursor()


def run_sql_script(filename, *args):
    file = open(filename, 'r')
    sql_file = file.read()
    file.close()
    cursor.execute(sql_file, *args)

def attributes(): #get columns description (member_id, first_name, last_name, ecc)
    run_sql_script(SELECT_ALL_SQL)
    return [description[0] for description in cursor.description]

#def to_dict(): #convert members list to dictionary (to do json later)
#needs extra work for every member a nested dictionary
#    run_sql_script(SELECT_ALL_SQL)
#    rows = cursor.fetchall()
#
#    dict_members = dict()
#    arr = []
#    descriptions = attributes()
#
#
#    for i in range(0,len(rows)): dict_members[i] = {}
#
#    for i in range(0, len(dict_members)):
#        for description in descriptions:
#            dict_members[i][description] = None
#    #print(dict_members)
#
#    for i in range(0, len(dict_members)):
#        print(dict_members[i])

def insert_in_db():
    first_name = Member.first_name()
    last_name = Member.last_name()
    phone_number = Member.phone_number()
    email = Member.email()

    run_sql_script(INSERT_SQL, (first_name, last_name, phone_number, email, date_format_dmy(), date_end_membership()))

    connection.commit()
    connection.close()

    print("{0} {1} member added to database on {2} at {3}".format(first_name, last_name, date_format_dmy(), time_format_hm()))

def show_members():
    run_sql_script(SHOW_MEMBERS_SQL)
    description = attributes()
    rows = cursor.fetchall()
    for row in rows:
        for i in range(0, len(description)):
            print("%s: %s" % (description[i], row[i]))
        print("------------------------------------")
    print("Total members: %d" % len(rows))


def update_member():
    first_name = Member.first_name()
    last_name = Member.last_name()

    run_sql_script(update_member, (first_name, last_name))
    connection.commit()
    connection.close()
    print("Member updated")

def view_member_details():
    first_name = Member.first_name()
    last_name = Member.last_name()

    run_sql_script(VIEW_MEMBER_SQL, (first_name, last_name))
    rows = cursor.fetchall()
    descriptions = attributes()
    for row in rows:
        for i in range(0, len(descriptions)):
            print("%s: %s" % (descriptions[i], row[i]))
        print("---------------------------------------")

def member_exists(first_name, last_name):

    def members_array_id():
        member_id = []

        run_sql_script(VIEW_MEMBER_SQL, (first_name, last_name))
        members = cursor.fetchall()

        for member in members:
            member_id.append(member[0])

        return members, member_id
    members, member_id = members_array_id()

    def get_attributes():
        description = attributes()
        print_stars()
        for member in members:
            for i in range(0, len(description)):
                print("%s: %s" % (description[i], member[i]))
            print_stars()

    def one_member():
        one_member = False
        if len(member_id) == 1: one_member = True
        return one_member
    one_member = one_member()

    def plus_member():
        plus_member = False
        if len(member_id) > 1:
            print("More than 1 member found.")
            get_attributes()
            print("Type member's ID to delete. Select %s | " % member_id)
            user_input = input()
            id_to_del = check_input(user_input, member_id)
            dictionary = send_to_dict(members, attributes())
            from_dict_by_id(dictionary, user_input)
            plus_member = True
        return plus_member, id_to_del
    plus_member, id_to_del = plus_member()

    def no_member():
        no_member = False
        if len(member_id) == 0: no_member = True
        return no_member
    no_member = no_member()

    return one_member, plus_member, id_to_del, no_member

def delete_member():
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
        quit_or_menu(user_input = input())

    connection.commit()
    connection.close()

def expired_memberships(): pass
def soon_to_expire(): pass
