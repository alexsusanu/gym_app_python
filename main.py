#https://docs.python.org/3/library/sqlite3.html

from menu import *
from modules.db import *
from definitions import create_table_sql

run_sql_script(create_table_sql)
#attributes()
Menu()
user_input = int(input())
Menu.select(user_input)

      
