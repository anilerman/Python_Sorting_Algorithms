# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 18:48:18 2023

@author: ANILERMAN
"""

def shell_sort(array):
    n = len(array)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = array[i]
            j = i
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap
            array[j] = temp
        gap //= 2

# Örnek bir dizi
array = [1,5,45,47,32,688,945,21,2,5]

# Shell Sort'u uygula
shell_sort(array)

# Sıralanmış diziyi yazdır
print("Sıralanmış Dizi:", array)
