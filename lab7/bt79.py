#  Bài 79: In vị trí các phần tử nguyên tố > 23 trong danh sách.
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


def kiemTraSoNguyenTo(lst):
    """Kiểm tra số nguyên tố.

    Args:
        lst (int): Số nguyên cần kiểm tra.

    Returns:
        bool: True nếu nguyên tố, False nếu không.
    """
    if lst < 2:
        return False
    for i in range(2, int(lst**0.5) + 1):
        if lst % i == 0:
            return False
    return True


def inViTriSoNguyenTo(lst):
    """In vị trí phần tử nguyên tố > 23.

    Args:
        lst (list[int]): Danh sách số nguyên.
    """
    for i in range(len(lst)):
        if kiemTraSoNguyenTo(lst[i]) and lst[i] > 23:
            print("Vị trí phần tử nguyên tố > 23 là: ", i)


n = nhap_so_luong_phan_tu()
lst = nhap_danh_sach(n)
inViTriSoNguyenTo(lst)
