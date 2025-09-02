# 38. Tính S(n) = 1 + (1+2)/2! + (1+2+3)/3! + ... + (1+2+...+n)/n!.
# CÁCH 1: Dùng for loop với công thức tổng số tự nhiên
# Nhập giá trị n từ bàn phím
n = int(input("Nhap n: "))
# Khởi tạo biến sum = 1 để lưu tổng (bắt đầu với số hạng đầu tiên)
sum = float(1)
# Dùng vòng lặp từ 2 đến n để tính từng phần tử của tổng
for i in range(2, n+1):
    # Tính tử số: 1 + 2 + ... + i
    # Công thức tổng số tự nhiên
    tu_so = i * (i + 1) // 2
    # Tính giai thừa i!
    giaithua = 1
    for j in range(1, i+1):
        giaithua *= j
    # Cộng phần tử tu_so/i! vào tổng
    sum += tu_so / giaithua
# in ra kết quả
print("S(n) = ", sum)
# CÁCH 2: Dùng hàm math.factorial
""" 
import math
# Nhập giá trị n từ bàn phím
n=int(input("Nhap n: "))
# Khởi tạo biến sum = 1 để lưu tổng
sum=1.0
# Dùng vòng lặp từ 2 đến n để tính từng phần tử của tổng
for i in range(2,n+1):
    # Tính tử số: 1 + 2 + ... + i bằng công thức
    tu_so = i * (i + 1) // 2
    # Cộng dồn tu_so/i! vào biến sum, dùng hàm math.factorial(i) để tính giai thừa
    sum += tu_so / math.factorial(i)
print("S(n) = ",sum)
 """
# CÁCH 3: Dùng 3 vòng lặp for
""" 
# 38. Tính S(n) = 1 + (1+2)/2! + (1+2+3)/3! + ... + (1+2+...+n)/n!
# Nhập giá trị n từ bàn phím
n=int(input("Nhap n: "))
# Khởi tạo biến sum = 1 để lưu tổng (bắt đầu với số hạng đầu tiên)
sum=float(1)
# Dùng vòng lặp từ 2 đến n để tính từng phần tử của tổng
for i in range(2,n+1):
    tu_so=0
    # Tính tử số: 1 + 2 + ... + i
    for j in range(1, i+1):
        tu_so += j
    # Tính giai thừa i!
    giaithua = 1
    for k in range(1, i+1):
        giaithua *= k
    # Cộng phần tử tu_so/i! vào tổng
    sum += tu_so / giaithua
# In ra kết quả
print("S(n) = ", sum)
 """
