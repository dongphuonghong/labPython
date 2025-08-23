# 23. Nhập vào số nguyên dương n; kiểm tra xem n có phải là số chính phương hay không.
# tạo biến n nhập giá trị từ bàn phím
n = int(input("Nhập số nguyên dương n: "))
# công thức kiểm tra số chính phương bằng cách lấy căn bậc 2 của n
cp = int(n**0.5)
# kiểm tra n có phải là số chính phương hay không
# nếu n có căn bậc 2 bằng số nguyên thì n là số chính phương
if cp*cp == n:
    print(f"{n} là số chính phương.")
# nếu không thì n không phải là số chính phương
else:
    print(f"{n} không là số chính phương.")
    # cách 2 sử dụng thư viện  math hàm sqrt dùng để lấy căn bậc 2 của n
    """
    import math
#tạo biến n nhập giá trị từ bàn phím
n=int(input("Nhập số nguyên dương n: "))
cp=math.sqrt(n)
if cp==int(cp):
    print(n," là số chính phương")
else:
    print(n," không phải là số chính phương")
"""
