# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 19:22:31 2024

@author: NGUYEN DUC LOI
"""

print("Danh sách các số thỏa yêu cầu là: ")
for i in range(2020, 3839):
    if i % 2 == 0 and i % 9 == 0:
        print(i, end='\t')
