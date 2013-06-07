'''
Given two folders as input, folder_duplicate and folder_original, any files in folder_duplicate that have a match in folder_original are moved to a new folder, 'seperated'.
Either of the files may have ' copy'after the filename, before the extention (i.e. if two files, one in each folder are identical, except for one or the other having ' copy', they will be treated as identical.
'''

import os
from shutil import move

folder_duplicate = '/Users/EL/Desktop/test environment/Articles_test'
folder_original = '/Users/EL/Desktop/test environment/To_Read_test'


if not folder_duplicate:
    folder_duplicate = input('Enter folder_duplicate path. Duplicates found in this folder will be moved: ')
folder_duplicate_files = os.listdir(path=folder_duplicate)


if not folder_original:
    folder_original = input('Enter folder_original path: ')
folder_original_files = os.listdir(path=folder_original)


folder_seperated = os.path.dirname(folder_duplicate) + '/seperated'
if not os.path.exists(folder_seperated):
    os.makedirs(folder_seperated)

for possible_duplicate_file in folder_duplicate_files:
    for possible_original_file in folder_original_files:
        if possible_original_file == possible_original_file or possible_duplicate_file + ' copy' == possible_original_file or possible_duplicate_file == possible_original_file + ' copy':
            move(folder_original + '/' + possible_duplicate_file, folder_seperated)
