# Bài 87: Đổi chỗ phần tử lớn nhất với phần tử nhỏ nhất trong danh sách.
def nhap_so_luong_phan_tu():
    """Nhập số lượng phần tử của danh sách.

    Returns:
        int: Số lượng phần tử (>0).
    """
    while True:
        n = int(input("Nhập số lượng phần tử của mảng: "))
        if n > 0:
            break
        print("Số lượng phần tử phải lớn hơn 0. Vui lòng nhập lại.")
    return n


def nhap_danh_sach(n):
    """Nhập danh sách n số nguyên.

    Args:
        n (int): Số lượng phần tử.

    Returns:
        list[int]: Danh sách số nguyên.
    """
    lst = []
    for i in range(n):
        x = int(input("Nhập phần tử thứ {}: ".format(i+1)))
        lst.append(x)
    return lst


def doi_cho_max_min(lst):
    """Đổi chỗ phần tử lớn nhất với phần tử nhỏ nhất.

    Args:
        lst (list[int]): Danh sách số nguyên.

    Returns:
        list[int]: Danh sách sau khi đổi chỗ.
    """
    if not lst:
        return lst
    max_index = lst.index(max(lst))
    min_index = lst.index(min(lst))
    lst[max_index], lst[min_index] = lst[min_index], lst[max_index]
    return lst


def main():
    n = nhap_so_luong_phan_tu()
    lst = nhap_danh_sach(n)
    print("Danh sách ban đầu:", lst)
    lst = doi_cho_max_min(lst)
    print("Danh sách sau khi đổi chỗ phần tử lớn nhất với phần tử nhỏ nhất:", lst)
