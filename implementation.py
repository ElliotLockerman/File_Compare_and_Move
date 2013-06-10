#! /usr/bin/env python

import os
from gui_alert import alert
from shutil import move

import gui_windows


def alert_user(interface_type, alert_text):
    if interface_type == "gui":
        gui_windows.alert(alert_text)



    
# Compare folders, create set of duplicates, move duplicates
def compare_and_move(main_window,interface_type,folder_duplicate_function,folder_original_function,folder_separated_function,ignore_map_function):
    
        
    # Get strings from StringVar() arguments
    folder_duplicate_str=folder_duplicate_function.get()
    folder_original_str=folder_original_function.get()
    folder_separated_str=folder_separated_function.get()   
    ignore_map_str = set(ignore_map_function.get().split(','))

    # Check if directories exist
    if not os.path.exists(folder_duplicate_str):
        alert_user(interface_type,"The folder with duplicates you specified does not exist. Please try again")
        return

    if not os.path.exists(folder_original_str):
        alert_user(interface_type,"The folder with originals you specified does not exist. Please try again")
        return
        
    if not os.path.exists(folder_separated_str):
        alert_user(interface_type,"The folder to move to you specified does not exist. Please try again")
        return
    
    

    # Create sets from lists from strings
    folder_duplicate_files = set(os.listdir(folder_duplicate_str))
    folder_original_files = set(os.listdir(folder_original_str))
    ignore_map_set = set(ignore_map_str)
    
    actual_duplicate_set = (folder_duplicate_files & folder_original_files) 
    actual_duplicate_set = actual_duplicate_set - ignore_map_set



    # Move duplicates
    for actual_duplicate_filename in actual_duplicate_set:
        move(folder_duplicate_str + '/' + actual_duplicate_filename, 
             folder_separated_str)
 

    
    # And alert user
    alert_user(interface_type,"All done!")
    
# End function compare_and_move
    
