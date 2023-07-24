#!/usr/bin/python3
"""
a Python script that, using a REST API,
for a given employee ID,
returns information about his/her TODO list progress.
"""

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
    for i in employee_task_data_dict:
        if i["completed"] is True:
            completed_tasks.append(i)
            task_done_count += 1
        total_tasks += 1

    EMPLOYEE_NAME = employee_data_dict["name"]

    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME,
        task_done_count,
        total_tasks))

    """
    for i in employee_task_data_dict:
        if i["completed"] is True:
            print("\t{}".format(i["title"]))
    """

    for i in completed_tasks:
        print("\t {}".format(i["title"]))
