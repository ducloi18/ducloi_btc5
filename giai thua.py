# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 16:51:56 2024

@author: NGUYEN DUC LOI
"""


n = int(input("Nhập vào số nguyên n: "))
giai_thua = 1
for i in range(1, n + 1):
    giai_thua *= i
if n >= 0:
    print(f" Giai thừa của {n} là: {giai_thua}")
else:
    print("Nhập lại số nguyên dương n")
