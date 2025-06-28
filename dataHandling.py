import json

def saveData(data):
    print("hbdsgvjh")
    with open("data.json", "w")as file:
        json.dump(data, file, indent=2)
    print("hbdsgvjh")

def fetchData():
    with open("data.json", "r") as file:
        data = json.load(file)
        
    return data

def restartUser():
    with open("data.json", "w") as file:
        json.dump(("{'name': '', 'existing user': False}"), file, indent = 2)