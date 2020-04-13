from definitions import VIEW_MEMBER_SQL
from definitions import CONNECTION, CURSOR

from modules.class_run_sql import run_sql_script, attributes, get_attributes
from modules.func import check_input, send_to_dict, from_dict_by_id
from members import Member

class MemberFunc():
    """ check member exists or not functions """
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

        self.member_id = []
        run_sql_script(VIEW_MEMBER_SQL, (self.first_name, self.last_name))
        self.members = CURSOR.fetchall()

        for member in self.members:
            self.member_id.append(member[0])

    def already_member(self):
        """ return true/false only if member already """
        already_member = False
        if self.member_id: already_member = True
        return already_member

    def view_matches(self):
        """return True and list if matches found / False otherwise """
        if len(self.member_id) >= 1:
            print("Here are all the matches found")
            get_attributes(self.members, attributes())
            return True
        else:
            return False

    def id_to_del(self):
        """ returns which id from array to delete or update """
        id_to_del = None
        print("Type member's ID to delete or update.")
        print("Select %s | " % self.member_id)
        user_input = input()
        id_to_del = check_input(user_input, self.member_id)
        dictionary = send_to_dict(self.members, attributes())
        print("You selected the following: ")
        from_dict_by_id(dictionary, user_input)
        return id_to_del

    def __call__(self):
        self.already_member()
        self.view_matches()
        self.id_to_del()
