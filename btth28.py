# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 19:56:18 2024

@author: NGUYEN DUC LOI
"""

N = int(input("Nhập vào số nguyên dương N: "))
uoc_so = []
while N < 0:
    N = int(input("Nhập lại sô nguyên dương"))
for i in range(1, N + 1):
    uoc_so += [i]
print(uoc_so)
