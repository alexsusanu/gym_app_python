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

from definitions import show_members_sql
from definitions import view_member_sql
from definitions import select_all_sql
from definitions import insert_sql
from definitions import delete_member_sql
from definitions import update_member_sql

#quit = ('q', 'Q', 'Quit', 'quit', 'QUIT')

connection = sqlite3.connect('GYM_DATABASE.db') #connect to db/create new otherwise
cursor = connection.cursor()


def run_sql_script(filename, *args):
    file = open(filename, 'r')
    sql_file = file.read()
    file.close()
    cursor.execute(sql_file, *args)

def attributes(): #get columns description (member_id, first_name, last_name, ecc)
    run_sql_script(select_all_sql)
    return [description[0] for description in cursor.description]

#def to_dict(): #convert members list to dictionary (to do json later)
#needs extra work for every member a nested dictionary
#    run_sql_script(select_all_sql)
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

    run_sql_script(insert_sql, (first_name, last_name, phone_number, email, date_format_dmy(), date_end_membership()))

    connection.commit()
    connection.close()

    print("{0} {1} member added to database on {2} at {3}".format(first_name, last_name, date_format_dmy(), time_format_hm()))

def show_members():
    run_sql_script(show_members_sql)
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
    member
    connection.commit()
    connection.close()
    print("Member updated")

def view_member_details():
    first_name = Member.first_name()
    last_name = Member.last_name()

    run_sql_script(view_member_sql, (first_name, last_name))
    rows = cursor.fetchall()
    descriptions = attributes()
    for row in rows:
        for i in range(0, len(descriptions)):
            print("%s: %s" % (descriptions[i], row[i]))
        print("---------------------------------------")

def member_exists(first_name, last_name):
    description = attributes()

    def members_array_id():
        members_array = []
        member_id = []

        run_sql_script(view_member_sql, (first_name, last_name))
        members = cursor.fetchall()

        for member in members:
            member_id.append(member[0])
        return members, member_id
    members, member_id = members_array_id()

    def get_attributes():    
        print_stars()
        for member in members:
            for i in range(0, len(description)):
                print("%s: %s" % (description[i], member[i]))
            print_stars()

    def one_member():
        one_member = False
        if len(member_id) == 1 : one_member = True
        return one_member
    one_member = one_member()    

    def plus_member():
        if len(member_id) > 1:
            print("More than 1 member found.")
            get_attributes()
            print("Type member's ID to delete. Select %s | " % member_id, end=" ")
            user_input = input()
            check_input(user_input, member_id)
    plus_member = plus_member()

    def no_member():
        no_member = False
        if len(member_id) == 0 : no_member = True
        return no_member
    no_member = no_member()

def delete_member():

    first_name = Member.first_name()
    last_name = Member.last_name()
    print_stars()
 
    member_exists(first_name, last_name)
     
    #run_sql_script(delete_member_sql, (first_name, last_name))
    #connection.commit()
    #connection.close()

def expired_memberships(): pass
def soon_to_expire(): pass
