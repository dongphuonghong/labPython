#  Bài 86: Tìm số lẻ lớn nhất trong danh sách (không có trả về -1).
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


def tim_so_le_lon_nhat(lst):
    """Tìm số lẻ lớn nhất trong danh sách.

    Args:
        lst (list[int]): Danh sách số nguyên.

    Returns:
        int: Số lẻ lớn nhất; -1 nếu không có.
    """
    so_le_lon_nhat = -1
    for i in lst:
        if i % 2 != 0:
            if i > so_le_lon_nhat:
                so_le_lon_nhat = i
    return so_le_lon_nhat


n = nhap_so_luong_phan_tu()
danh_sach = nhap_danh_sach(n)
so_le_lon_nhat = tim_so_le_lon_nhat(danh_sach)
if so_le_lon_nhat != -1:
    print("Số lẻ lớn nhất trong danh sách là:", so_le_lon_nhat)
else:
    print("Danh sách không có số lẻ.")
