# Sean Kunz
# Donate

import paypalrestsdk
import webbrowser
import tkinter as tk

from DB import DB

class Donate:
    def __init__(self, dbse):
        self.weburl = "https://www.paypal.com/fundraiser/112574644767835624/charity/14505"
        self.amt = 0.0
        self.db = dbse

    def donate(self):
        self.amt = self.db.getProgress()
        r = tk.Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(self.amt)
        r.update()
        r.destroy()
        webbrowser.open(self.weburl)
