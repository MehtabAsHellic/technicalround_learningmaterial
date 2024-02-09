# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 10:56:35 2024

@author: Raunak
"""

def find_smallest(lst, i):
    # the first elem is the smallest by default
    small = lst[i]
    small_i = i 
    
    for i in range(i+1, len(lst)):
        if lst[i]<small:
            small = lst[i]
            small_i = i 
    return small_i 

def selection_sort(lst):
    for i in range(0, len(lst)):
        index = find_smallest(lst, i)
        lst[i],lst[index] = lst[index], lst[i]
    return lst

print(selection_sort([5,4,2,6,7,1]))


