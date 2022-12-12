import os
import time

# Set empty list
myList = []

# Clear screen function
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# Display list function
def view_list():
  i = 1
  for item in myList:
      print(f"{i}) {item}")
      i += 1

print("TO DO LIST MANAGER 📝")
print()

while True:
  command = input("Do you want to view, add to or edit your to do list? ")
  if command.lower() == 'view':
    cls()
    if not myList:
      print("You do not have anything on your list")
      print()
    else:
      print("Here's what you have on your to do list currently: ")
      view_list()
      print()
  elif command.lower() == 'add':
    print()
    item = input("What would you like to add to the list? ")
    myList.append(item)
    cls()
    print("Here's what you have on your list so far: ")
    view_list()
    print()
  elif command.lower() == 'edit':
    remove_item = input("What would you like to remove from the list? ")
    for task in myList:
      if task == remove_item:
        myList.remove(task)
      else:
        print()
        print("Invalid entry")
        time.sleep(2)
        break
    cls()
    print("Here's what you have on your to do list currently: ")
    view_list()
    print()
  else:
    print('Please enter a valid command')
    print()
    continue