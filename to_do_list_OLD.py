#to_do_list_OLD.py
#Jacen Piatt

# NO INPUT VALIDATION
# POTENTIAL DATA LOSS
# NO INPUT VALIDATION

class ToDoManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def view_tasks(self):
        for idx, task in enumerate(self.tasks, start=1):
            status = "✓" if task["completed"] else "✗"
            print(f"{idx}. {task['task']} [{status}]")

    def save_tasks(self, file_name):
        with open(file_name, "w") as file:
            for task in self.tasks:
                completed = "1" if task["completed"] else "0"
                file.write(f"{task['task']}|{completed}\n")

    def load_tasks(self, file_name):
        with open(file_name, "r") as file:
            self.tasks = []
            for line in file:
                task, completed = line.strip().split("|")
                self.tasks.append({"task": task, "completed": bool(int(completed))})

    def mark_task_as_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
        else:
            print("Invalid task index.")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            print("Invalid task index.")


def main():
    todo_manager = ToDoManager()
    print("Welcome to the To-Do List Manager!")
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Save Tasks")
        print("4. Load Tasks")
        print("5. Mark Task as Completed")
        print("6. Remove Task")
        print("7. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            task = input("Enter a task: ")
            todo_manager.add_task(task)
        elif choice == "2":
            todo_manager.view_tasks()
        elif choice == "3":
            file_name = input("Enter file name to save tasks: ")
            todo_manager.save_tasks(file_name)
        elif choice == "4":
            file_name = input("Enter file name to load tasks: ")
            todo_manager.load_tasks(file_name)
        elif choice == "5":
            index = int(input("Enter the task number to mark as completed: ")) - 1
            todo_manager.mark_task_as_completed(index)
        elif choice == "6":
            index = int(input("Enter the task number to remove: ")) - 1
            todo_manager.remove_task(index)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
