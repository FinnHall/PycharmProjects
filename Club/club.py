from member import Member
import csv
import os
import tkinter as tk
from tkinter import ttk


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


class Roll:
    def __init__(self, members_list, current_date):
        self.members_list = members_list
        self.date = current_date
        self.attendance = {}

    def member_presence(self, member, presence):
        self.attendance[member] = presence

    def list_present(self):
        present_list = []
        for key in self.attendance.keys():
            if self.attendance[key]:
                present_list.append(key)
        return present_list

    def list_absent(self):
        absent_list = []
        for key in self.attendance.keys():
            if not self.attendance[key]:
                absent_list.append(key)
        return absent_list

    def list_member_attendance(self):
        return list(self.attendance.items())


class App(tk.Tk):
    pass


class Terminal:
    def __init__(self):
        self.club = Club.from_file('People', 'members.csv')
        self.command_list = ['1) List all members',
                             '2) Add a member',
                             '3) Remove a member',
                             "4) Update a member's name",
                             "5) Update a member's address",
                             "6) Update a member's phone number",
                             '7) Members attendance on specific date',
                             '8) Date attendance',
                             '9) Date absent members',
                             '0) Date present members',
                             'Q) Quit',
                             'B) Back']
        self.main()

    def main(self):
        os.system('cls')
        for i in range(10):
            print(self.command_list[i])
        command = input('\nCommand: ')
        match command.lower():
            case '1':
                self.list_all_members()
            case '2':
                self.add_member()
            case '3':
                self.remove_member()
            case '4':
                self.update_member_name()
            case '5':
                self.update_member_address()
            case '6':
                self.update_member_number()
            case '7':
                self.member_attendance_date()
            case '8':
                self.update_member_number()
            case '9':
                self.add_member()
            case '0':
                self.add_member()
            case 'q':
                self.add_member()
            case _:
                self.main()

    @staticmethod
    def display(function):
        os.system('cls')
        print()
        pass

    def list_all_members(self):
        os.system('cls')
        print(self.club.list_members())
        for i in self.command_list[-2]:
            print(i)
        input('\nCommand: ')

    def add_member(self):
        pass

    def remove_member(self):
        pass

    def update_member_name(self):
        pass

    def update_member_address(self):
        pass

    def update_member_number(self):
        pass

    def member_attendance_date(self):
        pass

    def update_member_number(self):
        pass

if __name__ == '__main__':
    Terminal()
