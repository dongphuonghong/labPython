# 36. Tinh,  vơi1 4 3 3 2 2 1 ) (       n n n S 
# tạo biến n và nhập giá trị từ bàn phím
n=int(input("Nhap n: "))
# khởi tạo biến sum = 0 để lưu tổng
sum=0
# dùng vòng lặp for để tính tổng từ 1 đến n
for i in range(1,n+1):
       # cộng dồn bình phương của i vào biến sum
   sum+=i*i 
# in ra kết quả
print("S = ",sum)
# cách 2 dùng math.pow để tính bình phương
""" 
import math
# tạo biến n và nhập giá trị từ bàn phím
n=int(input("Nhap n: "))
# khởi tạo biến sum = 0 để lưu tổng
sum=0
# dùng vòng lặp for để tính tổng từ 1 đến n
for i in range(1,n+1):
        # dùng hàm math.pow để tính bình phương của i, rồi cộng vào sum
    sum+=(int)(math.pow(i,2))
    # in ra kết quả
print("Tong la: ",sum)
"""