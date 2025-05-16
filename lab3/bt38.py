# 38. Tinh,  vơi! 3 2 1 ! 3 3 2 1 ! 2 2 1 1 ) ( n n n S              
# Nhập giá trị n từ bàn phím
n=int(input("Nhap n: "))
# Khởi tạo biến sum = 0 để lưu tổng
sum=0
# tạo biến giai thừa=1
giaithua=1
# Dùng vòng lặp từ 1 đến n để tính từng phần tử của tổng
for i in range(1,n+1):
        # Cập nhật giai thừa tại bước i
    giaithua*= i    
        # Cộng phần tử 1/i! vào tổng
sum+=1/giaithua
# Cộng thêm phần tử đầu tiên là 1 (theo đề bài)
sum += 1
#in ra kết quả
print("S = ",sum)
# cách 2  dùng hàm math.factorial 
""" 
import math
# Nhập giá trị n từ bàn phím
n=int(input("Nhap n: "))
# Khởi tạo biến sum = 0 để lưu tổng
sum=0
 #Dùng vòng lặp từ 1 đến n để tính từng phần tử của tổng
for i in range(1,n+1):
            # cộng dồn 1/i! vào biến sum, dùng hàm math.factorial(i) để tính giai thừa

        sum+=1/math.factorial(i)
print("S = ",sum)
 """