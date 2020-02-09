# Sean Kunz
# View

import tkinter as tk
import sys

from Speech import Speech
from DB import DB
from Donate import Donate
from PIL import ImageTk, Image

class View(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.database = DB()
        self.speech = Speech(self.database)
        self.dt = Donate(self.database)

        self.setupWindow()

        txt = "$" + str("{0:.2f}".format(self.database.getProgress()))
        self.amtlb = tk.Label(self.master, text=txt)
        self.amtlb.pack()
        self.amtlb.place(x=200, y=200)
        self.amtlb.config(font=("Arial", 28))

    def setupWindow(self):
        # Titles, etc
        self.master.title('Swear Jar!')
        self.master.geometry("500x500")
        self.master.resizable(0,0)

        # Buttons
        b = tk.Button(self.master, text="Quit", command = lambda : self.quit())
        b.pack()
        b.place(x=25, y=10, height=50, width=100)

        b = tk.Button(self.master, text="Listen", command = lambda : self.speech.listen(self.amtlb))
        b.pack()
        b.place(x=200, y=10, height=50, width=100)

        b = tk.Button(self.master, text="Donate", command = lambda : self.donate())
        b.pack()
        b.place(x=375, y=10, height=50, width=100)

        l = tk.Label(self.master, text="Try these words: [test, shit, hell, ass, damn]")
        l.pack()
        l.place(x=60, y=75)
        l.config(font=("Arial", 14))

    def quit(self):
        self.database.writeDB();
        sys.exit()

    def donate(self):
        self.dt.donate()
        self.database.emptyJar()
        txt = "$" + str("{0:.2f}".format(self.database.getProgress()))
        self.amtlb.config(text=txt)
