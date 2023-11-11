# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 18:23:47 2023

@author: ANILERMAN
"""

def selection_sort(array):
    
    n = len(array)
    
    for i in range(n):
        
        minimum_index = i
        
        for j in range(i+1, n):
            if array[j] < array[minimum_index]:
                minimum_index = j
        
        array[i], array[minimum_index] = array[minimum_index], array[i]
        
value = [1,5,45,47,32,688,945,21,2,5]

selection_sort(value)

print(value)