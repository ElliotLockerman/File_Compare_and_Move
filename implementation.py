#! /usr/bin/env python

import os
from gui_alert import alert

import gui_alert


def fail(interface_type, fail_text):
    if interface_type == "gui":
        gui_alert.alert(fail_text)



# Compare folders, create set of duplicates, move duplicates
def compare_and_move(interface_type,folder_duplicate_function,folder_original_function,folder_separated_function,ignore_map_function):
    
    # Get strings from StringVar() arguments
    folder_duplicate_str=folder_duplicate_function.get()
    folder_original_str=folder_original_function.get()
    folder_separated_str=folder_separated_function.get()   
    ignore_map_str = set(ignore_map_function.get().split(','))

    # Check if directories exist
    if not os.path.exists(folder_duplicate_str):
        fail(interface_type,"The folder with duplicates you specified does not exist. Please try again")
        return

    if not os.path.exists(folder_original_str):
        fail(interface_type,"The folder with originals you specified does not exist. Please try again")
        return
        
    if not os.path.exists(folder_separated_str):
        fail(interface_type,"The folder to move to you specified does not exist. Please try again")
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
    
