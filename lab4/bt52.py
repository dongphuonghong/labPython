# 52. Nhập vào 6 số thực a, b, c, d, e, f. Giải hệ phương trình sau: ax + by = c, dx + ey = f
# Giải hệ phương trình bậc hai: ax + by = c, dx + ey = f
# Đây là hàm giải hệ phương trình bậc hai với hai ẩn x và y
# Hàm này nhận vào các hệ số a, b, c, d, e, f và giải hệ phương trình
# bằng cách tính định thức D, Dx và Dy. Nếu D = 0, kiểm tra nghiệm đặc biệt Nhâp vao 6 sô thưc a, b, c, d, e, f . Giai hê phương trinh sau :       c by ax f ey dx
#  Giai hê phương trinh bô hai: ax + by = c, dx + ey = f
#  Đây là hàm giải hệ phương trình bậc hai với hai ẩn x và y
#  Hàm này nhận vào các hệ số a, b, c, d, e, f và giải hệ phương trình
#  bằng cách tính định thức D, Dx và Dy. Nếu D = 0,
def giai_phuong_trinh(a, b, c, d, e, f):
    """Giải hệ phương trình tuyến tính hai ẩn.

    Hệ: a*x + b*y = c; d*x + e*y = f.

    Args:
        a (float): Hệ số a.
        b (float): Hệ số b.
        c (float): Hệ số c.
        d (float): Hệ số d.
        e (float): Hệ số e.
        f (float): Hệ số f.

    Returns:
        None
    """
    D = a * e - b * d
    Dx = c * e - b * f
    Dy = a * f - c * d
    if D == 0:
        if Dx == 0 and Dy == 0:
            print("Phương trình có vô số nghiệm.")
        elif Dx == 0 or Dy == 0:
            print("Phương trình vô nghiệm.")
    else:
        x = Dx / D
        y = Dy / D
        print(f"Phương trình có nghiệm duy nhất: x = {x}, y = {y}")
# Đây là hàm main để chạy chương trình nhập dữ liệu và hiển thị kết quả
# Hàm main sẽ gọi hàm giai_phuong_trinh để giải hệ phương trình


def main():
    """Hàm chính: nhập hệ số và giải hệ phương trình."""
    a = float(input("Nhập a: "))
    b = float(input("Nhập b: "))
    c = float(input("Nhập c: "))
    d = float(input("Nhập d: "))
    e = float(input("Nhập e: "))
    f = float(input("Nhập f: "))
    giai_phuong_trinh(a, b, c, d, e, f)


main()
