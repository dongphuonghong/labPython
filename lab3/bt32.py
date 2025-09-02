# 32. Tính S(n) = 1! + 2! + 3! + ... + n! (n ≥ 0).
# Tính tổng các giai thừa từ 1! đến n!
# CÁCH 1: Tính giai thừa bằng vòng lặp for
# Nhập n từ bàn phím
n = int(input("nhập n: "))
# Khởi tạo biến giaithua = 1 để tính giai thừa từng bước
giaithua = 1
# Khởi tạo biến sum để lưu tổng
sum = 0
# Duyệt từ 1 đến n để tính các giai thừa
for i in range(1, n+1):
    # Tính giai thừa i bằng cách nhân dồn
    giaithua *= i
    # Cộng dồn giai thừa vào tổng
    sum += giaithua
# In ra kết quả tổng
print("sum =", sum)
# CÁCH 2: Dùng hàm math.factorial() để tính giai thừa
""" 
import math
# Nhập n từ bàn phím
n=int(input("nhập n: "))
# Khởi tạo tổng
sum=0
# Duyệt từ 1 đến n
for i in range(1,n+1):
    # Tính giai thừa bằng hàm có sẵn và cộng vào tổng
    sum+=math.factorial(i)
# In ra kết quả
print("Tổng là:",sum)
"""
