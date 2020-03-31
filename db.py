#https://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/

#cursor:  
#symbol that indicates the cursor / iterator
#an object used to pinpoint records in a database
#shows the specific record in the database that is being worked upon 

#DB.cursor -> static variable
#self.cursor -> instance variable
#elements outside methods belong to the class

import sqlite3 #import sqlite3 library

from members import *
from time_functions import *

class DB:
    connection = sqlite3.connect('database.db') #connect to db/create new otherwise
    cursor = connection.cursor()

    def insert_in_db():
        DB.cursor.execute("""
                            CREATE TABLE IF NOT EXISTS Members
                            (member_id integer primary key autoincrement, 
                            name text, 
                            surname text, 
                            age int, 
                            date text,
                            time text) 
                        """)

        member = Member(input("Insert name: "), input("Insert surname: "), int(input("Insert age: ")))

        # ? ? ? -> used as placeholders
        DB.cursor.execute("""
                            INSERT INTO Members (name, surname, age, date, time) 
                            VALUES (?, ?, ?, ?, ?) 
                        """,(member.name, member.surname, member.age, date_dmy, time_hm)) 
        print("Database insert executed at:",time_hm + " on", date_dmy)
        DB.connection.commit() #save changes to the db
        DB.connection.close() #close the db

    def show_members():
        DB.connection
        DB.cursor.execute("""   
                            SELECT name
                            FROM Members 
                        """)
        rows = DB.cursor.fetchall() #fetch one or all
        for row in rows:
            print(row)

    def update_member(): 
        print("Member updated")

    def view_member_details():
        print("Member details")

    def delete_member(name): #to add arg when calling
        DB.connection
        sql = """
        DELETE FROM Members
        WHERE name = ?
        """
        DB.cursor.execute(sql, [(name)])                
        DB.connection.commit()
        DB.connection.close()
        print("Member deleted")
