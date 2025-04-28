tasks = []

def create_task(task):
    """Add a new task to the tasks list."""
    tasks.append(task)
    print(f"Task '{task}' added successfully.")

def view_task():
    """Display all tasks."""
    if not tasks:
        print("No tasks available.")
        return
    print("\n--- Your Tasks ---")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def delete_task(tasknumber):
    """Remove a task by its task number."""
    try:
        removed_task = tasks.pop(tasknumber - 1)
        print(f"Task '{removed_task}' removed successfully.")
    except IndexError:
        print("Invalid task number. Please try again.")

while True:
    print("\nEnter 1 for Add Task")
    print("Enter 2 for View Tasks") 
    print("Enter 3 for Remove Task") 
    print("Enter 4 for Quit")
    
    taskk = input("Enter your task number: ")
    
    if taskk == "1":
        task = input("Enter your Task: ")
        create_task(task)
    elif taskk == "2":
        view_task()
    elif taskk == "3":
        tasknumber = input("Enter the task number to remove: ")
        try:
            tasknumber = int(tasknumber)
            delete_task(tasknumber)
        except ValueError:
            print("Invalid input. Please enter a valid task number.")
    elif taskk == "4":
        print("Exiting todo list app...")
        break
    else:
        print("Invalid choice. Please choose a correct option (1, 2, 3, 4).")
