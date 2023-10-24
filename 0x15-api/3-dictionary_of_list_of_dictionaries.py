#!/usr/bin/python3
"""request an API and save results into json"""
import json
import sys
import urllib.request as fetcher


if __name__ == "__main__":
    endpoint = 'https://jsonplaceholder.typicode.com'
    result = {}
    for i in range(1, 11):
        name_url = f'/users/{i}'
        todos_url = f'{name_url}/todos'
        with fetcher.urlopen(endpoint + name_url) as res:
            user_data = json.loads(res.read())
        with fetcher.urlopen(endpoint + todos_url) as res:
            todos_data = json.loads(res.read())
        result[str(i)] = [
                {
                    "username": user_data["username"],
                    "task": todo["title"],
                    "completed": todo["completed"]
                }
                for todo in todos_data
            ]
    with open("todo_all_employees.json", 'x') as file:
        file.write(json.dumps(result))
        file.close()
