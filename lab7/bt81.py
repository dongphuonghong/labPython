# Bài 81: Tìm vị trí phần tử âm lớn nhất (gần 0 nhất) trong danh sách.
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


def tim_vi_tri_am_lon_nhat(lst):
    """Tìm vị trí phần tử âm lớn nhất (gần 0 nhất).

    Args:
        lst (list[int]): Danh sách số nguyên.

    Returns:
        int: Chỉ số phần tử âm lớn nhất; -1 nếu không có.
    """
    vi_tri = -1
    am_lon_nhat = None
    for i in range(len(lst)):
        if lst[i] < 0:
            if am_lon_nhat is None or lst[i] > am_lon_nhat:
                am_lon_nhat = lst[i]
            vi_tri = i
    return vi_tri


def main():
    n = nhap_so_luong_phan_tu()
    lst = nhap_danh_sach(n)
    vi_tri = tim_vi_tri_am_lon_nhat(lst)
    if vi_tri == -1:
        print("Không có phần tử âm trong danh sách.")
    else:
        print("Vị trí phần tử âm lớn nhất (gần 0 nhất) trong danh sách là:", vi_tri)


if __name__ == "__main__":
    main()
