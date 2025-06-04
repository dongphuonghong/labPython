# 30. Tính S(n) = (1 + 3 + 5 + ... + (2n+1)) × (1 + 2 + 3 + ... + n)
# Tích của tổng các số lẻ và tổng các số tự nhiên từ 1 đến n
# CÁCH 1: Sử dụng vòng lặp for
# Nhập giá trị n từ bàn phím
n=int(input("Nhap n: "))
# Khởi tạo biến tổng các số lẻ và tổng các số tự nhiên
tong_so_le=0
tong_tu_nhien=0
# Dùng vòng lặp for để tính tổng các số lẻ từ 1 đến (2n + 1)
for i in range(0,n+1):
    # Tính giá trị của biến tong_so_le theo công thức (2*i)+1
    tong_so_le+=(2*i)+1
# Dùng vòng lặp for để tính tổng các số tự nhiên từ 1 đến n
for j in range(1,n+1):
    tong_tu_nhien+=j
# Tính kết quả S theo công thức S = tổng số lẻ × tổng số tự nhiên
kq=tong_so_le*tong_tu_nhien
# In ra kết quả
print("Ket qua S la:",kq)

# CÁCH 2: Tính theo công thức toán học hoặc dùng hàm math.pow 
"""
import math
# Nhập giá trị n từ bàn phím
n=int(input("Nhap n: "))
# Tính tổng các số lẻ theo công thức (n + 1)^2
tong_so_le=int(math.pow(n+1,2))
# Tính tổng tự nhiên theo công thức n*(n+1)/2
tong_tu_nhien=n*(n+1)//2
# Tính kết quả S = tổng số lẻ × tổng số tự nhiên
ketqua=tong_so_le*tong_tu_nhien
# In ra kết quả
print("Ket qua la:",ketqua)
"""