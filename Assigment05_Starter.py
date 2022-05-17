# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# SBMB,May 17, 2031,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
obj_File = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

dicRow = {"Task": "", "Priority": ""}
objFile = open(obj_File, "w")
objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
lstTable = [dicRow]
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        for row in lstTable:
            print("Task: " + str(row["Task"]) + " Priority: " + str(row["Priority"]))
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        str_task = str(input("What is the Task?"))
        str_priority = str(input("What is the Priority?"))
        # str_priority = str_priority + "\n"
        dicRow = {"Task": str_task, "Priority": str_priority}
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove a item from the list/Table
    elif (strChoice.strip() == '3'):
        str_search = input("What task would you like to delete?")
        for row in lstTable:
            dicRow = row
            if row["Task"].lower() == str_search.lower():
                lstTable.remove(row)
                print("Removed")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open(obj_File, "w")
        for row in lstTable:
            dicRow = row
            objFile.write(dicRow["Task"] + ', ' + dicRow["Priority"] + '\n')
        objFile.close()
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        break  # and Exit the program
