
def load_booklist():
    #load the file data into a list
    list = []
    with open('booklist.txt', 'r') as booklist_file:
        row = booklist_file.read().splitlines()
    for i in row:
        list.append(tuple(i.split(',')))
    return list


print(load_booklist())

