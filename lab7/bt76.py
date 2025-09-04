# Bài 76: Tìm vị trí phần tử nhỏ nhất trong danh sách (nếu nhiều lấy đầu tiên).
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
    """Nhập danh sách n số nguyên.

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


def tim_vi_tri_nho_nhat(lst):
    """Tìm vị trí phần tử nhỏ nhất (nếu nhiều lấy vị trí đầu tiên).

    Args:
        lst (list[int]): Danh sách số nguyên.

    Returns:
        int: Chỉ số phần tử nhỏ nhất.
    """
    min_index = 0

    for i in range(1, len(lst)):
        if lst[i] < lst[min_index]:
            min_index = i
    return min_index


def main():
    """Hàm chính: nhập danh sách và in vị trí phần tử nhỏ nhất."""
    n = nhap_so_luong_phan_tu()
    lst = nhap_danh_sach(n)
    vi_tri = tim_vi_tri_nho_nhat(lst)
    print("Vị trí phần tử nhỏ nhất trong danh sách là:", vi_tri)


if __name__ == "__main__":
    main()
