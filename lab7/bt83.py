#   Bài 83: Tìm vị trí phần tử dương nhỏ nhất trong mảng (không có trả về -1).
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


def tim_vi_tri_duong_nho_nhat(lst):
    """Tìm vị trí phần tử dương nhỏ nhất.

    Args:
        lst (list[int]): Danh sách số nguyên.

    Returns:
        int: Chỉ số phần tử dương nhỏ nhất; -1 nếu không có.
    """
    vi_tri = -1
    gia_tri_nho_nhat = None
    for i in range(len(lst)):
        if lst[i] > 0:
            if gia_tri_nho_nhat is None or lst[i] < gia_tri_nho_nhat:
                gia_tri_nho_nhat = lst[i]
                vi_tri = i
    return vi_tri


n = nhap_so_luong_phan_tu()
lst = nhap_danh_sach(n)
vi_tri = tim_vi_tri_duong_nho_nhat(lst)
if vi_tri != -1:
    print("Vị trí phần tử dương nhỏ nhất trong mảng là:", vi_tri)
else:
    print("Mảng không có phần tử dương.")
