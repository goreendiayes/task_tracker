#Some comments

#Import modules
import json
import datetime

#Global variables
file_path = "taskList.json"

def add_task():
    task_id = 0

    task_list = {}

    task_created = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    
    task_id += 1
    
    task = input("Enter a task: ")
    
    task_list["Task ID"] = str(task_id) #This needs to increment the value
    task_list["Description"] = task #capitalizeME
    task_list["Status"] = "New"
    task_list["createdAt"] = task_created

    
    with open(file_path, "a") as file:
        json.dump(task_list, file, indent=4)
        print(f"Task: '{task}' was added (ID: {task_id}).")
        # print(f"json file was created")


# def update_task():
#     task_updated = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
#     update_task = input("Enter task change: ")

# def delete_task():

new_task = add_task()

