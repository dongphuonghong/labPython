#  Bài 82: Tìm vị trí phần tử dương đầu tiên trong danh sách (không có trả về -1).
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


def timViTriPhanTuDuong(lst):
    """Tìm vị trí phần tử dương đầu tiên.

    Args:
        lst (list[int]): Danh sách số nguyên.

    Returns:
        int: Chỉ số phần tử dương đầu tiên; -1 nếu không có.
    """
    for i in range(len(lst)):
        if lst[i] > 0:
            return i
    return -1


n = nhap_so_luong_phan_tu()
lst = nhap_danh_sach(n)
print("Danh sách vừa nhập:", lst)
vi_tri = timViTriPhanTuDuong(lst)
if vi_tri != -1:
    print("Vị trí phần tử dương đầu tiên trong danh sách là:", vi_tri)
else:
    print("Không có phần tử dương trong danh sách.")
