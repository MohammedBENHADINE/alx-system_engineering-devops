#!/usr/bin/python3
"""request an API"""
import json
import sys
import urllib.request as fetcher

if __name__ == "__main__":
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
        if (el.get("completed") is True):
            todoDone.append("\t " + el.get("title"))
            done += 1
    print('Employee {} is done with tasks({}/{}):'.format(
        userF["name"], done, len(todosF)))
    print('{}'.format("\n".join(todoDone)))
