# 73. Viết chương trình nhập vào danh sách (Python list) các số nguyên và xuất ra màn hình các phần tử là số nguyên tố.
# Hàm nhap_so_luong_phan_tu
# Mô tả: Yêu cầu người dùng nhập số lượng phần tử của danh sách (số nguyên dương).
# Trả về: n (int) — số lượng phần tử (>0).
# Hành vi : Nếu nhập không hợp lệ (<=0), in thông báo lỗi
#           và yêu cầu nhập lại cho đến khi hợp lệ.
def nhap_so_luong_phan_tu():
    """Nhập số lượng phần tử danh sách (số nguyên dương).

    Returns:
        int: Số lượng phần tử (>0).
    """
    while True:
        n = int(input("Nhập số lượng phần tử của mảng: "))
        if n > 0:
            break
        print("Số lượng phần tử phải lớn hơn 0. Vui lòng nhập lại.")
    return n


# Hàm nhap_danh_sach
# Mô tả: Đọc n phần tử từ bàn phím và tạo danh sách các số nguyên.
# Trả về: lst (list[int]) — danh sách chứa n phần tử đã nhập.
# Hành vi: Lặp n lần, mỗi lần yêu cầu nhập một số nguyên và thêm vào danh sách.
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


# Hàm kiemTraSoNguyenTo
# Mô tả: Kiểm tra xem một số nguyên a có phải là số nguyên tố hay không.
# Trả về: True nếu a là số nguyên tố (>=2), False ngược lại.
# Hành vi: Kiểm tra các ước số từ 2 đến sqrt(a).
def kiemTraSoNguyenTo(a):
    """Kiểm tra số nguyên tố.

    Args:
        a (int): Số nguyên cần kiểm tra.

    Returns:
        bool: True nếu là số nguyên tố, False nếu không.
    """
    if a < 2:
        return False
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False
    return True


# Hàm xuat_so_nguyen_to
# Mô tả: In các phần tử trong danh sách là số nguyên tố.
# Hành vi: Duyệt danh sách, sử dụng kiemTraSoNguyenTo để kiểm tra từng phần tử.
def xuat_so_nguyen_to(lst):
    """In các phần tử nguyên tố trong danh sách.

    Args:
        lst (list[int]): Danh sách số nguyên.
    """
    for x in lst:
        if kiemTraSoNguyenTo(x):
            print(x, end=" ")
    print()

# Chương trình chính
# 1. Nhập số lượng phần tử
# 2. Nhập danh sách số nguyên với số lượng phần tử đã cho
# 3. In danh sách phần tử nguyên tố ra màn hình


n = nhap_so_luong_phan_tu()
lst = nhap_danh_sach(n)
print("Các số nguyên tố trong danh sách là: ", end="")
xuat_so_nguyen_to(lst)
