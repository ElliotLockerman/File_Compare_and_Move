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


folder_duplicate = None

folder_original = None

folder_seperated = None

ignore_map = None


#Compare folders and create set of duplicates
def compare_folders( folder_duplicate_function, folder_original_function, folder_separated_function, ignore_map_function):
    
    folder_duplicate_files = set(os.listdir(path=folder_duplicate_function))#Create sets from list
    folder_original_files = set(os.listdir(path=folder_original_function))#Create sets from list

    
    actual_duplicate_set = (folder_duplicate_files & folder_original_files) 
    actual_duplicate_set = actual_duplicate_set - ignore_map_function

    #Move duplicates
    for actual_duplicate_filename in actual_duplicate_set:
        #print('Duplicate Detected! Moving ' + actual_duplicate_filename)
        move(folder_duplicate_function + '/' + actual_duplicate_filename, folder_separated_function)
    
root = Tk()


