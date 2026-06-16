# ==========================================
# CODSOFT PYTHON INTERNSHIP
# TASK 1 - TO DO LIST APPLICATION
# ==========================================

tasks = []

def show_tasks():
    if len(tasks) == 0:
        print("\nNo tasks available.")
    else:
        print("\n" + "=" * 50)
        print("               YOUR TASK LIST")
        print("=" * 50)

        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

        print("=" * 50)
        print(f"Total Tasks : {len(tasks)}")
        print("=" * 50)

while True:

    print("\n")
    print("=" * 50)
    print("         TO-DO LIST APPLICATION")
    print("=" * 50)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Remove All Tasks")
    print("6. Exit")
    print("=" * 50)

    choice = input("Enter your choice (1-6): ")

    # Add Task
    if choice == "1":
        task = input("\nEnter the task: ")
        tasks.append(task)

        print("\nTask Added Successfully!")
        print(f"Current Number of Tasks: {len(tasks)}")

    # View Tasks
    elif choice == "2":
        show_tasks()

    # Update Task
    elif choice == "3":

        if len(tasks) == 0:
            print("\nNo tasks available to update.")

        else:
            show_tasks()

            try:
                task_number = int(input("\nEnter task number to update: "))

                if 1 <= task_number <= len(tasks):

                    new_task = input("Enter new task name: ")
                    old_task = tasks[task_number - 1]

                    tasks[task_number - 1] = new_task

                    print("\nTask Updated Successfully!")
                    print(f"Old Task : {old_task}")
                    print(f"New Task : {new_task}")

                else:
                    print("\nInvalid Task Number.")

            except ValueError:
                print("\nPlease enter a valid number.")

    # Delete Task
    elif choice == "4":

        if len(tasks) == 0:
            print("\nNo tasks available to delete.")

        else:
            show_tasks()

            try:
                task_number = int(input("\nEnter task number to delete: "))

                if 1 <= task_number <= len(tasks):

                    deleted_task = tasks.pop(task_number - 1)

                    print("\nTask Deleted Successfully!")
                    print(f"Deleted Task : {deleted_task}")

                else:
                    print("\nInvalid Task Number.")

            except ValueError:
                print("\nPlease enter a valid number.")

    # Remove All Tasks
    elif choice == "5":

        if len(tasks) == 0:
            print("\nTask list is already empty.")

        else:
            confirm = input(
                "\nAre you sure you want to remove all tasks? (yes/no): "
            )

            if confirm.lower() == "yes":
                tasks.clear()
                print("\nAll Tasks Removed Successfully!")
            else:
                print("\nOperation Cancelled.")

    # Exit
    elif choice == "6":

        print("\n" + "=" * 50)
        print("Thank You For Using TO-DO LIST APPLICATION")
        print("CODSOFT PYTHON INTERNSHIP - TASK 1")
        print("=" * 50)

        break

    else:
        print("\nInvalid Choice! Please select between 1 and 6.")