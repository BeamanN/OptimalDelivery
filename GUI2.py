from tkinter import *
from dijsktra import *
import random 

authorized_employees = {"Joe":"5893023","Beaman":"4891042","Faraz":"3948353","Chris":"395593"}
x = input("Enter your id number: ")
if (x not in list(authorized_employees.values())):
    print("NO ACCESS")
else:
    paths = {
        'a': {'b':3,'c':4, 'd':7},
        'b': {'c':1,'f':5},
        'c': {'f':6,'d':2},
        'd': {'e':3,'g':6},
        'e': {'g':3,'h':4},
        'f': {'e':1,'h':8},
        'g': {'h':2},
        'h': {'g':2}
    }
    p = random.randint(1, 103)
    listofKeys = list(paths.keys())
    if (p == 1):
        num = random.randint(0, len(paths))
        while(num >= 0):
            num -= 1
            paths.pop(listofKeys[random.randint(0,len(paths)-1)])

    def click():
        start = StartingPoint.get()
        finish = Destination.get()
        try:
            optimalPath = dijkstra(paths,start,finish)
            print(optimalPath)
        except:
            optimalPath = NONE
            print(optimalPath)
        

    #Creating window 
    window = Tk()
    window.title("Optimal Path")
    window.configure(background = "black")

    #Creating Labels
    Label (window, text = "Enter your current position: ", bg = "black", fg = "white", font = "none 12 bold").grid(row = 1, column = 0, sticky = W)
    Label (window, text = "Enter your destination: ", bg = "black", fg = "white", font = "none 12 bold").grid(row = 5, column = 0, sticky = W)
    Label (window, text = "Optimal Path: ", bg = "black", fg = "white", font = "none 12 bold").grid(row = 10, column = 0, sticky = W)

    #Creating text boxes
    StartingPoint = Entry(window, width = 20, bg = "white")
    StartingPoint.grid(row = 2, column = 0, sticky = W)

    Destination = Entry(window, width = 20, bg = "white")
    Destination.grid(row = 6, column = 0, sticky = W)

    Destination = Entry(window, width = 20, bg = "white")
    Destination.grid(row = 11, column = 0, sticky = W)

    #Creating Buttons
    Button(window,text = "Enter", width = 6, command = click).grid(row = 3, column = 0, sticky = W)

    window.mainloop()