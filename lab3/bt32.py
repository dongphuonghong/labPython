# 32. Tinh,  vơin n S   3 . 2 . 1 3 . 2 . 1 2 . 1 1 ) (     0  n
# Nhập n từ bàn phím

n=int(input("nhập n: "))
# Khởi tạo biến giai_thua = 1 để tính giai thừa từng bước

giaithua=1
# Khởi tạo biến sum để lưu tổng

sum=0
# Duyệt từ 1 đến n+1 (vì phải tính đến (n+1)!)
for i in range(1,n+2):
        # Tính giai thừa i bằng cách nhân dồn

    giaithua*=i
        # Cộng dồn giai thừa vào tổng

    sum+=giaithua
# In ra kết quả tổng

print("sum = ",sum)
# Cách 2: Dùng hàm math.factorial() để tính giai thừa

""" 
import math
# Nhập n từ bàn phím

n=int(input("nhập n: "))
# Khởi tạo tổng

sum=0
# Duyệt từ 1 đến n+1

for i in range(1,n+2):
        # Tính giai thừa bằng hàm có sẵn và cộng vào tổng
    sum+=math.factorial(i)
# in ra kết quả
print("Tổng là: ",sum)
 """