#! /usr/bin/env python
'''
Given two folders as input, folder_duplicate and folder_original, any files or folders in folder_duplicate that have a match in folder_original are moved to a new folder, 'separated'. NOT recursive, i.e. if two folders have a matching name, the entire folder will be moved, regardless of its contents. By default ignores .DS_Store files (Mac's folder attributes file)
'''


from Tkinter import *
import ttk
from ttk import *
import tkFileDialog

import implementation


# Functions

# Functions to call the select directory dialog. One for each button/folder
def get_folder_duplicate():
    folder_duplicate.set(tkFileDialog.askdirectory())

def get_folder_original():
    folder_original.set(tkFileDialog.askdirectory())
     
def get_folder_separated():
    folder_separated.set(tkFileDialog.askdirectory())


def window(text):
    new_window = Toplevel(root)
    new_window.resizable(FALSE,FALSE)
    new_frame = ttk.Frame(new_window, padding="10 10 10 10")
    new_frame.grid(column=0, row=0, sticky=(W, N, E, S))
    ttk.Label(new_frame, text=text).grid(column=0, row=0, pady=10)
    ttk.Button(new_frame, text="Ok", command=lambda: new_window.destroy()).grid(column=0, row=2)


# UI    
    
root = Tk()
root.title("File Compare and Move")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.geometry('+30+30')
root.minsize(650,350)
root.maxsize(2000,350)


# Root-level frame
mainframe = ttk.Frame(root, padding="10 30 10 10")
mainframe.grid(column=0, row=0, sticky=(W, N, E, S))

mainframe.columnconfigure(0, weight=0)
mainframe.columnconfigure(1, weight=1, minsize="100")
mainframe.columnconfigure(2, weight=1, minsize="100")
mainframe.columnconfigure(3, weight=0)

mainframe.rowconfigure(0, weight=0)
mainframe.rowconfigure(1, weight=0)
mainframe.rowconfigure(2, weight=0)
mainframe.rowconfigure(3, weight=0)
mainframe.rowconfigure(4, weight=0)
mainframe.rowconfigure(5, weight=0)



# UI Elements

# Folder Duplicate
ttk.Label(mainframe, text="Folder with duplicates: ").grid(column=0, row=1, padx="15", pady="15", sticky=E)
folder_duplicate = StringVar()
ttk.Entry(mainframe, textvariable=folder_duplicate).grid(column=1, row=1, columnspan=2, padx="15", pady="15", sticky=W+E)
ttk.Button(mainframe, text="Select Folder...", command=lambda: get_folder_duplicate()).grid(column=3, row=1, sticky=W, padx="15", pady="15")


# Folder Original
ttk.Label(mainframe, text="Folder with originals: ").grid(column=0, row=2, padx="15", pady="15", sticky=E)
folder_original = StringVar()
ttk.Entry(mainframe, textvariable=folder_original).grid(column=1, row=2, columnspan=2, padx="15", pady="15", sticky=W+E)
ttk.Button(mainframe, text="Select Folder...", command=lambda: get_folder_original()).grid(column=3, row=2, padx="15", pady="15")

# Folder Separated
ttk.Label(mainframe, text="Folder to move duplicates to: ").grid(column=0, row=3, padx="15", pady="15", sticky=E)
folder_separated = StringVar()
ttk.Entry(mainframe, textvariable=folder_separated).grid(column=1, row=3, columnspan=2, padx="15", pady="15", sticky=W+E)
ttk.Button(mainframe, text="Select Folder...", command= lambda: get_folder_separated()).grid(column=3, row=3, padx="20", pady="20")


# Ignore map
ttk.Label(mainframe, text="Files to ignore(comma delimited, no spaces): ").grid(column=0, row=4, padx="15", pady="15", sticky=E)
ignore_map = StringVar()
ignore_map.set(".DS_Store,")
ttk.Entry(mainframe, textvariable=ignore_map).grid(column=1, row=4, columnspan=2, sticky=W+E)


# Execute Button
ttk.Button(mainframe, text="Find and Move!", command= lambda: implementation.compare_and_move("gui",folder_duplicate,folder_original,folder_separated,ignore_map)).grid(column=3, row=5, sticky=(W, E), padx="20", pady="30")


root.mainloop()