#! /usr/bin/env python3.3
'''
Given two folders as input, folder_duplicate and folder_original, any files or folders in folder_duplicate that have a match in folder_original are moved to a new folder, 'separated'. NOT recursive, i.e. if two folders have a matching name, the entire folder will be moved, regardless of its contents. By default ignores .DS_Store files (Mac's folder attributes file)
'''


import os
from shutil import move
from tkinter import ttk
from tkinter import filedialog
from tkinter import *


# Functions

# Functions to call the select directory dialog. One for each button/folder
def get_folder_duplicate():
    folder_duplicate.set(filedialog.askdirectory())

def get_folder_original():
    folder_original.set(filedialog.askdirectory())
     
def get_folder_separated():
    folder_separated.set(filedialog.askdirectory())


# Compare folders, create set of duplicates, move duplicates
def compare_and_move(folder_duplicate_function,folder_original_function,
                     folder_separated_function,ignore_map_function):
    
    # Get strings from StringVar() arguments
    folder_duplicate_str=folder_duplicate_function.get()
    folder_original_str=folder_original_function.get()
    folder_separated_str=folder_separated_function.get()   
    ignore_map_str = set(ignore_map_function.get().split(sep=','))

    # Check if directories exist
    if not os.path.exists(folder_duplicate_str):
        fail_window = Toplevel(root)
        fail_window.resizable(FALSE,FALSE)
        fail_frame = ttk.Frame(fail_window, padding="10 10 10 10")
        fail_frame.grid(column=0, row=0, sticky=(W, N, E, S))
        ttk.Label(fail_frame, text="The folder with duplicates you specified does not exist. Please try again").grid(column=0, row=0, pady=10)
        ttk.Button(fail_frame, text="Ok",
                   command=lambda: fail_window.destroy()).grid(column=0, row=2)
        return
    if not os.path.exists(folder_original_str):
        fail_window = Toplevel(root)
        fail_window.resizable(FALSE,FALSE)
        fail_frame = ttk.Frame(fail_window, padding="10 10 10 10")
        fail_frame.grid(column=0, row=0, sticky=(W, N, E, S))
        ttk.Label(fail_frame, text="The folder with originals you specified does not exist. Please try again").grid(column=0, row=0, pady=10)
        ttk.Button(fail_frame, text="Ok",
                   command=lambda: fail_window.destroy()).grid(column=0, row=2)
        return
    if not os.path.exists(folder_separated_str):
        fail_window = Toplevel(root)
        fail_window.resizable(FALSE,FALSE)
        fail_frame = ttk.Frame(fail_window, padding="10 10 10 10")
        fail_frame.grid(column=0, row=0, sticky=(W, N, E, S))
        ttk.Label(fail_frame, text="The folder to move to you specified does not exist. Please try again").grid(column=0, row=0, pady=10)
        ttk.Button(fail_frame, text="Ok",
                   command=lambda: fail_window.destroy()).grid(column=0, row=2)
        return
    
    # Draw window with progress bar
    prog_window = Toplevel(root)
    prog_window.resizable(FALSE,FALSE)
    prog_frame = ttk.Frame(prog_window, padding="10 10 10 10")
    prog_frame.grid(column=0, row=0, sticky=(W, N, E, S))
    ttk.Label(prog_frame, text="Searching for and moving duplicates ").grid(column=1, row=0, padx="15", pady="15", sticky=E)
    prog_bar = ttk.Progressbar(prog_frame, orient="horizontal", length=250, mode='indeterminate')
    prog_bar.grid(column=0, row=1, columnspan=3)
    prog_bar.start()
    

    # Create sets from lists from strings
    folder_duplicate_files = set(os.listdir(path=folder_duplicate_str))
    folder_original_files = set(os.listdir(path=folder_original_str))
    ignore_map_set = set(ignore_map_str)
    
    actual_duplicate_set = (folder_duplicate_files & folder_original_files) 
    actual_duplicate_set = actual_duplicate_set - ignore_map_set



    # Move duplicates
    for actual_duplicate_filename in actual_duplicate_set:
        move(folder_duplicate_str + '/' + actual_duplicate_filename, 
             folder_separated_str)
 
    prog_window.destroy()
    
    done_window = Toplevel(root)
    done_window.resizable(FALSE,FALSE)
    done_frame = ttk.Frame(done_window, padding="10 10 10 10")
    done_frame.grid(column=0, row=0, sticky=(W, N, E, S))
    ttk.Label(done_frame, text="All Done!").grid(column=0, row=0, pady=10)
    ttk.Button(done_frame, text="Ok", command=lambda: done_window.destroy()).grid(column=0, row=2)
# End function compare_and_move
    



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
ttk.Label(mainframe, text="Folder with duplicates: ") \
    .grid(column=0, row=1, padx="15", pady="15", sticky=E)
folder_duplicate = StringVar()
ttk.Entry(mainframe, textvariable=folder_duplicate).grid(column=1, row=1, columnspan=2, padx="15", pady="15", sticky=W+E)
ttk.Button(mainframe, text="Select Folder...", 
           command=lambda: get_folder_duplicate()).grid(column=3, row=1, sticky=W, padx="15", pady="15")


# Folder Original
ttk.Label(mainframe, text="Folder with originals: ").grid(column=0, row=2, padx="15", pady="15", sticky=E)
folder_original = StringVar()
ttk.Entry(mainframe, textvariable=folder_original).grid(column=1, row=2, columnspan=2, padx="15", pady="15", sticky=W+E)
ttk.Button(mainframe, text="Select Folder...", 
           command=lambda: get_folder_original().grid(column=3, row=2, padx="15", pady="15")

# Folder Separated
ttk.Label(mainframe, text="Folder to move duplicates to: ").grid(column=0, row=3, padx="15", pady="15", sticky=E)
folder_separated = StringVar()
ttk.Entry(mainframe, textvariable=folder_separated).grid(column=1, row=3, columnspan=2, padx="15", pady="15", sticky=W+E)
ttk.Button(mainframe, text="Select Folder...", 
           command= lambda: get_folder_separated()).grid(column=3, row=3, padx="20", pady="20")


# Ignore map
ttk.Label(mainframe, text="Files to ignore(comma delimited, no spaces): ").grid(column=0, row=4, padx="15", pady="15", sticky=E)
ignore_map = StringVar()
ignore_map.set(".DS_Store,")
ttk.Entry(mainframe, textvariable=ignore_map).grid(column=1, row=4, columnspan=2, sticky=W+E)


# Execute Button
ttk.Button(mainframe, text="Find and Move!", 
           command= lambda: compare_and_move(folder_duplicate,folder_original,folder_separated,ignore_map)).grid(column=3, row=5, sticky=(W, E), padx="20", pady="30")


root.mainloop()