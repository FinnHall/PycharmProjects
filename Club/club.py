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

        self.roll = {}

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

    def list_members(self):
        return [member.name for member in self.members]

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
            writer = csv.writer(file, lineterminator='\n')
            for member in members:
                writer.writerows([[member.name, member.address, member.phone_number]])

    def create_roll(self, date):
        if date not in self.roll.keys():
            self.roll[date] = Roll(self.list_members(), date)

    def main(self):
        os.system('cls')
        for i in range(11):
            print(self.command_list[i])
        command = input('\nCommand: ')
        match command.lower():
            case '1':
                self.ui_list_all_members()
            case '2':
                self.ui_add_member()
            case '3':
                self.ui_remove_member()
            case '4':
                self.ui_update_member_name()
            case '5':
                self.ui_update_member_address()
            case '6':
                self.ui_update_member_number()
            case '7':
                self.ui_member_attendance_date()
            case '8':
                self.ui_attendance_date()
            case '9':
                self.ui_absent_date()
            case '0':
                self.ui_present_date()
            case 'q':
                quit()
            case _:
                self.main()

    def display(self):
        os.system('cls')
        print(f'{self.list_members()} \n')
        for i in range(2):
            print(self.command_list[-1 - i])

    def ui_list_all_members(self):
        self.display()
        command = input('\nCommand: ')
        match command.lower():
            case 'b':
                self.main()
            case 'q':
                quit()

    def ui_add_member(self):
        self.display()
        member_name = input('\nAdd Member Name: ')
        match member_name.lower():
            case 'b':
                self.main()
            case 'q':
                quit()
        member_number = input('Add Member Number: ')
        match member_number.lower():
            case 'b':
                self.main()
            case 'q':
                quit()
        member_address = input('Add Member Address: ')
        match member_address.lower():
            case 'b':
                self.main()
            case 'q':
                quit()
        self.add_member(member_name, member_number, member_address)
        self.ui_add_member()

    def ui_remove_member(self):
        self.display()
        member_name = input('\nRemove Member Name: ')
        match member_name.lower():
            case 'b':
                self.main()
            case 'q':
                quit()
        self.remove_member(member_name)
        self.ui_remove_member()

    def ui_update_member_name(self):
        self.display()
        member_name = input('\nUpdate Member Name: ')
        match member_name.lower():
            case 'b':
                self.main()
            case 'q':
                quit()
        member_new_name = input('Member New Name: ')
        match member_name.lower():
            case 'b':
                self.main()
            case 'q':
                quit()
        self.update_member_name(member_name, member_new_name)
        self.ui_update_member_name()

    def ui_update_member_address(self):
        self.display()
        member_name = input('\nMember Name: ')
        match member_name.lower():
            case 'b':
                self.main()
            case 'q':
                quit()
        member_new_address = input('Update Member Address: ')
        match member_name.lower():
            case 'b':
                self.main()
            case 'q':
                quit()
        self.update_member_address(member_name, member_new_address)
        self.ui_update_member_address()

    def ui_update_member_number(self):
        self.display()
        member_name = input('\nMember Name: ')
        match member_name.lower():
            case 'b':
                self.main()
            case 'q':
                quit()
        member_new_number = input('Update Member Number: ')
        match member_name.lower():
            case 'b':
                self.main()
            case 'q':
                quit()
        self.update_member_phone_number(member_name, member_new_number)
        self.ui_update_member_address()

    def ui_member_attendance_date(self):
        self.display()
        date = input('\nDate: ')
        name = input('\nName: ')
        presence = input('\nPresence: ')
        self.create_roll(date)
        self.roll[date].change_member_presence(name, presence)
        command = input('\nCommand: ')
        match command.lower():
            case 'b':
                self.main()
            case 'q':
                quit()

    def ui_attendance_date(self):
        os.system('cls')
        print('')
        for i in range(2):
            print(self.command_list[-1 - i])
        date = input('\nDate: ')
        self.create_roll(date)
        list_members = self.roll[date].list_member_attendance()
        print('')
        for i in list_members:
            print(i)
        command = input('\nCommand: ')
        match command.lower():
            case 'b':
                self.main()
            case 'q':
                quit()

    def ui_absent_date(self):
        os.system('cls')
        print('')
        for i in range(2):
            print(self.command_list[-1 - i])
        date = input('\nDate: ')
        self.create_roll(date)
        list_absent_members = self.roll[date].list_absent()
        print('')
        for i in list_absent_members:
            print(i)
        command = input('\nCommand: ')
        match command.lower():
            case 'b':
                self.main()
            case 'q':
                quit()

    def ui_present_date(self):
        os.system('cls')
        print('')
        for i in range(2):
            print(self.command_list[-1 - i])
        date = input('\nDate: ')
        self.create_roll(date)
        list_present_members = self.roll[date].list_present()
        print('')
        for i in list_present_members:
            print(i)
        command = input('\nCommand: ')
        match command.lower():
            case 'b':
                self.main()
            case 'q':
                quit()


class Roll:
    def __init__(self, members_list, current_date):
        self.members_list = members_list
        self.date = current_date
        self.attendance = {}
        for i in members_list:
            self.attendance[i] = 'Absent'

    def member_presence(self, member):
        presence = self.attendance[member]
        return presence

    def change_member_presence(self, member, presence):
        self.attendance[member] = presence

    def list_present(self):
        present_list = []
        for member, present in self.attendance.items():
            if present == 'Present':
                present_list.append(member)
        return present_list

    def list_absent(self):
        absent_list = []
        for member, present in self.attendance.items():
            if present == 'Absent':
                absent_list.append(member)
        return absent_list

    def list_member_attendance(self):
        return list(self.attendance.items())


class App(tk.Tk):
    pass


if __name__ == '__main__':
    Club.from_file('people', 'members.csv')
