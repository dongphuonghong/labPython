# 104. Viết hàm ti ́nh tổng các phần tử là bộ i của 3 hoặc 5 trong danh sách các số nguyên.
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


def tinh_tong_boi_3_5(lst):
    """Tính tổng các phần tử là bội số của 3 hoặc 5 trong danh sách.

    Args:
        lst (list[int]): Danh sách các số nguyên.

    Returns:
        int: Tổng các phần tử là bội số của 3 hoặc 5.
    """
    tong = 0
    for i in lst:
        if i % 3 == 0 or i % 5 == 0:
            tong += i
    return tong


n = nhap_so_luong_phan_tu()
lst = nhap_danh_sach(n)
tong = tinh_tong_boi_3_5(lst)
print("Tổng các phần tử là bội của 3 hoặc 5:", tong)
