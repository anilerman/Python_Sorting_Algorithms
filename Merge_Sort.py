# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 19:07:02 2023

@author: ANILERMAN
"""

def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2  # Diziyi ikiye bölmek için orta nokta

        left_half = array[:mid]  # Sol yarı
        right_half = array[mid:]  # Sağ yarı

        merge_sort(left_half)  # Sol yarıyı sırala (rekürsif çağrı)
        merge_sort(right_half)  # Sağ yarıyı sırala (rekürsif çağrı)

        i = j = k = 0

        # İkiye ayrılmış dizileri birleştirme
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1

        # Sol yarıdaki kalan elemanları birleştirilmiş diziye ekle
        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1

        # Sağ yarıdaki kalan elemanları birleştirilmiş diziye ekle
        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1

# Örnek bir dizi
array = [1,5,45,47,32,688,945,21,2,5]

# Merge Sort'u uygula
merge_sort(array)

# Sıralanmış diziyi yazdır
print("Sıralanmış Dizi:", array)
