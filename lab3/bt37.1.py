# 37. Tinh,  vơi! 1 ! 3 1 ! 2 1 1 ) ( n n S      
import math
# tạo biến n và nhập giá trị từ bàn phím
n=int(input("nhập n: "))
# Tạo biến sum để lưu tổng các giai thừa, khởi tạo bằng 0
sum=0
# Dùng vòng lặp for để tính giai thừa từ 1 đến n
for i in range(1,n+1):
        # Tính giai thừa của i bằng hàm math.factorial và cộng vào sum
    sum+=math.factorial(i)
    # In ra kết quả tổng S(n)
print("sum = ",sum)