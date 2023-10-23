#!/usr/bin/python3
"""request an API"""
import json
import sys
import urllib.request as fetcher


endpoint = 'https://jsonplaceholder.typicode.com'
name_url = '/users/' + str(sys.argv[1])
todos_url = name_url + '/todos'
res = fetcher.urlopen(endpoint + name_url)
user = res.read()
userF = json.loads(user)
res = fetcher.urlopen(endpoint + todos_url)
todos = res.read()
todosF = json.loads(todos)
done = 0
todoDone = []
for el in todosF:
    if (el["completed"] is True):
        todoDone.append("\t " + el["title"])
        done += 1
print('Employee {} is done with tasks({}/{})\n{}'.format(
    userF["name"], done, len(todosF),  "\n".join(todoDone)))
