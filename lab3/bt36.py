# 36. Tính S(n) = 1/1² + 1/2² + 1/3² + ... + 1/n².
# CÁCH 1: Sử dụng vòng lặp for với toán tử **
# Nhập giá trị n từ bàn phím
n = int(input("Nhap n: "))
# Khởi tạo biến sum = 0 để lưu tổng
sum = 0
# Dùng vòng lặp for để tính tổng từ 1 đến n
for i in range(1, n+1):
    # Cộng dồn nghịch đảo bình phương của i vào biến sum
    sum += 1/(i**2)
# In ra kết quả
print("S =", sum)
# CÁCH 2: Dùng math.pow để tính nghịch đảo bình phương
""" 
import math
# Nhập giá trị n từ bàn phím
n=int(input("Nhap n: "))
# Khởi tạo biến sum = 0 để lưu tổng
sum=0
# Dùng vòng lặp for để tính tổng từ 1 đến n
for i in range(1,n+1):
    # Dùng hàm math.pow để tính bình phương của i, rồi tính nghịch đảo và cộng vào sum
    sum+=1/math.pow(i,2)
# In ra kết quả
print("Tong la:",sum)
"""
