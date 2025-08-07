#Some comments

# Import modules
import json

# Global variables
file_path = "taskList.json"

task_list = []

#'Add' task function
# Add a new task
def add_task():
    new_task = input("Enter a task: ")
    task_list.append(new_task)
    # task_id = new_task.ge
    # print(new_task, task_id)
    # task_list.append(new_task)
    # print(f"task: '{new_task}' was added (ID: {new_task.index}).")

    with open(file_path, "a") as file:
        json.dump(new_task, file, indent=1000)
        print(f"task: '{new_task}' was added (ID: ).")
        # print(f"json file was created")


def update_task():
    update_task = input("Enter task change: ")


add_task()
print(task_list)
