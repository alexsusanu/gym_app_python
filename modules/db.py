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

connection = sqlite3.connect('GYM_DATABASE.db') #connect to db/create new otherwise
cursor = connection.cursor()

sql_create_table = """
                    CREATE TABLE IF NOT EXISTS Members 
                    (
                        MEMBER_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        FIRST_NAME VARCHAR(30) NOT NULL,
                        LAST_NAME VARCHAR(30) NOT NULL,
                        PHONE INTEGER,
                        EMAIL VARCAHR(30),
                        JOINING_DATE DATE,
                        ENDING_DATE DATE 
                    );  
                    """
sql_insert_in_db = """
                    INSERT INTO Members(FIRST_NAME, LAST_NAME, PHONE, EMAIL, JOINING_DATE, ENDING_DATE)
                    VALUES (?, ?, ?, ?, ?, ?)
                    """

sql_show_members = """SELECT FIRST_NAME, LAST_NAME FROM Members"""

   
def create_table():
    cursor.execute(sql_create_table)


def insert_in_db():
    first_name = Member.first_name()
    last_name = Member.last_name()
    phone_number = Member.phone_number()
    email = Member.email()
    args = first_name, last_name, phone_number, email, date_format_dmy(), date_end_membership()
    cursor.execute(sql_insert_in_db, args)
    connection.commit() #save changes to the db
    connection.close() #close the db
    print("{0} {1} member added to database on {2} at {3}".format(first_name, last_name, date_format_dmy(), time_hm))

def show_members():
    print(('%-10s %10s') % ('NAME', 'SURNAME'.ljust(15)))
    print()
    cursor.execute(sql_show_members)
    rows = cursor.fetchall() #fetch one or all
    for row in rows:
        print("%-10s %10s" % (row[0].title(), row[1].title().ljust(15)))
    print()
    print("Total members: %d" % len(rows))

def update_member():
    print("Insert old name: ")
    name = input()

    print("Insert new name: ")
    new_name = input()

    sql = """
            UPDATE Members
            SET FIRST_NAME = ?, LAST_NAME = ?
            WHERE FIRST_NAME = ? AND LAST_NAME = ?
          """
    cursor.execute(sql,(new_name, name))
    connection.commit()
    connection.close()
    print("Member updated")

def view_member_details():
    print("Insert name: ")
    name = input()

    print("Insert surname: ")
    surname = input()

    sql = """
    SELECT * FROM Members
    WHERE name = ?
    AND surname = ?
    """
    cursor.execute(sql, (name, surname))
    print(cursor.fetchall())
    connection.commit()
    connection.close()
    print("Member details")

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
