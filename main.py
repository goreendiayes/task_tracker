#Some comments

# Import modules
import json

# Global variables
file_path = "taskList.json"

task_list = []

#'Add' task function
# Add a new task
def add_task(task):
    new_task = input("Enter a task: ")
    task_list.append(new_task)
    # task_id = new_task.ge
    # print(new_task, task_id)
    # task_list.append(new_task)
    # print(f"task: '{new_task}' was added (ID: {new_task.index}).")

    # with open(file_path, "w", newline="") as file:
    #     json.dump(new_task, file, indent=4)
    #     print(f"task: '{new_task}' was added (ID: ).")
    #     # print(f"json file was created")


def update_task():
    update_task = input("Enter task change: ")


add_new_task = add_task("IDK")
print(task_list)
