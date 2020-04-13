from definitions import CREATE_TABLE_SQL
from definitions import VIEW_MEMBER_SQL
from definitions import SELECT_ALL_SQL
from definitions import SELECT_NAME_SQL
from definitions import INSERT_SQL
from definitions import DELETE_MEMBER_SQL
from definitions import UPDATE_MEMBER_SQL
from definitions import UPDATE_ID_SQL
from definitions import DELETE_ID_SQL
from definitions import CONNECTION, CURSOR
from definitions import sqlite3

from modules.func import print_stars
from members import Member
from time_functions import date, date_30, time_imp

def run_sql_script(filename, *args):
    """ execute sql files """
    file = open(filename, 'r')
    sql_file = file.read()
    file.close()
    CURSOR.execute(sql_file, *args)

def attributes(): 
    """ get column description from sql db, id name surname ecc """
    run_sql_script(SELECT_ALL_SQL)
    return [description[0] for description in CURSOR.description]

def get_attributes(arr, att):
    """ pair column description/attributes with values """
    print_stars()
    for elm in arr:
        for i, element in enumerate(att):
            print("%s: %s" % (element, elm[i]))
        print_stars()

def run_insert():
    (first_name, last_name, phone_number, email) = Member.ask_details()
    run_sql_script(INSERT_SQL, (first_name, last_name, phone_number, email, date, date_30))
    print("{0} {1} adding to database on {2} at {3}".format(first_name, last_name, date, time_imp()))

def run_select_all():
    run_sql_script(SELECT_ALL_SQL)
    rows = CURSOR.fetchall()
    get_attributes(rows, attributes())

def attr_name():
    run_sql_script(SELECT_ALL_SQL)
    desc = [description[0] for description in CURSOR.description]
    return desc[1], desc[2]

def run_select_name():
    run_sql_script(SELECT_NAME_SQL)
    rows = CURSOR.fetchall()
    att = attr_name()
    for row in rows:
        for i, element in enumerate(att):
            print("%s: %s" % (element, row[i])) 
        print("\n")
    print("Total members %d" % len(rows))

def run_update(old_first, old_last, id_to_del):
        (new_first_name, new_last_name, new_phone_number, new_email) = Member.ask_details()
        run_sql_script(UPDATE_ID_SQL, (new_first_name, new_last_name, new_phone_number, new_email, old_first, old_last, id_to_del))
        print("{0} {1} member updated to database on {2} at {3}".format(new_first_name, new_last_name, date, time_imp()))

def run_view(first_name, last_name):
    run_sql_script(VIEW_MEMBER_SQL, (first_name, last_name))
    rows = CURSOR.fetchall()
    get_attributes(rows, attributes())

def run_del(id_to_del):
    run_sql_script(DELETE_ID_SQL, (id_to_del))
    rows = CURSOR.fetchall()
