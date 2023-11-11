# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 18:37:50 2023

@author: ANILERMAN
"""

def insertion_sort(array):
    n = len(array)

    for i in range(1, n):
        sorted_value = array[i]  
        j = i - 1  

        # Karşılaştırılacak elemanı sıralı bölümdeki uygun konuma yerleştir
        while j >= 0 and sorted_value < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = sorted_value

# Örnek bir dizi
arr = [1,5,45,47,32,688,945,21,2,5]

# Insertion Sort'u uygula
insertion_sort(arr)

# Sıralanmış diziyi yazdır
print("Sıralanmış Dizi:", arr)