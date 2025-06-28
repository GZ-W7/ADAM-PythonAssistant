import datetime, webbrowser, os
from dataHandling import saveData, fetchData

data = fetchData()
print(data)
if data.get("existing user") == True:
    pass
else:
    print("Hello, I am A Dumb Assistant Mainly or ADAM. I am able to...")
    print("To start, what is your name?:")
    
    confirm = "n"

    while confirm not in ("y", "") :
        name = input(" \n - ")
        confirm = input(f"Are you {name}? Y/n \n - ").lower().strip()
        print(confirm)
    
    data["name"] = f"{name}"
    data["existing user"] = True
    saveData(data)
    