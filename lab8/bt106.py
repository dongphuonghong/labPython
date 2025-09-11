# 106. Viết hàm ti ́nh giá tri ̣ trung bi ̀nh các số hoàn thiện trong mảng các số nguyên.
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


def kiem_tra_so_hoan_thien(x):
    """Kiểm tra số hoàn thiện.

    Args:
        x (int): Số nguyên dương cần kiểm tra.

    Returns:
        bool: True nếu là số hoàn thiện, False nếu không.
    """
    if x < 1:
        return False
    tong = 0
    for i in range(1, x//2 + 1):
        if x % i == 0:
            tong += i
    return tong == x


def tinh_gia_tri_trung_binh(lst):
    """Tính giá trị trung bình của các số hoàn thiện trong danh sách.

    Args:
        lst (list[int]): Danh sách các số nguyên.

    Returns:
        float: Giá trị trung bình của các số hoàn thiện, hoặc 0 nếu không có số hoàn thiện.
    """
    tong = 0
    dem = 0
    for x in lst:
        if kiem_tra_so_hoan_thien(x):
            tong += x
            dem += 1
    if dem == 0:
        return 0
    return tong / dem


def main():
    """Chương trình chính: nhập dữ liệu và in giá trị trung bình số hoàn thiện."""
    n = nhap_so_luong_phan_tu()
    lst = nhap_danh_sach(n)
    gia_tri_trung_binh = tinh_gia_tri_trung_binh(lst)
    if gia_tri_trung_binh == 0:
        print("Không có số hoàn thiện trong mảng.")
    else:
        print("Giá trị trung bình của các số hoàn thiện trong mảng là:",
              gia_tri_trung_binh)


main()
