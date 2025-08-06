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
    print(f"task: '{new_task}' was added.")
    
    # try:
    #     with open(file_path, "w") as file:
    #         json.dump(new_task, file, indent=4)
    #         print(f"json file was created")
    # except Exception:
    #     print("Do nothing")

new_task = add_task()