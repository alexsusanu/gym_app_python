import os

root_dir = os.path.dirname(os.path.abspath(__file__)) #project root
create_table_sql = os.path.join(root_dir, 'sql_scripts/create_table.sql')
show_members_sql = os.path.join(root_dir, 'sql_scripts/show_members.sql')
view_member_sql = os.path.join(root_dir, 'sql_scripts/view_member.sql')
select_all_sql = os.path.join(root_dir, 'sql_scripts/select_all.sql')
insert_sql = os.path.join(root_dir, 'sql_scripts/insert.sql')
delete_member_sql = os.path.join(root_dir, 'sql_scripts/delete_member.sql')
update_member_sql = os.path.join(root_dir, 'sql_scripts/update_member.sql')
delete_id_sql = os.path.join(root_dir, 'sql_scripts/delete_id.sql')

