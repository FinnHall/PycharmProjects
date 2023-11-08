from member import Member

with open('members.csv', 'r') as f:
    lines_members_csv = f.readlines()
lists_of_members = []
for i in lines_members_csv:
    attribute = i.split(',')
    lists_of_members.append(Member(attribute[0], attribute[1], attribute[2][:-1]))
