#To-Do List Application: Create a text-based to-do list where users can add, remove, and view tasks.

# An empty list to store task
to_do_list = []

# Function to display all task
def view_tasks():
    if not to_do_list:
        print("List is Empty")
    else:
        print("Your List: ")
        for idx, task in enumerate(to_do_list, start=1):
            print(f"{idx}.{task}")

# function to add a task
def add_task():
    task = input("Enter your task: ")
    to_do_list.append(task)
    print(f"'{task}' has been added to your list")

# function to remove a task
def remove_task():
    # Show the tasks first to choose to remove
    view_tasks() 
    try:
        task_number = int(input("Enter the task number to remove: ")) -1
        if 0 <= task_number <= len(to_do_list):
            removed_task = to_do_list.pop(task_number)
            print(f"'{removed_task}' has been removed from your list")
        else:
            print("Invalid Task Number.")
    except ValueError:
        print("Enter a valid number.")

# Function to display the menu and take user input
def menu():
    while True:
        print("\n ***************    To Do List Menu    ***************")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Choose an option(1-4): ")

        if choice == "1":
            view_tasks()
        
        elif choice == "2":
            add_task()

        elif choice == "3":
            remove_task()

        elif choice == "4":
            print("Exiting the To Do List App, have a nice day")
            break
        else:
            print("Invalid Option, please choose again")

menu()
