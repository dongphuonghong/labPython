# 26. Viêt chương trinh đêm sô ươc sô cua sô nguyên dương N.Vi du:  N=12sô ươc sô cua 12 la 6
# Nhập số nguyên dương từ bàn phím

n=int(input("Nhap so nguyen duong N: "))
# Khởi tạo biến đếm d = 1 (vì i bắt đầu từ 1, và 1 luôn là ước của mọi số)

d=1
# Duyệt từ 1 đến n-1 để kiểm tra ước của n
for i in range(1,n):
        # Nếu N chia hết cho i thì i là ước của N → tăng biến đếm lên 1
    if n%i==0:
        d+=1
# In ra tổng số ước của N
print("Uoc so cua",n,"la",d)
# cách 2 dùng thư viện math
"""
import math
# Nhập số nguyên dương từ bàn phím

n=int(input("Nhap so nguyen duong N: "))
# khởi tạo biến đếm d với giá trị 2 (đếm số 2)
d=2
#dùng vòng lặp for để kiểm tra các số từ 2 đến căn bậc 2 của n
for i in range(2,int(math.sqrt(n))+1):
    # nếu n chia hết cho i thì d tăng lên 1
    if n%i==0:
        d+=1
        # nếu n chia hết cho i và n//i khác i thì d tăng lên 1
        if n//i!=i:
            d+=1
# In ra tổng số ước của N
print("tong cac so uoc cua ",n,"la:",d)
"""