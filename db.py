import sqlite3 #import sqlite3 library

from members import *
from time_functions import *

def insert_in_db():
    connection = sqlite3.connect('database.db') #connect to db/create new otherwise

    #cursor:  
    #symbol that indicates the cursor / iterator
    #an object used to pinpoint records in a database
    #shows the specific record in the database that is being worked upon 
    cursor = connection.cursor()
    cursor.execute("""  CREATE TABLE IF NOT EXISTS Members
                        (member_id integer primary key autoincrement, 
                        name text, 
                        surname text, 
                        age int, 
                        date text,
                        time text) """)

    member = Member(input("Insert name: "), input("Insert surname: "), int(input("Insert age: ")))

    # ? ? ? -> used as placeholders
    cursor.execute("""  INSERT INTO Members 
                        (name, surname, age, date, time) VALUES (?, ?, ?, ?, ?) """,
                        (member.name, member.surname, member.age, date_dmy, time_hm)) 
    print("Database insert executed at:",time_hm + " on", date_dmy)
    connection.commit() #save changes to the db
    connection.close() #close the db

def update_member():
    print("Member updated")

def delete_member():
    print("Member deleted")
