# 99. Viết hàm ti ́nh tổng các phần tử là nguyên tố trong mảng.
def nhap_so_luong_phan_tu():
    """Nhập số lượng phần tử danh sách (số nguyên dương).

    Returns:
        int: Số lượng phần tử (> 0).
    """
    while True:
        n = int(input("Nhập số lượng phần tử của mảng: "))
        if n > 0:
            break
        print("Số lượng phần tử phải lớn hơn 0. Vui lòng nhập lại.")
    return n


def nhap_danh_sach(n):
    """Nhập danh sách n số nguyên từ bàn phím.

    Args:
        n (int): Số lượng phần tử cần nhập.

    Returns:
        list[int]: Danh sách các số nguyên đã nhập.
    """
    lst = []
    for i in range(n):
        x = int(input("Nhập phần tử thứ {}: ".format(i+1)))
        lst.append(x)
    return lst


def kiemTraSoNguyenTo(a):
    """Kiểm tra số nguyên tố.

    Args:
        a (int): Số nguyên cần kiểm tra.

    Returns:
        bool: True nếu là số nguyên tố, False nếu không.
    """
    if a < 2:
        return False
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False
    return True


def tongSoNguyenTo(lst):
    """Tính tổng các phần tử là số nguyên tố trong danh sách.

    Args:
        lst (list[int]): Danh sách số nguyên.

    Returns:
        int: Tổng giá trị các số nguyên tố.
    """
    tong = 0
    for i in lst:
        if kiemTraSoNguyenTo(i):
            tong += i
    return tong


n = nhap_so_luong_phan_tu()
lst = nhap_danh_sach(n)
print("Tổng các phần tử nguyên tố trong mảng là:", tongSoNguyenTo(lst))
