# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:43:07 2024

@author: NGUYEN DUC LOI
"""

import math
n = int(input("Nhập vào số nguyên dương n: "))
so_khong_nguyen_to = []
while n <= 0:
    n = int(input("Nhập lại số n: "))
kiem_tra = math.sqrt(n)
for i in range(2, int(kiem_tra) + 1):
    if n % i == 0:
        so_khong_nguyen_to += [i]
if len(so_khong_nguyen_to) == 0:
    print("Số", n, "là số nguyên tố")
else:
    print("Số", n, "không là số nguyên tố")
