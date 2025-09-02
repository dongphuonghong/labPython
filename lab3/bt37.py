# 37. Tính S(n) = 1 + 1/1! + 1/2! + 1/3! + ... + 1/n!.
# CÁCH 1: Sử dụng vòng lặp for tính giai thừa từng bước
# Nhập giá trị n từ bàn phím
n = int(input("nhập n: "))
# Khởi tạo biến giaithua để lưu giá trị giai thừa, bắt đầu bằng 1
giaithua = 1
# Khởi tạo biến sum để lưu tổng, bắt đầu bằng 1 (số hạng đầu tiên)
sum = 1
# Dùng vòng lặp for để tính tổng nghịch đảo giai thừa từ 1! đến n!
for i in range(1, n+1):
    # Tính giai thừa tại bước i bằng cách nhân dồn với i
    giaithua *= i
    # Cộng dồn nghịch đảo giai thừa vào tổng sum
    sum += 1/giaithua
# In ra kết quả tổng S(n)
print("sum =", sum)
# CÁCH 2: Dùng hàm math.factorial để tính nghịch đảo giai thừa
""" 
import math
# Nhập giá trị n từ bàn phím
n=int(input("nhập n: "))
# Khởi tạo biến sum để lưu tổng, bắt đầu bằng 1 (số hạng đầu tiên)
sum=1
# Dùng vòng lặp for để tính nghịch đảo giai thừa từ 1! đến n!
for i in range(1,n+1):
    # Tính nghịch đảo giai thừa của i bằng hàm math.factorial và cộng vào sum
    sum+=1/math.factorial(i)
# In ra kết quả tổng S(n)
print("sum =",sum)
"""
