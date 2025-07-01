import json

def saveData(data):
    with open("data\\data.json", "w")as file:
        json.dump(data, file, indent=2)

def fetchData():
    with open("data\\data.json", "r") as file:
        data = json.load(file)
        
    return data

def restartUser():
    data = {
    "name": "",
    "existing user": False,
    "bg": "#2e2e2e",
    "font": "Consolas",
    "man": {
        "man": "Outputs manual on any given command - 'man [command]'",
        "help": "Outputs all available commands - 'help'",
        "time": "Outputs current time and date - 'time'\n",
        "weather": "Outputs current weather, high and low temperatures,\n [NEEDs TO BE FINISHED]",
        "search": "Opens default webbrowser with input keywords or url - 'search [keywords/url]'",
        "editor": "Opens a built in basic text editor - 'editor [filepath]'\n(filepath can be left empty to create a new file in documents.\nIf no file is given, it will create a new one)",
        "define": "Outputs definition of given word - 'define [word]'",
        "quote": "Outputs random quote - 'quote'",
        "exit": "Exits A.D.A.M - 'exit'"
    }
}
    with open("data\\data.json", "w") as file:
        json.dump(data, file, indent = 2)
    pass
