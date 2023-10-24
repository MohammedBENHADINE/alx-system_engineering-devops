#!/usr/bin/python3
"""request an API and save results into json"""
import json
import sys
import urllib.request as fetcher


if __name__ == "__main__":
    userid = str(sys.argv[1])
    endpoint = 'https://jsonplaceholder.typicode.com'
    name_url = f'/users/{userid}'
    todos_url = f'{name_url}/todos'

    with fetcher.urlopen(endpoint + name_url) as res:
        user_data = json.loads(res.read())
    with fetcher.urlopen(endpoint + todos_url) as res:
        todos_data = json.loads(res.read())

    result = {
        userid: [
            {
                "task": todo["title"],
                "completed": todo["completed"],
                "username": user_data["username"]
            }
            for todo in todos_data
        ]
    }
    with open(f'{userid}.json', 'x') as file:
        file.write(json.dumps(result))
        file.close()
