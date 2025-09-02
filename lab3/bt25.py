# 25. Viết chương trình nhập vào hai số nguyên dương a và b; tìm ước số chung lớn nhất (ƯCLN) và bội số chung nhỏ nhất (BCNN) của a và b.
# ước số chung lớn nhất (UCLN) của hai số nguyên dương a và b là số nguyên dương lớn nhất chia hết cho cả a và b.
# bội số chung nhỏ nhất (BCNN) của hai số nguyên dương a và b là số nguyên dương nhỏ nhất chia hết cho cả a và b.
# Nhập hai số nguyên dương từ bàn phím
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
# Khởi tạo biến ucln = 1 ucln = 1 (trường hợp giả sử)
ucln = 1
# Duyệt các số từ 2 đến min(a, b)
for i in range(2, min(a, b)+1):
    # Nếu số i chia hết cho cả a và b thì cập nhật ucln = i    if a%i==0 and b%i==0:
    ucln = i
    # in ra ước số chung lớn nhất
print("Ước số chung lớn nhất của", a, "và", b, "là:", ucln)
# tính bội số chung nhỏ nhất bằng công thức bcnn = (a*b)//ucln
bcnn = (a*b)//ucln
# in ra bội số chung nhỏ nhất
print("Bội số chung nhỏ nhất của", a, "và", b, "là:", bcnn)
