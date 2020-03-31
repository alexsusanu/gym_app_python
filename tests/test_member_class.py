import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from members import Member

class TestMemberClass(unittest.TestCase):
    def test_member_params(self):
        name = 'john'
        surname = "smith"
        age = 714

        self.assertIsInstance(name, str, "Not a string")
        self.assertIsInstance(surname, str)
        self.assertIsInstance(age, int)

unittest.main()
    
