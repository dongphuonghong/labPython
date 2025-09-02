# 44. Viết chương trình tính diện tích và chu vi hình tròn với bán kính được nhập từ bàn phím.
import math


def tinhDienTich(r):
    """Tính diện tích hình tròn.

    Args:
        r (float): Bán kính hình tròn.

    Returns:
        float: Diện tích = π * r^2.
    """
    return math.pi * r * r


def tinhChuVi(r):
    """Tính chu vi hình tròn.

    Args:
        r (float): Bán kính hình tròn.

    Returns:
        float: Chu vi = 2 * π * r.
    """
    return 2 * math.pi * r


def main():
    """Hàm chính: nhập bán kính và in diện tích, chu vi hình tròn."""
    r = float(input("Nhập bán kính hình tròn: "))
    dienTich = tinhDienTich(r)
    chuVi = tinhChuVi(r)
    print(f"Diện tích hình tròn: {dienTich:.2f}")
    print(f"Chu vi hình tròn: {chuVi:.2f}")


main()
