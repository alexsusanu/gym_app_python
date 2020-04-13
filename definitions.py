"""
files path
"""
import os
import sqlite3

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) #project root
CREATE_TABLE_SQL = os.path.join(ROOT_DIR, 'sql_scripts/create_table.sql')
SHOW_MEMBERS_SQL = os.path.join(ROOT_DIR, 'sql_scripts/show_members.sql')
VIEW_MEMBER_SQL = os.path.join(ROOT_DIR, 'sql_scripts/view_member.sql')
SELECT_ALL_SQL = os.path.join(ROOT_DIR, 'sql_scripts/select_all.sql')
SELECT_NAME_SQL = os.path.join(ROOT_DIR, 'sql_scripts/select_name.sql')
INSERT_SQL = os.path.join(ROOT_DIR, 'sql_scripts/insert.sql')
DELETE_MEMBER_SQL = os.path.join(ROOT_DIR, 'sql_scripts/delete_member.sql')
UPDATE_MEMBER_SQL = os.path.join(ROOT_DIR, 'sql_scripts/update_member.sql')
UPDATE_ID_SQL = os.path.join(ROOT_DIR, 'sql_scripts/update_id.sql')
DELETE_ID_SQL = os.path.join(ROOT_DIR, 'sql_scripts/delete_id.sql')

CONNECTION = sqlite3.connect('GYM_DATABASE.db') #connect to db/create new otherwise
CURSOR = CONNECTION.cursor()
