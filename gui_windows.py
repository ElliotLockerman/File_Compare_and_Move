#! /usr/bin/env python

from Tkinter import *
import ttk
from ttk import *

def alert(alert_text):
    alert_window = Tk()
    alert_window.title("File Compare and Move")
    alert_window.resizable(FALSE,FALSE)
    
    alertframe = ttk.Frame(alert_window, padding="10 10 10 10")
    alertframe.grid(column=0, row=0, sticky=(W, N, E, S))
    
    ttk.Label(alertframe, text=alert_text).grid(column=0, row=1, padx="15", pady="15", sticky=E)
    ttk.Button(alertframe, text="Ok", command=lambda: alert_window.destroy()).grid(column=0, row=2)
