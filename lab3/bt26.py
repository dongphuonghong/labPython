# 26. Viết chương trình đếm số ước của số nguyên dương N (ví dụ: N = 12 có 6 ước).
# Nhập số nguyên dương từ bàn phím
n = int(input("Nhap so nguyen duong N: "))
# Khởi tạo biến đếm d = 1 (vì i bắt đầu từ 1, và 1 luôn là ước của mọi số)
d = 1
# Duyệt từ 1 đến n-1 để kiểm tra các ước số khác
for i in range(1, n):
    # Nếu N chia hết cho i thì i là ước của N → tăng biến đếm lên 1
    if n % i == 0:
        d += 1
# In ra tổng số ước của N
print("Số ước của", n, "là", d)
"""
Cách 2: Sử dụng thư viện math để tối ưu hiệu suất (chỉ duyệt đến √n)
Nguyên lý: Nếu i là ước của n thì n/i cũng là ước của n
 Chỉ cần kiểm tra từ 1 đến √n thay vì từ 1 đến n
 Với mỗi ước i tìm được, ta có thêm ước n/i (trừ trường hợp i = √n)
import math
n = int(input("Nhập số nguyên dương N: "))
d = 0
for i in range(1, int(math.sqrt(n)) + 1):
    if n % i == 0:
        d += 1  # Đếm ước i
        if i != n // i:  # Nếu i khác n/i thì đếm thêm ước n/i
            d += 1
print("Số ước của", n, "là", d)
"""
