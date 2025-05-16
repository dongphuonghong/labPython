# 33. Tinh,  vơi2 2 2 2 3 2 1 ) ( n n S      
# Ý tưởng: sử dụng vòng lặp để tính tổng bình phương các số từ 1 đến n
# tạo biến n và nhập giá trị từ bàn phím
n=int(input("nhap n: "))
# khởi tạo biến sum = 0 để lưu tổng
sum=0
# dùng vòng lặp for để tính tổng bình phương từ 1 đến n
for i in range(1,n+1):
        # cộng bình phương của i vào biến sum (i^2 = i * i)
#ta dùng công thức i*i để cộng vào biến sum
    sum+=i*i
# in ra kết quả tổng S(n)
print("Tổng S(n) là:", sum)
# cách 2 dùng hàm math.pow để tính lũy thừa
"""  
import math
# nhập n từ bàn phím
n=int(input("nhap n: "))
# khởi tạo biến sum = 0 để lưu tổng
sum=0
# dùng vòng lặp for để tính tổng bình phương từ 1 đến n
for i in range(1,n+1):
        # dùng math.pow để tính i^2, sau đó ép kiểu về int
# dùng hàm math.pow để tính lũy thừa
    sum+=(int)(math.pow(i,2))
# in kết quả
print("Tổng S(n) là:", sum)
"""