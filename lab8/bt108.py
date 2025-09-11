# 108. Viết hàm tính giá trị trung bình các phần tử có giá trị là ước số của x trong mảng số nguyên
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


def gia_tri_trung_binh_uoc_so(lst, x):
    """Tính giá trị trung bình các phần tử trong lst là ước số của x.

    Args:
        lst (list[int]): Danh sách các số nguyên.
        x (int): Số nguyên dương để tìm ước số.

    Returns:
        float: Giá trị trung bình các phần tử là ước số của x, hoặc 0 nếu không có.
    """

    tong = 0
    dem = 0
    for num in lst:
        if x % num == 0 and num != 0:
            tong += num
            dem += 1
    if dem == 0:
        return 0
    return tong / dem
# Hàm main
# Mô tả: Chương trình chính để nhập dữ liệu, tính và in kết quả.


def main():
    """Chương trình chính: nhập danh sách và tính trung bình các ước số của x."""
    n = nhap_so_luong_phan_tu()
    lst = nhap_danh_sach(n)
    print("Danh sách đã nhập:", lst)
    x = int(input("Nhập số nguyên dương x: "))
    gia_tri_trung_binh = gia_tri_trung_binh_uoc_so(lst, x)
    if gia_tri_trung_binh == 0:
        print("Không có ước số của x trong danh sách.")
    else:
        print("Giá trị trung bình của các ước số của x trong danh sách là:",
              gia_tri_trung_binh)


main()
