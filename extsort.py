# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 01:48:38 2024

@author: Raunak
"""

def find_smallest(files:list[str], i:int)->int:
    """
    Find the string that lexicographically comes first.

    Parameters
    ----------
    files : list[str]
        DESCRIPTION.
    i : int
        DESCRIPTION.

    Returns
    -------
    int
        DESCRIPTION.

    """
    smallest:str = files[i]
    smallest_i:int = i
    filename, key_ext = smallest.split(".")
    
    for i in range(i+1, len(files)):
        file_ext:str = files[i].split(".")[1]
        
        # if the file extensions are different (lexicographically)
        if file_ext<key_ext:        # compare the file extensions
            smallest = files[i]     # update the smallest value
            smallest_i = i 
            key_ext:str = smallest.split(".")[1]    # update the extension that comes first
        
        # but if the file extensions are same (lexicographically)
        elif ord(file_ext[0])==ord(key_ext[0]):
            if files[i]<filename:       # compare the filenames
                smallest = files[i]
                smallest_i = i 
                key_ext:str = smallest.split(".")[1]
    return smallest_i
            

def extsort(files:list[str])->list[str]:
    """
    Sort a list of filenames based on their extensions.

    Parameters
    ----------
    files : list[str]
        DESCRIPTION.

    Returns
    -------
    list[str]
        DESCRIPTION.

    """
    for i in range(len(files)):
        where_smallest = find_smallest(files, i)
        files[i], files[where_smallest] = files[where_smallest], files[i]
    return files

print(extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c']))
