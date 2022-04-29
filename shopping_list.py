import os


# Make a list to hold our items
todo_list = []


# Funtion Definitions
def showHelp():
    clearScreen()
    print("Todo Application. What shall we get done today?")
    print("Enter HELP to see this screen again")
    print("Enter SHOW to see the current list")
    print("Enter LOAD to load the previous list")
    print("Enter SAVE to save the current list")
    print("Enter CLEAR to clear the list")
    print("Enter DONE to exit the program")


def clearScreen():
    os.system("cls" if os.name == 'nt' else 'clear')


def showList():
    clearScreen()
    print("Here's your list:")

    for index, item in enumerate(todo_list, start = 1):
        print("{}. {}".format(index, item))

    print("-" * 15)


def addItem(newItem):
    clearScreen()
    
    if len(todo_list): # if there is something in the todolist
        position = input("Where should I add {}? \n"
                "Press ENTER to add to the end of the list\n"
                ">>> ".format(newItem))
    else:
        position = 0

    try:
        position = abs(int(position))
    except ValueError:
        position = None

    if position is not None:
        todo_list.insert(position-1, newItem)
    else:
        todo_list.append(newItem)
    
    showList()
    print("{} was added to the list.".format(newItem))


def removeItem():
    showList()
    
    removed_item = input("What would you like to remove?\n"
            ">>> ")
    try:
        todo_list.remove(removed_item)
    except ValueError:
        pass
    
    showList()

    print("{} was successfully removed from the list.".format(removed_item))

def saveList():
    file = open('todo_list.txt', 'w', newline='\r\n')
    for item in todo_list:
        file.write(item + '\n')
    print("Your list was sucessfully saved.")

    file.close()


def loadList():
    file = open('todo_list.txt', 'r', newline='\r\n').read().splitlines()
    for item in file:
       todo_list.append(item)
    
    showList()


def clearList():
    todo_list.clear()
    showList()
    print("The list was cleared")


# Main Loop
def main():
    showHelp()
    while True:
        newItem = input(">>>  ")
        if newItem.upper() == 'HELP':
            showHelp()
            continue
        elif newItem.upper() == 'SHOW':
            showList()
            continue
        elif newItem.upper() == 'DONE':
            break
        elif newItem.upper() == 'SAVE':
            saveList()
            continue
        elif newItem.upper() == 'LOAD':
            loadList()
            continue
        elif newItem.upper() == 'REMOVE':
            removeItem()
            continue
        elif newItem.upper() == 'CLEAR':
            clearList()
            continue
        addItem(newItem)
    showList()


# And. here. we. go !
main()
# Make a list to hold our items
todo_list = []


# Funtion Definitions
def showHelp():
    clearScreen()
    print("Welcome to the Todo List. What shall we get today?")
    print("Enter HELP to see this screen again")
    print("Enter SHOW to see the current list")
    print("Enter LOAD to load the previous list")
    print("Enter SAVE to save the current list")
    print("Enter CLEAR to clear the list")
    print("Enter DONE to exit the program")


def clearScreen():
    os.system("cls" if os.name == 'nt' else 'clear')


def showList():
    clearScreen()
    print("Here's your list:")

    for index, item in enumerate(todo_list, start = 1):
        print("{}. {}".format(index, item))

    print("-" * 15)


def addItem(newItem):
    clearScreen()
    
    if len(todo_list): # if there is something in the todo list
        position = input("Where should I add {}? \n"
                "Press ENTER to add to the end of the list\n"
                ">>> ".format(newItem))
    else:
        position = 0

    try:
        position = abs(int(position))
    except ValueError:
        position = None

    if position is not None:
        todo_list.insert(position-1, newItem)
    else:
        todo_list.append(newItem)
    
    showList()
    print("{} was added to the list.".format(newItem))


def removeItem():
    showList()
    
    removed_item = input("What would you like to remove?\n"
            ">>> ")
    try:
        todo_list.remove(removed_item)
    except ValueError:
        pass
    
    showList()

    print("{} was successfully removed from the list.".format(removed_item))

def saveList():
    file = open('shopping_list.txt', 'w', newline='\r\n')
    for item in todo_list:
        file.write(item + '\n')
    print("Your list was sucessfully saved.")

    file.close()


def loadList():
    file = open('todo_list.txt', 'r', newline='\r\n').read().splitlines()
    for item in file:
       todo_list.append(item)
    
    showList()


def clearList():
    todo_list.clear()
    showList()
    print("The list was cleared")


# Main Loop for the Application
def main():
    showHelp()
    while True:
        newItem = input(">>>  ")
        if newItem.upper() == 'HELP':
            showHelp()
            continue
        elif newItem.upper() == 'SHOW':
            showList()
            continue
        elif newItem.upper() == 'DONE':
            break
        elif newItem.upper() == 'SAVE':
            saveList()
            continue
        elif newItem.upper() == 'LOAD':
            loadList()
            continue
        elif newItem.upper() == 'REMOVE':
            removeItem()
            continue
        elif newItem.upper() == 'CLEAR':
            clearList()
            continue
        addItem(newItem)
    showList()


# And. here. we. go !
main()