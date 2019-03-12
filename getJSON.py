import json


def getJSON(filename):
    with open(filename, 'r') as file:
        contents = file.read()
        return json.loads(contents)
