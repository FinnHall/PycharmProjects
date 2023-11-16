from unittest import TestCase
from club import Club
from member import Member


class TestClub(TestCase):
    def setUp(self):
        members = [Member('Guy', 'Guy street', '555-5555'),
                   Member('Dude', 'Dude Avenue', '555-7868'),
                   Member('Person', 'Person Blv', '555-1111'),
                   Member('Pedestrian', 'Pedestrian Road', '555-9283'),
                   Member('Other Guy', 'Other Guy street', '555-3453')]
        self.people = Club('People Club', members)

    def setUp1(self):
        members = [Member('Fred', '123 St.', '555-4325'),
                   Member('Tilda', 'Lily Road', '555-7567'),
                   Member('Lenny', '3424 S Hello Dr', '555-2374'),
                   Member('Bob', 'Some Road', '555-9425'),
                   Member('Mick', 'The Best St.', '555-2342')]
        self.norms = Club('norms Club', members)

    def test_list_members(self):
        self.setUp()
        self.assertEqual([member.name for member in self.people.list_members()], ['Guy', 'Dude', 'Person',
                                                                                  'Pedestrian', 'Other Guy'])

    def test_list_members1(self):
        self.setUp1()
        self.assertEqual([member.name for member in self.norms.list_members()], ['Fred', 'Tilda', 'Lenny', 'Bob',
                                                                                 'Mick'])

    def test_find_member(self):
        self.setUp()
        self.assertEqual(self.people.find_member('Dude').name, 'Dude')

    def test_find_member1(self):
        self.setUp1()
        self.assertEqual(self.norms.find_member('Lenny').name, 'Lenny')

    def test_add_member(self):
        self.setUp()
        self.people.add_member('Other Dude', 'Other Dude Dr.', '555-2304')
        self.assertEqual(self.people.find_member('Other Dude').name, 'Other Dude')

    def test_add_member1(self):
        self.setUp1()
        self.norms.add_member('Tom', 'Tom Blvd', '555-3456')
        self.assertEqual(self.norms.find_member('Tom').name, 'Tom')

    def test_remove_member(self):
        self.setUp()
        self.people.remove_member('Pedestrian')
        self.assertIsNone(self.people.find_member('Pedestrian'))

    def test_remove_member1(self):
        self.setUp1()
        self.norms.remove_member('Mick')
        self.assertIsNone(self.norms.find_member('Mick'))

    def test_update_member_name(self):
        self.setUp()
        self.people.update_member_name('Person', 'New Guy')
        self.assertIsNone(self.people.find_member('Person'))

    def test_update_member_name1(self):
        self.setUp1()
        self.norms.update_member_name('Tilda', 'Not Tilda')
        self.assertIsNone(self.norms.find_member('Tilda'))

    def test_update_member_address(self):
        self.setUp()
        self.people.update_member_address('Dude', 'New Street')
        self.assertEqual(self.people.find_member('Dude').address, 'New Street')

    def test_update_member_address1(self):
        self.setUp1()
        self.norms.update_member_address('Bob', 'Bob Road')
        self.assertEqual(self.norms.find_member('Bob').address, 'Bob Road')

    def test_update_member_phone_number(self):
        self.setUp()
        self.people.update_member_phone_number('Other Guy', '555-2305')
        self.assertEqual(self.people.find_member('Other Guy').phone_number, '555-2305')

    def test_update_member_phone_number1(self):
        self.setUp1()
        self.norms.update_member_phone_number('Fred', '555-3064')
        self.assertEqual(self.norms.find_member('Fred').phone_number, '555-3064')
