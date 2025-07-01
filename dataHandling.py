import os
import json

def get_data_file():
    appdata_dir = os.path.join(os.getenv("APPDATA"), "ADAM")
    os.makedirs(appdata_dir, exist_ok=True)
    return os.path.join(appdata_dir, "data.json")

def saveData(data):
    data_file = get_data_file()
    with open(data_file, "w") as file:
        json.dump(data, file, indent=2)

def fetchData():
    data_file = get_data_file()
    with open(data_file, "r") as file:
        data = json.load(file)
    return data

def restartUser():
    data_file = get_data_file()
    data = {
        "name": "",
        "existing user": False,
        "bg": "#2e2e2e",
        "font": "Consolas",
        "man": {
            "man": "Outputs manual on any given command - 'man [command]'",
            "help": "Outputs all available commands - 'help'",
            "time": "Outputs current time and date - 'time'",
            "search": "Opens default webbrowser with input keywords or url - 'search [keywords/url]'",
            "editor": "Opens a built in basic text editor - 'editor [filepath]'\n(filepath can be left empty to create a new file in documents.\nIf no file is given, it will create a new one)",
            "define": "Outputs definition of given word - 'define [word]'",
            "quote": "Outputs random quote - 'quote'",
            "exit": "Exits A.D.A.M - 'exit'"
        }
    }
    with open(data_file, "w") as file:
        json.dump(data, file, indent=2)
