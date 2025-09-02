# 43. Viết chương trình tính diện tích và chu vi của hình chữ nhật với chiều dài và chiều rộng được nhập từ bàn phím.
def tinhDienTich(chieuDai, chieuRong):
    """Tính diện tích hình chữ nhật.

    Args:
        chieuDai (float): Chiều dài hình chữ nhật.
        chieuRong (float): Chiều rộng hình chữ nhật.

    Returns:
        float: Diện tích (chiều dài * chiều rộng).
    """
    return chieuDai * chieuRong


def tinhChuVi(chieuDai, chieuRong):
    """Tính chu vi hình chữ nhật.

    Args:
        chieuDai (float): Chiều dài hình chữ nhật.
        chieuRong (float): Chiều rộng hình chữ nhật.

    Returns:
        float: Chu vi = 2 * (chiều dài + chiều rộng).
    """
    return 2 * (chieuDai + chieuRong)


def main():
    """Hàm chính: nhập dữ liệu từ người dùng và in diện tích, chu vi."""
    chieuDai = float(input("Nhập chiều dài của hình chữ nhật: "))
    chieuRong = float(input("Nhập chiều rộng của hình chữ nhật: "))
    dienTich = tinhDienTich(chieuDai, chieuRong)
    chuVi = tinhChuVi(chieuDai, chieuRong)
    print(f"Diện tích của hình chữ nhật là: {dienTich}")
    print(f"Chu vi của hình chữ nhật là: {chuVi}")


main()
