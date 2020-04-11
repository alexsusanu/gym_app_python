#https://docs.python.org/3/library/sqlite3.html

from menu import *
from modules.db import *
from definitions import CREATE_TABLE_SQL

run_sql_script(CREATE_TABLE_SQL)
Menu()
user_input = int(input())
Menu.select(user_input)
