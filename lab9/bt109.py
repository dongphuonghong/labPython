# 109. Viết hàm sắp xếp danh sách theo thứ tự giảm dần.
def nhap_so_luong_phan_tu():
    """Nhập số lượng phần tử của danh sách.

    Hàm yêu cầu người dùng nhập số lượng phần tử (số nguyên dương) cho danh sách.

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
    """Nhập danh sách gồm n số thực từ bàn phím.

    Args:
        n (int): Số lượng phần tử cần nhập (n > 0).

    Returns:
        list[float]: Danh sách các số thực được người dùng nhập.
    """
    lst = []
    for i in range(n):
        x = float(input("Nhập phần tử thứ {}: ".format(i+1)))
    lst.append(x)
    return lst


def sap_xep_giam_dan(lst):
    """Sắp xếp các phần tử của danh sách theo thứ tự giảm dần.

    Args:
        lst (list[float]): Danh sách các số thực cần sắp xếp.

    Returns:
        list[float]: Danh sách mới đã được sắp xếp giảm dần.
    """
    return sorted(lst, reverse=True)


n = nhap_so_luong_phan_tu()
lst = nhap_danh_sach(n)
lst_sorted = sap_xep_giam_dan(lst)
print("Danh sách sau khi sắp xếp:", lst_sorted)
