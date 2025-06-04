# 28. Tính n! với n ≥ 0
#giai thừa của n là tích của tất cả các số nguyên dương từ 1 đến n
# tạo biến n nhập giá trị từ bàn phím
n=int(input("Nhap n: "))
# kiểm tra n có âm hay không
if n<0:
    # nếu n âm thì không tính được giai thừa và in ra thông báo
    # không tính được giai thừa của số âm
    print("Khong tinh duoc giai thua cua so am")
# nếu n không âm thì tính giai thừa
else:
    # tạo biến gia thừa và khởi tạo giá trị bằng 1
    giaithua=1
    #  dùng vòng lập for duyệt từ 1 đến n
    for i in range(2,n+1):
    # nhân gia thừa với i
        giaithua*=i
print("Giai thua cua",n,"la:",giaithua)
#cách 2 sử dụng hàm factorial của thư viện math đêm tính giai thừa
"""
import math
# tạo biến n nhập giá trị từ bàn phím
n=int(input("Nhap n: "))
# kiểm tra n có âm hay không
if n<0:
# nếu n âm thì không tính được giai thừa và in ra thông báo
# không tính được giai thừa của số âm
    print("Khong tinh duoc giai thua cua so am")
# nếu n dương thì tính giai thừa
else:
# tính giai thừa của n bằng cách sử dụng hàm factorial trong thư viện math
    # và in ra kết quả
    print("Giai thua cua",n,"la:",math.factorial(n))
  """