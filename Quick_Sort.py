# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 19:14:57 2023

@author: ANILERMAN
"""

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[len(array) // 2]  # Pivot olarak orta elemanı seçin
    left = [x for x in array if x < pivot]  # Pivot'tan küçük elemanlar
    middle = [x for x in array if x == pivot]  # Pivot ile aynı değere sahip elemanlar
    right = [x for x in array if x > pivot]  # Pivot'tan büyük elemanlar

    # Sıralanmış alt dizileri birleştirin ve dizi döndürün
    return quick_sort(left) + middle + quick_sort(right)

# Örnek bir dizi
array = [1,5,45,47,32,688,945,21,2,5]

# Quick Sort'u uygula
sorted_array = quick_sort(array)

# Sıralanmış diziyi yazdır
print("Sıralanmış Dizi:", sorted_array)
