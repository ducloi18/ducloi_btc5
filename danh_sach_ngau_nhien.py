# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 18:36:15 2024

@author: NGUYEN DUC LOI
"""

import random
ds = ""
for i in range(random.randrange(1, 12)):
    so = random.randrange(20, 31)
    chuoi = str(so)
    ds = ds + chuoi + " "
print(ds)
ds = ds[:-1]
x = ds.split(" ")
print(len(x))


so_binh_phuong = ""
so_binh_phuong = [pow(float(i), 2) \
                  for i in range(99) if 18 <= pow(float(i), 2) <= 99]
print("Danh sách các giá trị bình phương:", so_binh_phuong)
if so_binh_phuong:
    gia_tri_ngau_nhien = random.choice(so_binh_phuong)
    print("Giá trị ngẫu nhiên từ danh sách bình phương:", gia_tri_ngau_nhien)
