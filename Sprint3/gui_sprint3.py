from tkinter import *
from main import *
import random

authorized_employees = {"Joe": "5893023", "Beaman": "1938472", "Faraz": "3948353", "Chris": "395593", "Avery": "6918572"}
x = input("Enter your id number: ")
if (x not in list(authorized_employees.values())):
    print("NO ACCESS")
else:
    paths = {
        'a': {'b': 3, 'c': 4, 'd': 7},
        'b': {'c': 1, 'f': 5},
        'c': {'f': 6, 'd': 2},
        'd': {'e': 3, 'g': 6},
        'e': {'g': 3, 'h': 4},
        'f': {'e': 1, 'h': 8},
        'g': {'h': 2},
        'h': {'g': 2}
    }
    p = random.randint(1, 103)
    listofKeys = list(paths.keys())
    if (p == 1):
        num = random.randint(0, len(paths))
        while (num >= 0):
            num -= 1
            paths.pop(listofKeys[random.randint(0, len(paths) - 1)])



    def click():
        start = StartingPoint.get()
        finish = Destination.get()
        paths = {
            'a': {'b': 3, 'c': 4, 'd': 7},
            'b': {'c': 1, 'f': 5},
            'c': {'f': 6, 'd': 2},
            'd': {'e': 3, 'g': 6},
            'e': {'g': 3, 'h': 4},
            'f': {'e': 1, 'h': 8},
            'g': {'h': 2},
            'h': {'g': 2}
        }

        try:
            optimaldistance, optimalPath = dijkstra(paths, start, finish)


            if(optimaldistance >= 1):
                outputLabel1 = Label(window, text="Optimal Path: " + str(optimalPath), bg="black", fg="white",
                                 font="none 12 bold").grid(row=10, column=0, sticky=W)
                outputLabel2 = Label(window, text="Distance Length: " + str(optimaldistance), bg="black", fg="white",
                                 font="none 12 bold").grid(row=11, column=0, sticky=W)
                outputLabel3 = Label(window, text="Relaunch Program for New Starting/End Location", bg="black", fg="white",
                                     font="none 12 bold").grid(row=12, column=0, sticky=W)

                StartingPoint.config(state=DISABLED)
                Destination.config(state=DISABLED)
                enterButton.config(state=DISABLED)



            else:
                outputLabel1 = Label(window, text="That Path is Not Reachable", bg="black", fg="white",
                                     font="none 12 bold").grid(row=10, column=0, sticky=W)
                outputLabel2 = Label(window, text="Please Relaunch Program and ", bg="black", fg="white",
                                     font="none 12 bold").grid(row=11, column=0, sticky=W)
                outputLabel3 = Label(window, text="Enter a New Starting/End Location",bg="black", fg="white",
                                     font="none 12 bold").grid(row=12, column=0, sticky=W)

                StartingPoint.config(state=DISABLED)
                Destination.config(state=DISABLED)
                enterButton.config(state=DISABLED)
        except:
            optimalPath = NONE
            print(optimalPath)


    # Creating window
    window = Tk()
    window.title("Optimal Path")
    window.configure(background="black")
    window.resizable(width=False, height=False)
    icon = PhotoImage(file='Delivery.png')

    # Setting icon of master window
    window.iconphoto(False, icon)

    # Creating Labels
    Label(window, text="Enter your current position: ", bg="black", fg="white", font="none 12 bold").grid(row=1,
                                                                                                          column=0,
                                                                                                          sticky=W)
    Label(window, text="Enter your destination: ", bg="black", fg="white", font="none 12 bold").grid(row=5, column=0,
                                                                                                     sticky=W)


    # Creating text boxes
    StartingPoint = Entry(window, width=20, bg="white")
    StartingPoint.grid(row=2, column=0, sticky=W)

    Destination = Entry(window, width=20, bg="white")
    Destination.grid(row=6, column=0, sticky=W)


    # Creating Buttons
    enterButton = Button(window, text="Enter", width=6, command=click).grid(row=7, column=0, sticky=W)

    window.mainloop()