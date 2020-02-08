# Sean Kunz
# Driver

import tkinter as tk
from View import View

class Driver(tk.Frame):
    def __init__(self, master=None):
        #self.database = DB()
        self.v = View(master)
        #self.speech = Speech()
        #self.donate = Donate()

        #self.initialize()

def main():
    root = tk.Tk()
    d = Driver(master=root)
    root.mainloop()
main()
