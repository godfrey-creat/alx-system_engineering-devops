#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID.
"""
import requests
import sys


def get_todo_list_progress(employee_id):
    """
    Fetches the TODO list progress for a given employee ID.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        tuple: A tuple containing the name of the employee, number of completed tasks,
               total number of tasks, and a list of completed tasks.
    """
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(employee_id)).json()
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()

    completed = [t.get("title") for t in todos if t.get("completed")]
    return user.get("name"), len(completed), len(todos), completed


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])
    name, num_completed, total_tasks,
    completed_tasks = get_todo_list_progress(employee_id)

    print("Employee {} is done with tasks({}/{}):".format(
        name, num_completed, total_tasks))
    for task in completed_tasks:
        print("\t" + task)
