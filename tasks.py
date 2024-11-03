# Simple To-Do List Manager

# Initialize an empty list to store tasks
tasks = []


def add_task():
    """Function to add a task"""
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added.\n")


def view_tasks():
    """Function to view all tasks"""
    if not tasks:
        print("No tasks to display.\n")
    else:
        print("Here are your tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print()


def delete_task():
    """Function to delete a task by index"""
    view_tasks()
    if tasks:
        try:
            task_num = int(input("Enter the task number to delete: "))
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' deleted.\n")
        except (IndexError, ValueError):
            print("Invalid task number.\n")


def main():
    """Main function to display menu and handle user choices"""
    while True:
        print("To-Do List Manager")
        print("1. Add a Task")
        print("2. View Tasks")
        print("3. Delete a Task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("Exiting To-Do List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
