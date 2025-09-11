# 102. Viết hàm ti ́nh tổng các phần tử cực đại trong danh sách các số nguyên (phần tử cực đại là phần tử lớn hơn các phần tử xung quanh nó ).Vi ́ dụ :  1 5 2 6 3 5 1 8 6
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


# Hàm nhap_danh_sach
# Mô tả: Đọc n phần tử từ bàn phím và tạo danh sách các số nguyên.
# Tham số: n (int) — số lượng phần tử cần nhập.
# Trả về: lst (list[int]) — danh sách chứa n phần tử đã nhập.
# Hành vi: Lặp n lần, mỗi lần yêu cầu nhập một số nguyên và thêm vào danh sách.
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


def tinh_tong_cuc_dai(lst):
    """Tính tổng các phần tử cực đại trong danh sách.

    Phần tử cực đại là phần tử lớn hơn các phần tử kề trái và kề phải.

    Args:
        lst (list[int]): Danh sách các số nguyên.

    Returns:
        int: Tổng các phần tử cực đại. Trả 0 nếu danh sách có ít hơn 3 phần tử.
    """
    if len(lst) < 3:
        return 0

    tong_cuc_dai = 0
    for i in range(1, len(lst) - 1):
        if lst[i] > lst[i - 1] and lst[i] > lst[i + 1]:
            tong_cuc_dai += lst[i]
    return tong_cuc_dai


n = nhap_so_luong_phan_tu()
lst = nhap_danh_sach(n)
tong_cuc_dai = tinh_tong_cuc_dai(lst)
print("Tổng các phần tử cực đại trong danh sách là:", tong_cuc_dai)
