'''
Given two folders as input, folder_duplicate and folder_original, any files or folders in folder_duplicate that have a match in folder_original are moved to a new folder, 'seperated'.
NOT recursive, i.e. if two folders have a matching name, the entire folder will be moved, regardless of its contents.
Ignores .DS_Store files (Mac's folder atributes file)
'''

import os
from shutil import move


folder_duplicate = input('Enter folder_duplicate path. Duplicates found in this folder will be moved: ')
folder_duplicate_files = os.listdir(path=folder_duplicate)
print('folder_duplicate = ' + folder_duplicate)

folder_original = input('Enter folder_original path: ')
folder_original_files = os.listdir(path=folder_original)
print('folder_original = ' + folder_original)

folder_seperated = os.path.dirname(folder_duplicate) + '/seperated'
if not os.path.exists(folder_seperated):
    os.makedirs(folder_seperated)
print('folder_seperated = ' + folder_seperated)

for possible_duplicate_file in folder_duplicate_files:
    print('Checking possible_duplicate_file ' + possible_duplicate_file) 
    if not possible_duplicate_file == '.DS_Store':
        for possible_original_file in folder_original_files:
            if not possible_original_file == '.DS_store':
                if possible_duplicate_file == possible_original_file:
                    print('Duplicate Detected! Moving ' + possible_duplicate_file)
                    move(folder_duplicate + '/' + possible_duplicate_file, folder_seperated)

print('All done!')
