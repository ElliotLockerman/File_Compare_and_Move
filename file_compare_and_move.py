#! /usr/bin/env python3
'''
Given two folders as input, folder_duplicate and folder_original, any files or folders in folder_duplicate that have a match in folder_original are moved to a new folder, 'separated'.
NOT recursive, i.e. if two folders have a matching name, the entire folder will be moved, regardless of its contents.
Ignores .DS_Store files (Mac's folder attributes file)
'''

import os
from shutil import move

folder_not_entered = True
while folder_not_entered:
    folder_duplicate = input('Enter the duplicate folder path. Duplicates found in this folder will be moved: ')
    if os.path.exists(folder_duplicate):
        folder_not_entered = False
        print('    folder_duplicate: ' + folder_duplicate, end="\n\n")
    else:
        print('Folder does not exist. Please try again')

folder_not_entered = True
while folder_not_entered:
    folder_original = input('Enter original folder path: ')
    if os.path.exists(folder_original):     
        folder_not_entered = False
        print('    folder_original: ' + folder_original, end="\n\n")
    else:
        print('Folder does not exist. Please try again')

ignore_map = set(input('.DS_Store is ignored by default.\nEnter addition files to be ignored, space delimited\n(If there are no additional files to be ignored, press enter): ').split(sep=' '))
ignore_map.add('.DS_Store')
print('    Ignoring: ',end="") 
print(ignore_map, end="\n\n")

folder_duplicate_files = set(os.listdir(path=folder_duplicate))

folder_original_files = set(os.listdir(path=folder_original))


folder_separated = os.path.dirname(folder_duplicate) + '/separated'
if not os.path.exists(folder_separated):
    os.makedirs(folder_separated)
print('folder_separated: ',end="")
print(folder_separated)


actual_duplicate_set = (folder_duplicate_files & folder_original_files) 
actual_duplicate_set = actual_duplicate_set - ignore_map


for actual_duplicate_filename in actual_duplicate_set:
    print('Duplicate Detected! Moving ' + actual_duplicate_filename)
    move(folder_duplicate + '/' + actual_duplicate_filename, folder_separated)
    


print('All done!')
