# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 14:48:01 2024

@author: NGUYEN DUC LOI
"""

email = input("Nhập vào một email: ")
khoang_trang = " "
ktdb = ['!', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '+', '.', '/']
ten_duoi_hop_le = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com"]
if "@" not in email or email.count("@") != 1:
    print("nhập email không hợp lệ")
else:
    ten_nguoi_dung, ten_duoi = email.split("@")
    print(ten_nguoi_dung)
    print(ten_duoi)
    if ten_duoi not in ten_duoi_hop_le or len(ten_nguoi_dung) < 6:
        print("email không hợp lệ")
    else:
        for i in ten_nguoi_dung:
            if i == khoang_trang or i in ktdb:
                print("email không hợp lệ")
                break
        else:
            print("email hợp lệ")
