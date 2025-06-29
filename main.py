import datetime, webbrowser, os
from tkinter import *
from tkinter import messagebox
from dataHandling import saveData, fetchData, restartUser

#restartUser()

#Loads all saved data from previous sessions
data = fetchData()

#------------------------------------------
#FUNCTIONS

# Used to clear the window/screen of widgets
#def clearWindow():
#    for i in root.winfo_children():
#        i.destroy()


#INTRODUCTION FUNCTIONS


#Used to confirm your name at the first instance of this being used
def confirmName(event):

    value = entry.get()
    # Initiates a pop up asking to confirm if you are "NAME"
    if messagebox.askyesno(title="Confirm your identity", message=f"Are you {value}?"):
        data["name"] = value
        data["existing user"] = True
        saveData(data)
        newUser.destroy()

# Introduction screen, prompts user for name
def intro():
    global newUser, entry
    newUser = Tk()
    
    #Creates and Styles intro screen
    newUser.title("Welcome to A.D.A.M")
    newUser.geometry("420x380")
    newUser.resizable(height=False, width=False)
    newUser.config(background=data["bg"])


    introText = Label(newUser, text="----------------------------------------\nA.D.A.M. — A Dumb Assistant Mainly\nVersion 0.1\n----------------------------------------\n\nStatus: Active\nMode: Standby\nModules Loaded: Base Functions\n\nEnter 'help' to list available commands.\n\nUser identification required.\nEnter name:"
                    , font=("Consolas", 12),wraplength=400, padx=10, pady=30, bg=data["bg"], fg="#eeeeee", justify="left")
    introText.grid(row=1,column=1)

    inputLabel = Label(newUser, text=">", bg=data["bg"], fg="#eeeeee",font=("Consolas", 12), justify="right")
    inputLabel.place(x=20,y=300)

    entry = Entry(justify="left", bg=data["bg"], fg="#eeeeee", font=("Consolas", 12), borderwidth=0)
    entry.place(x=35,y=303)

    #Allows user to submit name using enter key
    newUser.bind("<Return>", confirmName)

    newUser.mainloop()
    bootScreen()


#MAIN FUNCTIONS

def close(window):
    window.destroy()

def help():
    global helpWindow
    helpWindow = Toplevel()
    helpWindow.title("Help")
    helpWindow.config(background=data["bg"])
    helpWindow.resizable(height=False, width=False)

    text = ("""Available Commands:
────────────────────────────\n
time        - Displays the current system time and date.\n
weather     - Shows local weather information.\n
search      - Performs a web search using your default browser.\n
editor      - Opens a basic built-in text editor.\n
stocks      - Launches a stock market game using real stock data.\n
notes       - Save and view personal notes.\n
define      - Look up dictionary definitions for words.\n
quote       - Display a random quote.""")

    label = Label(helpWindow, text=text, font=("Consolas", 12), padx=10, pady=30, bg=data["bg"], fg="#eeeeee", justify="left")
    label.grid(row=0,column=0)

    btn = Button(helpWindow, text="ok", command=help)
    

def decide(event):
    choice = inputEntry.get().lower()
    inputEntry.delete(0, END)
    if choice == "help":
        help()
    elif choice == "time":
        pass
    elif choice == "weather":
        pass
    elif choice == "search":
        pass
    else:
        messagebox.showerror(message="Requested operation is invalid, please consult 'help' to see valid operations.")


def bootScreen():
    global root, inputEntry

    #Defines main window
    root = Tk()
    root.resizable(height=False,width=False)
    root.title("A.D.A.M")
    root.geometry("384x235")

    bootText = Label(root, text=f"----------------------------------------\nWelcome, {data["name"]}.\n\nSystem status: Online\nCommand interface ready.\n\nType 'help' to view available commands.\n\n")
    bootText.config(font=("Consolas", 12),wraplength=400, padx=10, pady=30, bg=data["bg"], fg="#eeeeee", justify="left")
    bootText.grid(row=1,column=1)

    inputLabel = Label(root, text=">", bg=data["bg"], fg="#eeeeee",font=("Consolas", 12), justify="right")
    inputLabel.place(x=20,y=180)

    inputEntry = Entry(root, justify="left", bg=data["bg"], fg="#eeeeee", font=("Consolas", 12), borderwidth=0)
    inputEntry.place(x=35,y=183)

    inputEntry.bind("<Return>", decide)

    root.mainloop()



#------------------------------------------

if data["existing user"] == False:
    intro()
else:
    bootScreen()

