# 90. Viết hàm đếm các phần tử âm, hàm đếm các phần tử dương trong danh sách.
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


def demSoDuong(lst):
    """Đếm số phần tử dương trong danh sách.

    Args:
        lst (list[int]): Danh sách số nguyên.

    Returns:
        int: Số lượng phần tử > 0.
    """
    d = 0
    for i in lst:
        if i > 0:
            d += 1
    return d


def demSoAm(lst):
    """Đếm số phần tử âm trong danh sách.

    Args:
        lst (list[int]): Danh sách số nguyên.

    Returns:
        int: Số lượng phần tử < 0.
    """
    d = 0
    for i in lst:
        if i < 0:
            d += 1
    return d


n = nhap_so_luong_phan_tu()
lst = nhap_danh_sach(n)
print("Số phần tử dương trong danh sách:", demSoDuong(lst))
print("Số phần tử âm trong danh sách:", demSoAm(lst))
