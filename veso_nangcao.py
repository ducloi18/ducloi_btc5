# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 16:10:36 2024

@author: NGUYEN DUC LOI
"""

import random
ds_veso = []
tien_thuong = 0
gia_ve = 10000
so_ve_mua = random.randrange(1, 9)
tien_tra = so_ve_mua * gia_ve
for k in range(so_ve_mua):
    veso = []
    while len(veso) < 6:
        so = random.randint(1, 46)
        if so not in veso:
            veso += [so]
    ds_veso += [veso]
print("Bạn đã mua các vé số sau: ")
for veso in ds_veso:
    ve_so_str = "-".join(str(so) for so in veso)
    print("Vé số của bạn: ", ve_so_str)
veso_may = []
while len(veso_may) < 6:
    so_may = random.randint(1, 46)
    if so not in veso_may:
        veso_may += [so_may]
ve_so_may = ""
for m in range(len(veso_may)):
    ve_so_may += str(veso_may[m]) + "-"
    ve_so_moi_may = ve_so_may[:-1]
print("Vé số trúng thưởng là: ", ve_so_moi_may)
trung_nhau = []
for veso in ds_veso:
    trung_nhau = [so for so in veso if so in veso_may]
    so_trung = len(trung_nhau)
    print(f"\nVé số {veso} có {so_trung} số trùng", trung_nhau)
if len(trung_nhau) == 3:
    tien_thuong += 30000
elif len(trung_nhau) == 4:
    tien_thuong += 300000
elif len(trung_nhau) == 5:
    tien_thuong += 10000000
elif len(trung_nhau) == 6:
    tien_thuong += 10000000000
print("Số tiền đã tốn khi mua vé số: ", tien_tra)
print("Số tiền trúng thưởng là: ", tien_thuong)
if tien_thuong == 0:
    print("Chúc bạn may mắn lần sau")
