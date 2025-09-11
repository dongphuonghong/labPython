# 98. Viết hàm ti ́nh tổng các phần tử lẻ trong mảng.


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


def tongChan(lst):
    """Tính tổng các phần tử lẻ trong danh sách.

    Args:
        lst (list[int]): Danh sách số nguyên.

    Returns:
        int: Tổng giá trị các phần tử lẻ.
    """
    tong = 0
    for i in lst:
        if i % 2 != 0:
            tong += i
    return tong


N = nhap_so_luong_phan_tu()
lst = nhap_danh_sach(N)
print("Tổng các phần tử chẵn trong mảng là:", tongChan(lst))
