#! /usr/bin/env python3
'''
Given two folders as input, folder_duplicate and folder_original, any files or folders in folder_duplicate that have a match in folder_original are moved to a new folder, 'separated'.
NOT recursive, i.e. if two folders have a matching name, the entire folder will be moved, regardless of its contents.
Ignores .DS_Store files (Mac's folder attributes file)
'''


import os
from shutil import move
from tkinter import *
from tkinter import ttk
from tkinter import filedialog




def get_folder_duplicate():
    folder_duplicate.set(filedialog.askdirectory())


def get_folder_original():
    folder_original.set(filedialog.askdirectory())
    
    
def get_folder_separated():
    folder_separated.set(filedialog.askdirectory())




#Compare folders, create set of duplicates, move duplicates
def compare_and_move():
    
    folder_duplicate_str=folder_duplicate.get()
    folder_original_str=folder_original.get()
    folder_separated_str=folder_separated.get()
    ignore_map_str = ignore_map.get()
    
    
    folder_duplicate_files = set(os.listdir(path=folder_duplicate_str))#Create sets from list
    folder_original_files = set(os.listdir(path=folder_original_str))#Create sets from list
    ignore_map_set = set(ignore_map_str)
    
    actual_duplicate_set = (folder_duplicate_files & folder_original_files) 
    actual_duplicate_set = actual_duplicate_set - ignore_map_str

    #Move duplicates
    for actual_duplicate_filename in actual_duplicate_set:
        #print('Duplicate Detected! Moving ' + actual_duplicate_filename)
        move(folder_duplicate_str + '/' + actual_duplicate_filename, folder_separated_str)
    
root = Tk()
root.title("File Compare and Move")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


mainframe = ttk.Frame(root, padding="10")
mainframe.grid(column=0, row=0, sticky=(W, N, E, S))

mainframe.columnconfigure(0, weight=0)
mainframe.columnconfigure(1, weight=3, minsize="100")
mainframe.columnconfigure(2, weight=3, minsize="100")
mainframe.columnconfigure(3, weight=0)


mainframe.rowconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=2)
mainframe.rowconfigure(2, weight=2)
mainframe.rowconfigure(3, weight=2)
mainframe.rowconfigure(4, weight=2)
mainframe.rowconfigure(5, weight=2)



#Folder Duplicate
ttk.Label(mainframe, text="Folder with duplicates: ").grid(column=0, row=1, padx="15", pady="15")
folder_duplicate = StringVar()
ttk.Entry(mainframe, textvariable=folder_duplicate).grid(column=1, row=1, columnspan=2, padx="15", pady="15")
ttk.Button(mainframe, text="Select Folder...", command=lambda: get_folder_duplicate()).grid(column=3, row=1, sticky=(W, E), padx="15", pady="15")


#Folder Original
ttk.Label(mainframe, text="Folder with originals: ").grid(column=0, row=2, padx="15", pady="15")
folder_original = StringVar()
ttk.Entry(mainframe, textvariable=folder_original).grid(column=1, row=2, columnspan=2, padx="15", pady="15")
ttk.Button(mainframe, text="Select Folder...", command=lambda: get_folder_original()).grid(column=3, row=2, sticky=(W, E), padx="15", pady="15")

#Folder Separated
ttk.Label(mainframe, text="Folder to move duplicates to: ").grid(column=0, row=3, padx="15", pady="15")
folder_separated = StringVar()
ttk.Entry(mainframe, textvariable=folder_separated).grid(column=1, row=3, columnspan=2, padx="15", pady="15")
ttk.Button(mainframe, text="Select Folder...", command= lambda: get_folder_separated()).grid(column=3, row=3, sticky=(W, E), padx="20", pady="20")


#Ignore map
ttk.Label(mainframe, text="Files to ignore (comma delimited): ").grid(column=0, row=4, padx="15", pady="15")
ignore_map = StringVar()
ignore_map.set(".DS_Store,")
ttk.Entry(mainframe, textvariable=ignore_map).grid(column=1, row=4, columnspan=2)


#Excecute Button
ttk.Button(mainframe, text="Find and Move!", command= lambda: compare_and_move()).grid(column=3, row=5, sticky=(W, E), padx="20", pady="30")


root.mainloop()