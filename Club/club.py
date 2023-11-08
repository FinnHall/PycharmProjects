from member import Member
import csv


class Club:
    def __init__(self, club_name, members, filename=None):
        self.club_name = club_name
        self.members = members
        self.filename = filename

    def list_members(self):
        return self.members

    def find_member(self, name):
        for i in self.members:
            if i.name == name:
                return i

    def add_member(self, name, address, phone_number):
        self.members.append(Member(name, address, phone_number))
        self._save_members()

    def remove_member(self, name):
        self.members.remove(self.find_member(name))
        self._save_members()

    def update_member_name(self, name, new_name):
        self.find_member(name)._name = new_name
        self._save_members()

    def update_member_address(self, name, new_address):
        self.find_member(name)._address = new_address
        self._save_members()

    def update_member_phone_number(self, name, new_phone_number):
        self.find_member(name)._phone_number = new_phone_number
        self._save_members()

    @classmethod
    def from_file(cls, club_name, filename):
        members = cls.load_members(filename)
        return cls(club_name, members, filename)

    def _save_members(self):
        if self.filename:
            Club.write_members(self.filename, self.members)

    @staticmethod
    def load_members(filename):
        members = []
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                members.append(Member(row[0], row[1], row[2]))
        return members

    @staticmethod
    def write_members(filename, members):
        with open(filename, 'w') as file:
            writer = csv.writer(file)
            for member in members:
                writer.writerows([member.name, member.address, member.phone_number])
