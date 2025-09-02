# 41. Tính S(n) = x² + x⁴ + x⁶ + ... + x^(2n).
# CÁCH 1: Dùng for loop với phép nhân dồn
# Tạo biến n và nhập giá trị từ bàn phím
n = int(input("Nhap n: "))
# Tạo biến x và nhập giá trị từ bàn phím
x = float(input("Nhap x: "))
# Tạo biến sum và khởi tạo giá trị bằng 0
sum = 0
# Tính x^2
x1 = x*x
# Khởi tạo biến luythua = x^2
luythua = x1
# Tính tổng các lũy thừa chẵn từ x^2 đến x^(2n)
for i in range(1, n+1):
    sum += luythua
    # Tăng lũy thừa lên bậc tiếp theo (nhân x^2)
    luythua *= x1
# In ra kết quả
print("S(n) = ", sum)
# CÁCH 2: Dùng hàm math.pow để tính lũy thừa
"""
import math
# Tạo biến n và nhập giá trị từ bàn phím
n=int(input("Nhap n: "))
# Tạo biến x và nhập giá trị từ bàn phím
x=float(input("Nhap x: "))
# Khởi tạo biến sum bằng 0 để lưu tổng
sum=0
# Dùng vòng lặp for chạy từ 1 đến n
for i in range(1,n+1):
    # Tính lũy thừa x^(2*i) bằng hàm math.pow và cộng dồn vào sum
    sum+=math.pow(x,2*i)
    # In ra kết quả
print("S(n) = ",sum)
  """
