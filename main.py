import datetime, webbrowser, os, time, re
from tkinter import *
from tkinter import messagebox, filedialog
from dataHandling import saveData, fetchData, restartUser
import ctypes


# Dear anyone who reads this,
# Prepare some bleach for your eyes and I am sorry.

# Checks if data file exists, if not makes folder and file
if not os.path.exists("data\\data.json"):
    os.makedirs("data", exist_ok=True)
    restartUser()

#Loads all saved data from previous sessions
global data
data = fetchData()

#Set app id and change taskbar icon
myAppId = "adam.assistant.py"
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myAppId)


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
    if messagebox.askyesno(title="Confirm identity", message=f"Are you {value}?"):
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

    icon = PhotoImage(file="icon.png")
    newUser.iconphoto(True, icon)

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
man         - brings up the manual on any command (man [command])\n
time        - Displays the current system time and date.\n
weather     - Shows local weather information.\n
search      - Performs a web search using your default browser.\n
editor      - Opens a basic built-in text editor.\n
stocks      - Launches a stock market game using real stock data.\n
notes       - Save and view personal notes.\n
define      - Look up dictionary definitions for words.\n
quote       - Display a random quote.\n
exit        - exits A.D.A.M\n""")

    label = Label(helpWindow, text=text, font=("Consolas", 12), padx=10, pady=30, bg=data["bg"], fg="#eeeeee", justify="left")
    label.grid(row=0,column=0)

    

    btn = Button(helpWindow, text="close", command=lambda: close(helpWindow))
    btn.config(font=(data["font"], 12), bg="#eeeeee", fg="black")
    btn.place(relx=0.46,rely=0.9)

def argError(input):
    messagebox.showerror(title="Syntax Error", message=f"{input[0]}: expected 1 argument, got {len(input)-1}.")

def manWarning(input):
    messagebox.showerror(title="Syntax Error", message=f"Argument given not valid: {input[1]}")
    
def man(input):

    manWindow = Toplevel(root)
    manWindow.title(f"Manual: {input[1]}")
    manWindow.config(background=data["bg"])
    manWindow.resizable(False, False)

    info = Label(manWindow,text=data["man"][input[1]],bg=data["bg"], fg="#eeeeee",font=("Consolas", 12), justify="left", wraplength=300, padx=20, pady=20)
    info.pack()

    btn = Button(manWindow, text="close", command=lambda: close(manWindow))
    btn.config(font=(data["font"], 12), bg="#eeeeee", fg="black")
    btn.pack()

def search(input):
    domain_pattern = re.compile(r"^[\w.-]+\.(com|org|net|io|gov|edu)(/.*)?$")
    #Checks if input begins with protocals
    if input[1].startswith("http://") or input[1].startswith("https://"):
        webbrowser.open(input[1])
    
    #checks if input has any popular top level domains
    
    elif bool(domain_pattern.match(input[1])):
        webbrowser.open(input[1])
    else:
    
        #recreates search terms and opens it in google
        query = ""
        for i in range(1, len(input)):
            query += f" {input[i]}"

        webbrowser.open(f"https://www.google.com/search?q={query}")
    
def saveFile(filepath):
    targetPath  = filepath
    if targetPath == False:
        targetPath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", ".txt"),("Python Files", "*.py"), ("All Files", "*.*")])
    elif targetPath:
        with open(targetPath, "w", encoding="utf-8") as file:
            file.write(textArea.get(1.0, END))
        messagebox.showinfo(title="Saved File", message=f"File saved to {targetPath}")

def editor(input):
    print(input)

    # checks if file was given
    try:
        filepath = input[1]
    except TypeError:
        pass

    print(filepath)

    #defines window and style
    editWindow = Toplevel()
    editWindow.geometry("800x600")
    editWindow.config(bg=data["bg"])
    editWindow.resizable(True, True)

    #defines menu bar and styles
    menubar = Menu(editWindow)
    editWindow.config(menu=menubar)

    fileMenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=fileMenu)
    fileMenu.add_command(label="Save", command=lambda: saveFile(filepath))
    fileMenu.add_command(label="Exit", command=lambda: close(editWindow))

    #defines text widget and style
    global textArea
    textArea = Text(editWindow, wrap=WORD, undo=True, font=(data["font"], 12), fg="#eeeeee", bg=data["bg"])
    textArea.pack(fill=BOTH, expand=True)
    textArea.focus()

    # tries to find file
    if filepath:
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as file:
                textArea.insert(1.0, file.read())
            editWindow.title(f"A.D.A.M File Editor: {os.path.basename(filepath)}")
        else:
            editWindow.title(f"A.D.A.M File Editor: New File {filepath}")
    else:
        editWindow.title("A.D.A.M File Editor: New File")

def currentTime():
    now = datetime.datetime.now()
    formatted_time = now.strftime("%A, %B %d, %Y\n%I:%M:%S %p")

    timeWindow = Toplevel(root)
    timeWindow.title("System Time")
    timeWindow.config(background=data["bg"])
    timeWindow.resizable(False, False)

    label = Label(timeWindow, text=formatted_time, font=("Consolas", 14), bg=data["bg"], fg="#eeeeee", padx=20, pady=30, justify="center")
    label.pack()

    btn = Button(timeWindow, text="close", command=lambda: close(timeWindow))
    btn.config(font=(data["font"], 12), bg="#eeeeee", fg="black")
    btn.pack(pady=(0, 20))

def decide(event):
    choice = inputEntry.get().lower().split(" ")
    inputEntry.delete(0, END)

    if choice[0] == "help":
        help()

    elif choice[0] == "man":
        if len(choice)==2:
            if choice[1] in data["man"]:
                man(choice)
            else:
                manWarning(choice)
        else:
            argError(choice)
            
    elif choice[0] == "time":
        currentTime()

    elif choice[0] == "weather":
        pass

    elif choice[0] == "search":
        search(choice)

    elif choice[0] == "editor":
        editor(choice)

    elif choice[0] == "define":
        pass

    elif choice[0] == "quote":
        pass

    elif choice[0] == "exit":
        close(root)

    else:
        messagebox.showerror(message="Requested command is invalid, please consult 'help' to see valid command.")

def bootScreen():
    global root, inputEntry

    #Defines main window
    root = Tk()
    root.resizable(height=False,width=False)
    root.title("A.D.A.M")
    root.geometry("384x235")

    # Create and set icon for root and all top level windows
    icon = PhotoImage(file="icon.png")
    root.iconphoto(True, icon)

    bootText = Label(root, text=f"----------------------------------------\nWelcome, {data["name"]}.\n\nSystem status: Online\nCommand interface ready.\n\nType 'help' to view available commands.\n\n")
    bootText.config(font=("Consolas", 12),wraplength=400, padx=10, pady=30, bg=data["bg"], fg="#eeeeee", justify="left")
    bootText.grid(row=1,column=1)

    inputLabel = Label(root, text=">", bg=data["bg"], fg="#eeeeee",font=("Consolas", 12), justify="right")
    inputLabel.place(x=20,y=180)

    inputEntry = Entry(root, justify="left", bg=data["bg"], fg="#eeeeee", font=("Consolas", 12), borderwidth=0, width=35)
    inputEntry.place(x=35,y=183)
    inputEntry.focus()

    inputEntry.bind("<Return>", decide)

    root.mainloop()


#------------------------------------------

if data["existing user"] == False:
    intro()
else:
    bootScreen()
