# 44. Viết chương trình tính diện tích và chu vi hình tròn với bán kính được nhập từ bàn phím.
import math
# Đây là hàm tính diện tích hình tròn
# Công thức tính diện tích hình tròn là S = π * r^2
def tinhDienTich(r):
    return math.pi * r * r
# Đây là hàm tính chu vi hình tròn
# Công thức tính chu vi hình tròn là C = 2 * π * r
def tinhChuVi(r):
    return 2 * math.pi * r
# Hàm main để thực hiện chương trình
# Nó sẽ yêu cầu người dùng nhập bán kính hình tròn và sau đó tính diện tích và chu vi
# Cuối cùng, nó sẽ in kết quả ra màn hình
def main():
    r = float(input("Nhập bán kính hình tròn: "))
    dienTich = tinhDienTich(r)
    chuVi = tinhChuVi(r)
    print(f"Diện tích hình tròn: {dienTich:.2f}")
    print(f"Chu vi hình tròn: {chuVi:.2f}")
main()