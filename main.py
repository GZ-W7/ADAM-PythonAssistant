import datetime, webbrowser, os
from tkinter import *
from dataHandling import saveData, fetchData, restartUser

restartUser()
data = fetchData()
print(type(data))
root = Tk()
root.title("Welcome to A.D.A.M")
root.geometry("420x380")
root.resizable(height=False, width=False)
root.config(background=data["bg"])
introText = Label(root, text="----------------------------------------\nA.D.A.M. — A Dumb Assistant Mainly\nVersion 0.1\n----------------------------------------\n\nStatus: Active\nMode: Standby\nModules Loaded: Base Functions\n\nEnter 'help' to list available commands.\n\nUser identification required.\nEnter name:"
                  , font=("Consolas", 12),wraplength=400, padx=10, pady=30, bg=data["bg"], fg="#eeeeee", justify="left")
introText.grid(row=1,column=1)

Label(root, text=">", bg=data["bg"], fg="#eeeeee",font=("Consolas", 12), justify="right").place(x=20,y=300)
name = Entry(root, justify="left", bg=data["bg"], fg="#eeeeee", borderwidth=0).place(x=35,y=304)

"""
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
"""
root.mainloop()