#!/usr/bin/python3
"""
Python script to export data in the JSON format.
"""

import json
import urllib.request

if __name__ == "__main__":
    employee_data = urllib.request.urlopen(
            "https://jsonplaceholder.typicode.com/users/")
    employee_task_data = urllib.request.urlopen(
            "https://jsonplaceholder.typicode.com/todos/")

    employee_data_dict = json.loads(employee_data.read().decode())
    employee_task_data_dict = json.loads(employee_task_data.read().decode())

    employee_tasks = {}  # dictionary to store tasks for each employee

    for employee in employee_data_dict:
        employee_id = employee["id"]
        employee_name = employee["name"]
        username = employee["username"]
        tasks = []

        for task in employee_task_data_dict:
            if task["userId"] == employee_id:
                tasks.append({
                    "username": username,
                    "task": task["title"],
                    "completed": task["completed"]
                })

        employee_tasks[employee_id] = tasks

    filename = "todo_all_employees.json"
    with open(filename, mode="w") as file:
        json.dump(employee_tasks, file)

    # print("Data exported to {}".format(filename))
