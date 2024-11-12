#12. Nhâp vao hai sô nguyên a, b. In ra man hinh gia tri lơn nhât.
# Cách 1 swr dụng if else:
#tạo biến a, b và nhập giá trị cho a, b từ bàn phím
a=int(input(" nhap a : "))    
b=int(input(" nhap b : "))  
#so sánh giá trị của a và b
if a>b:    
    #nếu a lớn hơn b thì in ra ket qua a lớn hơn b
    print("a lớn hơn b")    
    #ngược lại in ra ket qua b lớn hơn a
else:   
    print("b lớn hơn a")
# Cách 2 sử  dụng if else giả dụ a là số lớn nhất :
"""
#tạo biến a,b nhập từ bàn phím.
a=int(input("Nhập số a:"))
b=int(input("Nhập số b:"))
#tìm số lớn nhất bằng cách gỉ dụ a là số lớn nhất
max=a
#so sánh b với max
if b>max:
    #nếu b lớn hơn max thì gán b cho max
    max=b
#in ra kết quả
print("Số lớn nhất là:",max)
"""
# Cách 3 sử dụng hàm max của thư viện math:
"""
import math
#tạo biến a,b nhập từ bàn phím.
a=int(input("Nhập số a:"))
b=int(input("Nhập số b:"))
#tìm số lớn nhất bằng cách swr dụng  hàm max của thư viện math
max1=max(a,b)
#in ra kết quả 
print("Số lớn nhất là:",max1)
"""
# cách 4 sử dụng  if else  rút gọn:
"""
#tạo biến a,b nhập từ bàn phím.
a=int(input("Nhập số a:"))
b=int(input("Nhập số b:"))
#tìm số lớn nhất bằng cách sử dụng toán tử 3 ngôi if else rút gọn trong python
max=(a if a>b else b)
#in ra kết quả 
print("Số lớn nhất là:",max)
"""
# Cách 5 sử dụng hàm max của python:
"""
#tạo biến a,b nhập từ bàn phím.
a=int(input("Nhập số a:"))
b=int(input("Nhập số b:"))
max1=max(a,b)
print("Số lớn nhất là:",max1)
"""