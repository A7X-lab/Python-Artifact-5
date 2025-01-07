# To-Do List App v1.0 Developed by Kirklen Allen
# This app helps users manage a list of tasks by adding, viewing, editing, completing, and removing tasks.

tasks = []  # A global list to store all tasks. Each task is a dictionary with 'task' and 'done' keys.

def display_menu():
    """Display the main menu options to the user."""
    print("\nTo-Do List App v1.0")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Edit Task")
    print("5. Remove Task")
    print("6. Exit")

def add_task():
    """Add a new task to the list."""
    task_desc = input("Enter the task description: ").strip()  # Strip removes leading/trailing whitespace
    tasks.append({"task": task_desc, "done": False})  # Append a dictionary representing the task to the list
    print(f"Task added: {task_desc}")

def view_tasks():
    """View all tasks, showing their description and completion status."""
    if not tasks:  # Check if the task list is empty
        print("\nNo tasks available in the list.")
        return
    print("\nTasks:")
    for i, task in enumerate(tasks, start=1):  # Loop through tasks with an index starting at 1
        status = "✓" if task["done"] else "✗"  # Show ✓ for completed tasks and ✗ for pending tasks
        print(f"{i}. {task['task']} [{status}]")

def mark_task_done():
    """Mark a task as completed."""
    view_tasks()  # Show the list of tasks
    try:
        task_num = int(input("\nEnter the task number to mark as complete: ")) - 1
        if 0 <= task_num < len(tasks):  # Validate the task number
            tasks[task_num]["done"] = True  # Update the 'done' key of the selected task
            print(f"Task marked as complete: {tasks[task_num]['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def edit_task():
    """Edit the description of an existing task."""
    view_tasks()
    try:
        task_num = int(input("\nEnter the task number to edit: ")) - 1
        if 0 <= task_num < len(tasks):  # Validate the task number
            new_desc = input("Enter the new description: ").strip()
            old_desc = tasks[task_num]["task"]  # Store the old task description for reference
            tasks[task_num]["task"] = new_desc  # Update the task description
            print(f"Task updated: '{old_desc}' -> '{new_desc}'")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def remove_task():
    """Remove a task from the list."""
    view_tasks()
    try:
        task_num = int(input("\nEnter the task number to remove: ")) - 1
        if 0 <= task_num < len(tasks):  # Validate the task number
            removed_task = tasks.pop(task_num)  # Remove the task using the pop() method
            print(f"Task removed: {removed_task['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def main():
    """Main program loop that handles user interaction."""
    while True:
        display_menu()  # Show the main menu
        try:
            choice = int(input("\nSelect an option: "))  # Get user's choice
            if choice == 1:
                add_task()
            elif choice == 2:
                view_tasks()
            elif choice == 3:
                mark_task_done()
            elif choice == 4:
                edit_task()
            elif choice == 5:
                remove_task()
            elif choice == 6:
                print("Exiting To-Do List App. Until we meet again! :D")
                break  # Exit the loop and terminate the program
            else:
                print("Invalid choice. Please select a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a valid choice.")

if __name__ == "__main__":
    main()  # Start the application if this script is run directly
