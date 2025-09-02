# 53. Viết chương trình nhập 2 số nguyên dương a, b. Tìm USCLN và BSCNN của hai số nguyên đó.
# Đây là hàm tính USCLN (ước số chung lớn nhất) của hai số nguyên dương a và b
# bằng thuật toán Euclid.
def tim_uscln(a, b):
    """Tìm ƯCLN của hai số bằng thuật toán Euclid.

    Args:
        a (int): Số nguyên dương.
        b (int): Số nguyên dương.

    Returns:
        int: Ước số chung lớn nhất.
    """
    while b != 0:
        a, b = b, a % b
    return a
# Đây là hàm tính BSCNN (bội số chung nhỏ nhất) của hai số nguyên dương a và b
# bằng công thức: BSCNN(a, b) = (a * b) / USCLN(a, b)


def tim_bscnn(a, b):
    """Tính BSCNN của hai số.

    Args:
        a (int): Số nguyên dương.
        b (int): Số nguyên dương.

    Returns:
        int: Bội số chung nhỏ nhất.
    """
    return a * b // tim_uscln(a, b)
# Đây là hàm main để chạy chương trình nhập dữ liệu và hiển thị kết quả
# Hàm main sẽ gọi các hàm tim_uscln và tim_bscnn


def main():
    """Hàm chính: nhập a, b và in ƯCLN, BSCNN."""
    a = int(input("Nhập số nguyên dương a: "))
    b = int(input("Nhập số nguyên dương b: "))
    uscln = tim_uscln(a, b)
    bscnn = tim_bscnn(a, b)
    print(f"USCLN của {a} và {b} là: {uscln}")
    print(f"BSCNN của {a} và {b} là: {bscnn}")


main()
