from unittest import TestCase
from member import Member
from club import Roll


class TestRoll(TestCase):

    def setUp(self):
        members = [Member('Guy', 'Guy street', '555-5555'),
                   Member('Dude', 'Dude Avenue', '555-7868'),
                   Member('Person', 'Person Blv', '555-1111'),
                   Member('Pedestrian', 'Pedestrian Road', '555-9283'),
                   Member('Other Guy', 'Other Guy street', '555-3453')]
        current_date = '11/16/23'
        self.roll = Roll(members, current_date)
        self.roll.attendance = {'Guy': True,
                                'Dude': False,
                                'Person': True,
                                'Pedestrian': True,
                                'Other Guy': False}
        # ------------------------------------------------------------------------------------------ #
        members1 = [Member('Fred', '123 St.', '555-4325'),
                    Member('Tilda', 'Lily Road', '555-7567'),
                    Member('Lenny', '3424 S Hello Dr', '555-2374'),
                    Member('Bob', 'Some Road', '555-9425'),
                    Member('Mick', 'The Best St.', '555-2342')]
        current_date1 = '11/16/23'
        self.roll1 = Roll(members1, current_date1)
        self.roll1.attendance = {'Fred': False,
                                 'Tilda': False,
                                 'Lenny': True,
                                 'Bob': False,
                                 'Mick': True}

    def test_member_presence(self):
        self.roll.member_presence('Guy', True)
        self.assertTrue(self.roll.attendance['Guy'])

    def test_list_present(self):
        self.assertEqual(self.roll.list_present(), ['Guy', 'Person', 'Pedestrian'])

    def test_list_absent(self):
        self.assertEqual(self.roll.list_absent(), ['Dude', 'Other Guy'])

    def test_list_member_attendance(self):
        self.assertEqual(self.roll.list_member_attendance(), [('Guy', True), ('Dude', False), ('Person', True),
                                                              ('Pedestrian', True), ('Other Guy', False)])

    def test_member_presence1(self):
        self.roll1.member_presence('Mick', True)
        self.assertTrue(self.roll1.attendance['Mick'])

    def test_list_present1(self):
        self.assertEqual(self.roll1.list_present(), ['Lenny', 'Mick'])

    def test_list_absent1(self):
        self.assertEqual(self.roll1.list_absent(), ['Fred', 'Tilda', 'Bob'])

    def test_list_member_attendance1(self):
        self.assertEqual(self.roll1.list_member_attendance(), [('Fred', False), ('Tilda', False), ('Lenny', True),
                                                               ('Bob', False), ('Mick', True)])
