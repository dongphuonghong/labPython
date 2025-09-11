# 101. Viết hàm ti ́nh tổng các phần tử chia hết cho 5 có trong danh sách.
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


def tinh_tong_phan_tu_chia_5(lst):
    """Tính tổng các phần tử chia hết cho 5 trong danh sách.

    Args:
        lst (list[int]): Danh sách các số nguyên.

    Returns:
        int: Tổng các phần tử chia hết cho 5.
    """
    tong = 0
    for i in lst:
        if i % 5 == 0:
            tong += i
    return tong


n = nhap_so_luong_phan_tu()
lst = nhap_danh_sach(n)
print("Tổng các phần tử chia hết cho 5 là:", tinh_tong_phan_tu_chia_5(lst))
