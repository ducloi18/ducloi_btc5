# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:00:26 2024

@author: NGUYEN DUC LOI
"""

import math
n = int(input("Nhập vào số nguyên dương n: "))
while n <= 0:
    n = int(input("Nhập lại số n: "))
so_chinh_phuong = math.sqrt(n)
so = int(so_chinh_phuong)
kiem_tra = so * so
if n == kiem_tra:
    print("Số", n, "là số chính phương")
else:
    print("Số", n, "không là số chính phương")
