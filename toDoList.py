print("Welcome to the To Do List Project by Gregory Alexandrou.")
print("It's a simple to do list ...")
print("------")
data = []
def showMenu():
    menu = ["1. Add an item to the List", "2. Mark an Item as Done", "3. View the To Do List", "4. Exit"]
    print("Your Options:")
    for task in menu:
        print(task)

def addToList():
    item = input("What is it to be done? ")
    data.append(item)
    print("Added item:", item)
    print(" ")

def showList():
    if len(data) > 0:
        print("Here is the list of the ToDo items:")
        i = 0
        for item in data:
            i = i + 1
            print(str(i) + ".",item)
        print(" ")
    else:
        print("No items in the List.")
        print(" ")

def removeItem():
    if len(data) > 0:
        showList()
        number = int(input("Number of Item to Remove: "))
        print("Removed item: ", data[number - 1])
        data.pop(number - 1)

showMenu()
user_input = "random"
while user_input != "4":
    user_input = input("Enter Your Choice: ")
    if user_input == "1":
        addToList()
    elif user_input == "2":
        removeItem()
    elif user_input == "3":
        showList()
    elif user_input == "4":
        print("Goodbye!")
        print("Terminating ...")
    else:
        print("Enter Valid Option ... ")
        showMenu()
