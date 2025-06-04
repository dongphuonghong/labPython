# 33. Tính S(n) = 1² + 2² + 3² + ... + n² (với n ≥ 0)
# Tính tổng bình phương các số từ 1 đến n
# CÁCH 1: Sử dụng vòng lặp for với phép nhân
# Nhập giá trị n từ bàn phím
n=int(input("nhap n: "))
# Khởi tạo biến sum = 0 để lưu tổng
sum=0
# Dùng vòng lặp for để tính tổng bình phương từ 1 đến n
for i in range(1,n+1):
    # Cộng bình phương của i vào biến sum (i² = i * i)
    sum+=i*i
# In ra kết quả tổng S(n)
print("Tổng S(n) là:", sum)
# CÁCH 2: Dùng hàm math.pow để tính lũy thừa
"""  
import math
# Nhập n từ bàn phím
n=int(input("nhap n: "))
# Khởi tạo biến sum = 0 để lưu tổng
sum=0
# Dùng vòng lặp for để tính tổng bình phương từ 1 đến n
for i in range(1,n+1):
    # Dùng math.pow để tính i², sau đó ép kiểu về int
    sum+=(int)(math.pow(i,2))
# In kết quả
print("Tổng S(n) là:", sum)
"""