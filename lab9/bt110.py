# 110. Viết hàm sắp xếp mảng theo thứ tự tăng dần các phần tử là số nguyên tố.
def nhap_so_luong_phan_tu():
    """Nhập số lượng phần tử của danh sách.

    Yêu cầu người dùng nhập số lượng phần tử của mảng (số nguyên dương).

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
    """Nhập danh sách gồm n số nguyên từ bàn phím.

    Args:
        n (int): Số lượng phần tử cần nhập (n > 0).

    Returns:
        list[int]: Danh sách các số nguyên được nhập.
    """
    lst = []
    for i in range(n):
        x = int(input("Nhập phần tử thứ {}: ".format(i+1)))
        lst.append(x)
    return lst


def kiemTraSoNguyenTo(a):
    """Kiểm tra một số có phải là số nguyên tố.

    Thuật toán kiểm tra bằng cách thử chia các số từ 2 đến căn bậc hai của số cần kiểm tra.

    Args:
        a (int): Số nguyên cần kiểm tra.

    Returns:
        bool: True nếu là số nguyên tố, ngược lại False.
    """
    if a < 2:
        return False
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False
    return True


def sapXepTangDanSoNguyen(lst):
    """Sắp xếp tăng dần các phần tử là số nguyên tố trong danh sách.

    Các phần tử không phải số nguyên tố giữ nguyên vị trí tương đối. Việc sắp xếp thực hiện bằng cách duyệt cặp phần tử và hoán đổi khi cần.

    Args:
        lst (list[int]): Danh sách các số nguyên.

    Returns:
        list[int]: Danh sách sau khi các số nguyên tố đã được sắp xếp tăng dần tại chỗ.
    """
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if kiemTraSoNguyenTo(lst[i]) and kiemTraSoNguyenTo(lst[j]) and lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst


n = nhap_so_luong_phan_tu()
lst = nhap_danh_sach(n)
lst_sorted = sapXepTangDanSoNguyen(lst)
print("Danh sách sau khi sắp xếp:", lst_sorted)
