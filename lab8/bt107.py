#  107. Viết hàm tính giá trị trung bình các phần tử có giá trị lẻ trong danh sách số nguyên.
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


def kiem_tra_so_le(x):
    """Kiểm tra số lẻ.

    Args:
        x (int): Số nguyên cần kiểm tra.

    Returns:
        bool: True nếu là số lẻ, False nếu không.
    """
    return x % 2 != 0


def tinh_gia_tri_trung_binh_cac_so_le(lst):
    """Tính giá trị trung bình của các số lẻ trong danh sách.

    Args:
        lst (list[int]): Danh sách các số nguyên.

    Returns:
        float: Giá trị trung bình của các số lẻ, hoặc 0 nếu không có số lẻ.
    """
    tong = 0
    dem = 0
    for x in lst:
        if kiem_tra_so_le(x):
            tong += x
            dem += 1
    if dem == 0:
        return 0
    return tong / dem


def main():
    """Chương trình chính: nhập danh sách và in giá trị trung bình số lẻ."""
    n = nhap_so_luong_phan_tu()
    lst = nhap_danh_sach(n)
    print("Danh sách đã nhập:", lst)
    gia_tri_trung_binh = tinh_gia_tri_trung_binh_cac_so_le(lst)
    if gia_tri_trung_binh == 0:
        print("Không có số lẻ trong danh sách.")
    else:
        print("Giá trị trung bình của các số lẻ trong danh sách là:",
              gia_tri_trung_binh)


main()
