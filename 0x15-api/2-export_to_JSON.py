#!/usr/bin/python3
"""extend Python script to export data in the JSON format."""

import json
import sys
import urllib.request

if __name__ == "__main__":
    employee_ID = sys.argv[1]

    employee_data = urllib.request.urlopen(
        "https://jsonplaceholder.typicode.com/users/{}/".format(
            employee_ID))
    employee_tasks = urllib.request.urlopen(
        "https://jsonplaceholder.typicode.com/users/{}/todos/".format(
            employee_ID))

    employee_data_dict = json.loads(employee_data.read().decode())
    employee_task_data_dict = json.loads(employee_tasks.read().decode())

    task_done_count = 0  # counter for tasks done
    total_tasks = 0  # counter for all tasks
    completed_tasks = []  # list to contain completed tasks
    for task in employee_task_data_dict:
        if task["completed"] is True:
            completed_tasks.append(task)
            task_done_count += 1
        total_tasks += 1

    EMPLOYEE_NAME = employee_data_dict["name"]
    USERNAME = employee_data_dict["username"]
    USER_ID = employee_data_dict["id"]

    data = {
        USER_ID: [
            {
                "task": task["title"],
                "completed": task["completed"],
                "username": USERNAME
            }
            for task in employee_task_data_dict  # completed_tasks
        ]
    }

    filename = "{}.json".format(USER_ID)
    with open(filename, mode="w") as file:
        json.dump(data, file)
