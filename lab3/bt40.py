# 40. Tính P(x,n) = x¹ + x² + x³ + ... + xⁿ (tổng các lũy thừa của x từ 1 đến n).
# tạo biến n và nhập giá trị từ bàn phím40. Tinh.y x y x P  ) , (
# tạo biến n và nhập giá trị từ bàn phím
n = int(input("Nhap n: "))
# tạo biến x và nhập giá trị từ bàn phím
x = float(input("Nhap x: "))
# Khởi tạo biến luythua để lưu lũy thừa, giá trị ban đầu là 1
luythua = 1
# Khởi tạo biến sum để lưu tổng các lũy thừa
sum = 0
# dùng vòng lặp for để tính tổng từ 1 đến n
for i in range(1, n+1):
    # Tính lũy thừa x^i bằng cách nhân dồn x
    luythua *= x
    # Cộng dồn vào tổng sum
    sum += luythua
# In ra kết quả tổng P(x, n)
print(f"Tong la: {sum}")
# cách 2 sử dụng hàm math.pow
""" 
import math
# tạo biến n và nhập giá trị từ bàn phím
n=int(input("Nhap n: "))
# tạo biến x và nhập giá trị từ bàn phím
x=float(input("Nhap x: "))
# tạo biến sum và khởi tạo giá trị bằng 0
sum=0
# Dùng vòng lặp for để tính tổng từ x^1 đến x^n
for i in range(1,n+1):
        # Tính lũy thừa bằng hàm math.pow và cộng vào tổng
    sum+=math.pow(x,i)
# in ra kết quả
print(f"Tong  la: {sum:}")
 """
