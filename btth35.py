# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 14:54:26 2024

@author: NGUYEN DUC LOI
"""

so_nguyen = int(input("Nhập một số nguyên dương n: "))
if so_nguyen > 0:
    S = 0
    for i in range(1, so_nguyen + 1):
        S += i
    print("Kết quả là: ", S)
else:
    print("Vui lòng nhập số nguyên dương")
