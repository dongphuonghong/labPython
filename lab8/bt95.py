# 95. Viết hàm đếm các phần tử là số hoàn thiện trong danh sách.
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


def kiem_tra_so_hoan_thien(x):
    """Kiểm tra số hoàn thiện.

    Args:
        x (int): Số nguyên dương cần kiểm tra.

    Returns:
        bool: True nếu là số hoàn thiện, False nếu không.
    """
    tong = 0
    for i in range(1, x//2 + 1):
        if x % i == 0:
            tong += i
    return tong == x


def demSoHoanThien(lst):
    """Đếm số phần tử là số hoàn thiện trong danh sách.

    Args:
        lst (list[int]): Danh sách số nguyên.

    Returns:
        int: Số lượng số hoàn thiện.
    """
    d = 0
    for i in lst:
        if kiem_tra_so_hoan_thien(i):
            d += 1
    return d


n = nhap_so_luong_phan_tu()
lst = nhap_danh_sach(n)
print("Số lượng phần tử là số hoàn thiện trong danh sách:", demSoHoanThien(lst))
