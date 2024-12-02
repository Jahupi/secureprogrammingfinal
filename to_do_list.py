#to_do_list.py
#jacen piatt

class ToDoManager:
    def __init__(self):
        #initialize the list
        self.tasks = []

    def add_task(self, task):
        #add a task to the list
        #input validation so tasks isn't empty
        if not task.strip():
            print("Task can't be empty...")
            return
        self.tasks.append({"task": task, "completed": False})

    def view_tasks(self):
        #return a list of tasks with their status
        #message if there aren't any tasks to see
        if not self.tasks:
            print("No tasks avaliable to view")
            return
        for idx, task in enumerate(self.tasks, start=1):
            status = "✓" if task["completed"] else "✗"
            print(f"{idx}. {task['task']} [{status}]")

    def save_tasks(self, file_name):
        #save tasks to a file
        #input validation for file name
        if not file_name.strip():
            print("File name cannot be empty...")
            return
        try:
            with open(file_name, "w") as file:
                for task in self.tasks:
                    completed = "1" if task["completed"] else "0"
                    file.write(f"{task['task']}|{completed}\n")
            print("Tasks have been saved")
        except Exception as e:
            print(f"Error saving tasks: {e}")

    def load_tasks(self, file_name):
        #load tasks from a file
        #input validation for loading file
        if not file_name.strip():
            print("File name can't be empty...")
            return
        try:
            with open(file_name, "r") as file:
                self.tasks = []
                for line in file:
                    task, completed = line.strip().split("|")
                    self.tasks.append({"task": task, "completed": bool(int(completed))})
            print("Tasks have been loaded")
        except FileNotFoundError:
            print("File wasn't found. Make sure to check your file name.")
        except Exception as e:
            print(f"Error loading tasks: {e}")

    def mark_task_as_completed(self, index):
        #mark a task as completed
        if not self.tasks:
            print("No tasks to mark as completed.")
            return
        if not (0 <= index < len(self.tasks)):
            print("Invalid task number")
            return
        self.tasks[index]["completed"] = True
        print(f"Task {index + 1} marked as completed")

    def remove_task(self, index):
        #removes a task from list
        if not self.tasks:
            print("No tasks to remove.")
            return
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f"Task '{removed_task['task']}' removed.")
        else:
            print("Invalid task number. Please enter a valid number.")

def main():
    todo_manager = ToDoManager()
    print("Welcome to the To-Do List Manager!")
    #catch entire loop in a tryexcept in case of the worst
    try:
        while True:
            print("\nOptions:")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Save Tasks")
            print("4. Load Tasks")
            print("5. Mark Task as Completed")
            print("6. Remove Task")
            print("7. Exit")

            choice = input("Choose an option: ").strip()
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
                #catch invalid numbers
                try:
                    index = int(input("Enter the task number to mark as completed: ")) - 1
                    todo_manager.mark_task_as_completed(index)
                except ValueError:
                    print("Invalid number, please try again")
            elif choice == "6":
                #catch invalid numbers
                try:
                    index = int(input("Enter the task number to remove: ")) - 1
                    todo_manager.remove_task(index)
                except ValueError:
                    print("Invalid number, please try again")
            elif choice == "7":
                #ask if people want to save their tasks before exiting to prevent data loss
                try:
                    save_before_exit = input("Do you want to save your tasks before you exit? (y/n): ").strip().lower()
                    if save_before_exit = "y":
                        file_name = input("Enter file name to save tasks to: ")
                        todo_manager.save_tasks(file_name)
                except Exception as e:
                    print(f"An error occurred while saving: {e}")
                print("Goodbye!")
                break
            else:
                print("Invalid option. Try again.")
    except Exception as e:
        print(f"An unexpected error occured: {e}")
        
if __name__ == "__main__":
    main()
