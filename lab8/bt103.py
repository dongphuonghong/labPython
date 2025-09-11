# 103. Viết hàm ti ́nh tổng các phần tử cực tiểu trong mảng các số nguyên (phần tử cực tiểu là phần tử nhỏ hơn các phần tử xung quanh nó ).Vi ́ dụ :  6 4 2 9 5 3 7 1 5 8
def nhap_so_luong_phan_tu():
    """Nhập số lượng phần tử danh sách (số nguyên dương).

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
    """Nhập danh sách n số nguyên từ bàn phím.

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


def tinh_tong_cuc_tieu(lst):
    """Tính tổng các phần tử cực tiểu trong danh sách.

    Phần tử cực tiểu là phần tử nhỏ hơn các phần tử kề trái và kề phải.

    Args:
        lst (list[int]): Danh sách các số nguyên.

    Returns:
        int: Tổng các phần tử cực tiểu. Trả 0 nếu danh sách có ít hơn 3 phần tử.
    """
    if len(lst) < 3:
        return 0
    tong_cuc_tieu = 0
    for i in range(1, len(lst) - 1):
        if lst[i] < lst[i - 1] and lst[i] < lst[i + 1]:
            tong_cuc_tieu += lst[i]
    return tong_cuc_tieu


n = nhap_so_luong_phan_tu()
lst = nhap_danh_sach(n)
tong_cuc_tieu = tinh_tong_cuc_tieu(lst)
print("Tổng các phần tử cực tiểu trong mảng là:", tong_cuc_tieu)
