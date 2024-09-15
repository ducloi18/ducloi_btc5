# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 19:10:45 2024

@author: NGUYEN DUC LOI
"""

print("      Hồ sơ quản lí nhân viên của công ty X:  ")
nhan_vien = [
    {"loai_nv": "van_phong", "ma_nv": "NV001", "ho_ten": "Nguyen Van A", "luong_cb": 5000000, "so_ngay": 22},
    {"loai_nv": "van_phong", "ma_nv": "NV002", "ho_ten": "Tran Thi B", "luong_cb": 4800000, "so_ngay": 20},
    {"loai_nv": "van_phong", "ma_nv": "NV003", "ho_ten": "Hoang Van C", "luong_cb": 5500000, "so_ngay": 25},
    {"loai_nv": "van_phong", "ma_nv": "NV004", "ho_ten": "Pham Thi Yen D", "luong_cb": 5300000, "so_ngay": 23},
    {"loai_nv": "van_phong", "ma_nv": "NV005", "ho_ten": "Nguyen Dinh E", "luong_cb": 5100000, "so_ngay": 21},
    {"loai_nv": "ban_hang", "ma_nv": "NV006", "ho_ten": "Nguyen Thi F", "luong_cb": 4500000, "so_san_pham": 120},
    {"loai_nv": "ban_hang", "ma_nv": "NV007", "ho_ten": "Tran Van G", "luong_cb": 4600000, "so_san_pham": 115},
    {"loai_nv": "ban_hang", "ma_nv": "NV008", "ho_ten": "Phan Thi H", "luong_cb": 4400000, "so_san_pham": 130},
    {"loai_nv": "ban_hang", "ma_nv": "NV009", "ho_ten": "Pham Van I", "luong_cb": 4700000, "so_san_pham": 125},
    {"loai_nv": "ban_hang", "ma_nv": "NV010", "ho_ten": "Hoang Thi K", "luong_cb": 4300000, "so_san_pham": 110}
]
for nv in nhan_vien:
    if nv["loai_nv"] == "van_phong":
        luong_thang = nv["luong_cb"] + nv["so_ngay"] * 100000
    elif nv["loai_nv"] == "ban_hang":
        luong_thang = nv["luong_cb"] + nv["so_san_pham"] * 50000
    print(f"Mã NV: {nv['ma_nv']}, Họ tên: {nv['ho_ten']}, Lương tháng: {luong_thang}")
