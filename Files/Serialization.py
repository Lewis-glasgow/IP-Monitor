import json
import os

path = "data.json"

def Load():
    if not os.path.exists(path):
        return []
        
    with open(path, 'r') as file:
        return json.load(file)

def Save(data):
    with open(path, 'w') as file:
        json.dump(data, file)