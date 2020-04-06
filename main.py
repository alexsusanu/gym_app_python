#https://docs.python.org/3/library/sqlite3.html

from menu import *
from modules.db import *

create_table()
Menu()
user_input = int(input())
Menu.select(user_input)

      
