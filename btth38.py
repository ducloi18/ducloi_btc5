# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 00:04:38 2024

@author: NGUYEN DUC LOI
"""

n = int(input("Nhập vào số nguyên dương n: "))
S = 1
while n <= 0:
    n = int(input("Nhập lại n: "))
for i in range(1, n + 1):
    S *= i
print("Tổng là: ", S)
