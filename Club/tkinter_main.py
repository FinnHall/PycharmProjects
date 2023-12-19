import tkinter as tk
from update_dialog import UpdateDialog
from club import Club


club = Club.from_file("TSA", 'members.csv')


def get_name(member_record):
    return member_record[0: member_record.find(',')]


def remove_member(event):
    selected = listbox.curselection()
    if len(selected) > 0:
        index = selected[0]
        member_record = listbox.get(index)
        name = get_name(member_record)
        club.remove_member(name)
        listbox_data.set(club.get_members())


def add_member(event):
    dialog = UpdateDialog(window, "Add Member")
    club.add_member(dialog.name, dialog.address, dialog.phone)
    listbox_data.set(club.get_members())


def update_member(event):
    selected = listbox.curselection()
    if len(selected) > 0:
        index = selected[0]
        member_record = listbox.get(index)
        fields = member_record.split(',')
        dialog = UpdateDialog(window, "Update Member", name=fields[0], address=fields[1], phone=fields[2])
        if dialog.name != fields[0]:
            club.change_member_name(fields[0], dialog.name)
        if dialog.address != fields[1]:
            club.update_member_address(dialog.name, dialog.address)
        if dialog.phone != fields[2]:
            club.update_member_phone_number(dialog.name, dialog.phone)
    listbox_data.set(club.get_members())


window = tk.Tk()
window.title(f"Club {club.club_name} Managing Tool")

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

listbox_data = tk.StringVar(window, club.get_members())
listbox = tk.Listbox(window, selectmode='SINGLE', listvariable=listbox_data, font=('Calibri', 36))
frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_add = tk.Button(frm_buttons, text="Add", font=('Calibri', 24))
btn_add.bind("<ButtonRelease>", add_member)
btn_update = tk.Button(frm_buttons, text="Update", font=('Calibri', 24))
btn_update.bind("<ButtonRelease>", update_member)
btn_remove = tk.Button(frm_buttons, text="Remove", font=('Calibri', 24))
btn_remove.bind("<ButtonRelease>", remove_member)

btn_add.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_update.grid(row=1, column=0, sticky="ew", padx=5)
btn_remove.grid(row=2, column=0, sticky="ew", padx=5)
frm_buttons.grid(row=0, column=0, sticky="ns")
listbox.grid(row=0, column=1, sticky="nsew")

window.mainloop()


