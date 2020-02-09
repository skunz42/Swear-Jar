# Sean Kunz
# View

import tkinter as tk
import tkinter.font as tkFont
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

        txt = "Press the listen button!"
        self.updatelbl = tk.Label(self.master, text=txt)
        self.updatelbl.pack(side=tk.BOTTOM)
        #self.updatelbl.place(x=150, y=400)
        self.updatelbl.config(font=("Arial", 18))

        self.database = DB()
        self.speech = Speech(self.database, self.updatelbl)
        self.dt = Donate(self.database)

        self.setupWindow()

        txt = "$" + str("{0:.2f}".format(self.database.getProgress()))
        self.amtlb = tk.Label(self.master, text=txt)
        self.amtlb.pack()
        self.amtlb.place(x=200, y=230)
        self.amtlb.config(font=("Arial", 28, "bold"))

    def setupWindow(self):
        # Titles, etc
        self.master.title('Swear Jar!')
        self.master.geometry("500x400")
        self.master.resizable(0,0)
        self.master.configure(background='white')

        helv36 = tkFont.Font(family='Helvetica', size=14, weight=tkFont.BOLD)

        # Image
        path = "../assets/jar.jpg"
        img = Image.open(path)
        img = img.resize((200,200), Image.ANTIALIAS)
        map = ImageTk.PhotoImage(img)
        mpl = tk.Label(self.master, image=map)
        mpl.image=map
        mpl.pack()
        mpl.place(x=150, y=150)

        # Buttons
        b = tk.Button(self.master, text="Quit", font=helv36, bg='blue', command = lambda : self.quit())
        b.pack()
        b.place(x=25, y=10, height=50, width=100)

        b = tk.Button(self.master, text="Listen", font=helv36, bg='blue', command = lambda : self.speech.listen(self.amtlb))
        b.pack()
        b.place(x=200, y=10, height=50, width=100)

        b = tk.Button(self.master, text="Donate", font = helv36, bg='blue', command = lambda : self.donate())
        b.pack()
        b.place(x=375, y=10, height=50, width=100)

        l = tk.Label(self.master, text="Try these words: [test, shit, hell, ass, damn]")
        l.pack()
        l.place(x=10, y=90)
        l.config(font=("Arial", 18))

    def quit(self):
        self.database.writeDB();
        sys.exit()

    def donate(self):
        self.dt.donate()
        self.database.emptyJar()
        txt = "$" + str("{0:.2f}".format(self.database.getProgress()))
        self.amtlb.config(text=txt)
