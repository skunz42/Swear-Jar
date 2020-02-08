# Sean Kunz
# View

import tkinter as tk
import sys

class View(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.setupWindow()

    def setupWindow(self):
        # Titles, etc
        self.master.title('Swear Jar!')
        self.master.geometry("500x500")
        self.master.resizable(0,0)

        # Buttons
        b = tk.Button(self.master, text="Quit", command = lambda : self.quit())
        b.pack()
        b.place(x=25, y=10, height=25, width=100)

        b = tk.Button(self.master, text="Donate", command = lambda : self.donate())
        b.pack()
        b.place(x=375, y=10, height=25, width=100)

    def quit(self):
        print(sys.exit())

    def donate(self):
        print(":^)")
