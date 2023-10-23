# Authors   : Rayan Oukani
# Emails    : roukani@umass.edu
# Spire IDs : 34462508

# This is a starting example. You do NOT need to modify this function
def clear_tasks(list):
  list.clear()

# Create an empty list
to_do_list = []

# Below please implement the add_task, delete_task, and move_task functions
# ----- YOUR CODE STARTS HERE -----

N = 0

def add_task(lst, strng):
    lst.append(strng)
    ack = F"Task successfully added. {int(len(lst))} tasks remaining."
    return ack

def delete_task(lst, strng):
    lst.remove(strng)
    ack = F"Task successfully deleted. {int(len(lst))} tasks remaining."
    return ack

def move_task(lst, from_index, to_index):
    old = lst[from_index]
    lst.pop(from_index)
    lst.insert(to_index,old)

    ack = F"Task '{old}' successfully moved to index {to_index}"
    return ack


# ===== YOUR CODE ENDS HERE =====

# You can use the code below to help test your functions

# Uncomment the following 5 lines (i.e. remove the # characters on each line) to test add_task
print(add_task(to_do_list, 'zybook reading'))
print(add_task(to_do_list, 'do laundry'))
print(add_task(to_do_list, 'cics110 lab 3'))
print(add_task(to_do_list, 'math homework'))
print(add_task(to_do_list, 'grocery shopping'))

# Uncomment the following 2 lines (i.e. remove the # characters on each line) to test delete_task
print(delete_task(to_do_list, 'zybook reading'))
print(delete_task(to_do_list, 'math homework'))

# Uncomment the following 5 lines (i.e. remove the # characters on each line) to test move_task
to_do_list = ['zybook reading', 'do laundry', 'cics110 lab 3', 'math homework', 'grocery shopping']
print(move_task(to_do_list, 2, 0))
print('Current to-do list:', to_do_list, '\n')
print(move_task(to_do_list, 1, 4))
print('Current to-do list:', to_do_list, '\n')