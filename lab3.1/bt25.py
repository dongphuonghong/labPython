# 25. Viết chương trình nhập vào hai số nguyên dương a và b. Tìm ước số chung lớn nhất và bội số chung nhỏ nhất của a và b.
# CÁCH 1: Thuật toán Euclid không sử dụng biến tạm
# Nhập hai số nguyên dương từ bàn phím
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
# Lưu giá trị ban đầu của a và b
x = a
y = b
# Sử dụng thuật toán Euclid để tìm UCLN
# Điều kiện: tiếp tục khi cả a và b đều khác 0
while a!=0 and b!=0:
    # Nếu a lớn hơn b, thay a bằng a chia dư cho b
    if a > b:
        # Cập nhật a là a chia dư cho b
        a=a % b
        # Nếu b lớn hơn hoặc bằng a, thay b bằng b chia dư cho a
    else:        
        b= b % a
# Xác định UCLN (số còn lại khác 0)
ucln=a
if b!=0:
    # Nếu b khác 0 thì ucln là b
    ucln=b
# Tính BCNN bằng công thức BCNN = (x*y)/UCLN
bcnn=(x*y)//ucln
# In kết quả
print("Ước số chung lớn nhất là: ", ucln)
print("Bội số chung nhỏ nhất là: ", bcnn)
"""
Cách 2: Thuật toán Euclid sử dụng biến tạm (temp)
 Sử dụng biến tạm để hoán đổi giá trị a và b
 Điều kiện dừng: b == 0 (thay vì a!=0 and b!=0)
 Kết quả cuối cùng được lưu trong biến a
# 25. Viết chương trình nhập vào hai số nguyên dương a và b. Tìm ước số chung lớn nhất và bội số chung nhỏ nhất của a và b.
# ước số chung lớn nhất (UCLN) của hai số nguyên dương a và b là số nguyên dương lớn nhất chia hết cho cả a và b.
# bội số chung nhỏ nhất (BCNN) của hai số nguyên dương a và b là số nguyên dương nhỏ nhất chia hết cho cả a và b.
# Nhập hai số nguyên dương từ bàn phím
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
# khởi tạo biến x = a, y = b để lưu giá trị ban đầu của a và b
x = a
y = b
# Sử dụng thuật toán Euclid để tìm ước số chung lớn nhất (UCLN)
# Dùng vòng lặp while kiểm tra điều kiện b khác 0
while b != 0:
    # tạo biến tạm để lưu giá trị của b
    temp= b
    # cập nhật giá trị của b là a chia cho b lấy dư
    b= a % b
    # cập nhật giá trị của a là giá trị tạm
    a= temp
# in ra ước số chung lớn nhất
print("Ước số chung lớn nhất là: ", a)
# tạo biến ucln là a (giá trị cuối cùng của a sau khi vòng lặp kết thúc)
ucln= a
# tính bội số chung nhỏ nhất (BCNN) bằng công thức bcnn = (x*y)//ucln
bcnn= (x*y)//ucln
# in ra bội số chung nhỏ nhất
print("Bội số chung nhỏ nhất là: ", bcnn)
"""