#!/usr/bin/python3
"""request an API and save results into csv"""
import csv
import json
import sys
import urllib.request as fetcher


if __name__ == "__main__":
    userid = str(sys.argv[1])
    endpoint = 'https://jsonplaceholder.typicode.com'
    name_url = '/users/' + str(sys.argv[1])
    todos_url = name_url + '/todos'
    res = fetcher.urlopen(endpoint + name_url)
    user = res.read()
    userF = json.loads(user)
    username = userF.get("name")
    res = fetcher.urlopen(endpoint + todos_url)
    todos = res.read()
    todosF = json.loads(todos)
    with open(userid + ".csv", 'x', newline='') as file:
        writer = csv.writer(file, quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        for el in todosF:
            writer.writerow([
                userid, userF.get("username"),
                str(el.get("completed")),
                el.get("title")
                ])
        file.close()
