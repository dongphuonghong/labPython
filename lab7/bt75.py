# Bài 75: Tìm vị trí xuất hiện cuối cùng của giá trị x trong danh sách.
def nhap_so_luong_phan_tu():
    """Nhập số lượng phần tử của danh sách.

    Returns:
        int: Số lượng phần tử (số nguyên dương > 0).
    """
    while True:
        n = int(input("Nhập số lượng phần tử của mảng: "))
        if n > 0:
            break
        print("Số lượng phần tử phải lớn hơn 0. Vui lòng nhập lại.")
    return n


def nhap_danh_sach(n):
    """Nhập danh sách gồm n số nguyên từ bàn phím.

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


def tim_vi_tri_cuoi_cung(lst, x):
    """Tìm vị trí xuất hiện cuối cùng của giá trị x trong danh sách.

    Args:
        lst (list[int]): Danh sách các số nguyên.
        x (int): Giá trị cần tìm.

    Returns:
        int: Vị trí (chỉ số) xuất hiện cuối cùng của x trong lst, hoặc -1 nếu không tìm thấy.
    """
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] == x:
            return i
    return -1


# Chương trình chính
n = nhap_so_luong_phan_tu()
lst = nhap_danh_sach(n)
x = int(input("Nhập giá trị x cần tìm: "))
vi_tri = tim_vi_tri_cuoi_cung(lst, x)
if vi_tri != -1:
    print("Vị trí xuất hiện cuối cùng của {} là: {}".format(x, vi_tri))
else:
    print("{} không có trong danh sách.".format(x))