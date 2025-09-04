#  Bài 88: Với X nhập vào, in các phần tử có giá trị trong [1, X].
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


def in_cac_phan_tu_trong_khoang(lst, x):
    """In các phần tử có giá trị trong đoạn [1, x].

    Args:
        lst (list[int]): Danh sách số nguyên.
        x (int): Cận trên của đoạn.
    """
    print("Các phần tử có giá trị trong [1, {}]:".format(x))
    for i in lst:
        if 1 <= i <= x:
            print(i)


def main():
    n = nhap_so_luong_phan_tu()
    lst = nhap_danh_sach(n)
    x = int(input("Nhập giá trị X: "))
    in_cac_phan_tu_trong_khoang(lst, x)


if __name__ == "__main__":
    main()
