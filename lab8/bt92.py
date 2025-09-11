# 92. Viết hàm đếm số lần xuất hiện của phần tử  x trong mảng.
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


def demSoLanXuatHien(lst, x):
    """Đếm số lần xuất hiện của phần tử x trong danh sách.

    Args:
        lst (list[int]): Danh sách số nguyên.
        x (int): Giá trị cần đếm.

    Returns:
        int: Số lần xuất hiện của x trong danh sách.
    """
    d = 0
    for i in lst:
        if i == x:
            d += 1
    return d


n = nhap_so_luong_phan_tu()
lst = nhap_danh_sach(n)
x = int(input("Nhập phần tử x cần đếm: "))
print("Số lần xuất hiện của phần tử {} là: {}".format(x, demSoLanXuatHien(lst, x)))
