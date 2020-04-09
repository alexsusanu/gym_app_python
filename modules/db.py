#https://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/

#cursor:  
#symbol that indicates the cursor / iterator
#an object used to pinpoint records in a database
#shows the specific record in the database that is being worked upon 

#cursor -> static variable
#self.cursor -> instance variable
#elements outside methods belong to the class

#used as place holders (?,?,?,?)

import sqlite3 #import sqlite3 library

from members import *
from time_functions import *
from definitions import show_members_sql
from definitions import view_member_sql
from definitions import select_all_sql



connection = sqlite3.connect('GYM_DATABASE.db') #connect to db/create new otherwise
cursor = connection.cursor()

sql_insert_in_db = """
                    INSERT INTO Members(FIRST_NAME, LAST_NAME, PHONE, EMAIL, JOINING_DATE, ENDING_DATE)
                    VALUES (?, ?, ?, ?, ?, ?)
                    """

sql_update_member = """
                    UPDATE Members
                    SET FIRST_NAME = ?, LAST_NAME = ?
                    WHERE FIRST_NAME = ? AND LAST_NAME = ?
                    """


def run_sql_script(filename, *args):
    file = open(filename, 'r')
    sql_file = file.read()
    file.close()
    cursor.execute(sql_file, *args)

  
def attributes():
    run_sql_script(select_all_sql)
    descriptions = [description[0] for description in cursor.description]
    #print(descriptions) 
    #print(len(cursor.description))
    return descriptions

 

def insert_in_db():
    first_name = Member.first_name()
    last_name = Member.last_name()
    phone_number = Member.phone_number()
    email = Member.email()
    args = first_name, last_name, phone_number, email, date_format_dmy(), date_end_membership()
    cursor.execute(sql_insert_in_db, args)
    connection.commit() #save changes to the db
    connection.close() #close the db
    print("{0} {1} member added to database on {2} at {3}".format(first_name, last_name, date_format_dmy(), time_format_hm()))

def show_members():
    print(('%-10s %10s') % ('NAME', 'SURNAME'.ljust(15)))
    print()
    cursor.execute(run_sql_script('sql_scripts/show_members.sql'))
    rows = cursor.fetchall() #fetch one or all
    for row in rows:
        print("%-10s %10s" % (row[0].title(), row[1].title().ljust(15)))
    print()
    print("Total members: %d" % len(rows))

def update_member():
    cursor.execute(sql,(new_name, name))
    connection.commit()
    connection.close()
    print("Member updated")

def view_member_details():
    first_name = Member.first_name()
    last_name = Member.last_name()

    run_sql_script(view_member_sql, (first_name, last_name)) #select all members with the same first and last name
    rows = cursor.fetchall()
    description = attributes() #calling attributes function to get all columns names
    for row in rows:
        for i in range(0, len(description)):
            print("%s: %s" % (description[i], row[i]))
        print("---------------------------------------")

def delete_member(): #to add arg when calling
    print("Insert name to delete: ")
    name = input()

    sql = """
    DELETE FROM Members
    WHERE name = ?
    """
    cursor.execute(sql, [(name)])                
    connection.commit()
    connection.close()
    print("Member deleted")

def expired_memberships(): pass
def soon_to_expire(): pass
