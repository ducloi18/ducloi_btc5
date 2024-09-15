# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 19:43:10 2024

@author: NGUYEN DUC LOI
"""

n = int(input("Nhập số nguyên n: "))
for i in range(1, n + 1):
    mu = pow(i, i)
    dict = {i : mu}
    print(dict)
