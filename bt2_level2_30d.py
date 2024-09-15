# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 02:27:49 2024

@author: NGUYEN DUC LOI
"""

tong_chan = 0
tong_le = 0
for i in range(0, 101):
    if i % 2 == 0:
        tong_chan += i
    else:
        tong_le += i
print("Tổng các số chẵn trong dãy: ", tong_chan)
print("Tổng các số lẻ trong dãy: ", tong_le)