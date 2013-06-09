#! /usr/bin/env python

from Tkinter import *
import ttk
from ttk import *

def alert(alert_text):
    root = Tk()
    root.title("File Compare and Move")
    root.resizable(FALSE,FALSE)
    
    mainframe = ttk.Frame(root, padding="10 10 10 10")
    mainframe.grid(column=0, row=0, sticky=(W, N, E, S))
    
    ttk.Label(mainframe, text=alert_text).grid(column=0, row=1, padx="15", pady="15", sticky=E)
    ttk.Button(mainframe, text="Ok", command=lambda: root.destroy()).grid(column=0, row=2)