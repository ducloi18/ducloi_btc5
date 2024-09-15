# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 19:18:56 2024

@author: NGUYEN DUC LOI
"""


print("Danh sách các số thỏa yêu cầu là: ")
for i in range(2018, 2829):
    if i % 2 == 0 and i % 5 == 0:
        print(i, end='\t')
