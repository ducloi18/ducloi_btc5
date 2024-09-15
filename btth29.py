# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 21:58:34 2024

@author: NGUYEN DUC LOI
"""

N = int(input("Nhập số nguyên dương N: "))
tong_cac_chu_so = 0
while N < 0:
    N = int(input("Nhập lại số nguyên dương N: "))
for chu_so in str(N):
    tong_cac_chu_so += int(chu_so)
print("Tổng các chữ số của N là: ", tong_cac_chu_so)
