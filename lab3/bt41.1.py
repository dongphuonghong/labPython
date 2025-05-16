# 41. Tinh,) 3 2 1 ( ) 3 2 1 ( ) 2 1 ( 1 ) ( n n S              
import math
# tạo biến n và nhập giá trị từ bàn phím
n=int(input("Nhap n: "))
# tạo biến x và nhập giá trị từ bàn phím
x=float(input("Nhap x: "))
# tạo biến sum và khởi tạo giá trị bằng 0
sum=0
# dùng vòng lặp for để tính tổng từ 1 đến n+1
for i in range(1,n+1):
    #dùng hàm math.pow để tính lũy thừa với công thức 2*i
    sum+=math.pow(x,2*i)
    # in ra kết quả
print("S = ",sum)