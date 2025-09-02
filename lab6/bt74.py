# 74. Viết chương trình nhập vào danh sách (Python list) các số nguyên và xuất ra màn hình các phần tử là số chính phương nằm tại những vị trí lẻ trong danh sách.
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
# Mô tả : Nhập lần lượt n số nguyên từ bàn phím và lưu vào danh sách.
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


# Hàm kiemTraSoChinhPhuong
# Mô tả : Kiểm tra một số nguyên có phải là số chính phương hay không.
# Trả về: True nếu a là số chính phương, False ngược lại.
# Hành vi: Lấy căn bậc hai kiểu int và so sánh bình phương.
def kiemTraSoChinhPhuong(a):
    """Kiểm tra số chính phương.

    Args:
        a (int): Số nguyên cần kiểm tra.

    Returns:
        bool: True nếu chính phương, False nếu không.
    """
    x = int(a**0.5)
    return x * x == a


# Hàm xuat_so_chinh_phuong
# Mô tả : In các số chính phương nằm tại vị trí lẻ trong danh sách.
# Hành vi: Duyệt danh sách theo chỉ số, nếu chỉ số lẻ và phần tử là số chính phương thì in.
def xuat_so_chinh_phuong(lst):
    """In các số chính phương ở vị trí lẻ trong danh sách.

    Args:
        lst (list[int]): Danh sách số nguyên.
    """
    for i in range(len(lst)):
        if kiemTraSoChinhPhuong(lst[i]) and i % 2 != 0:
            print(lst[i], end=" ")
    print()


# Chương trình chính
# 1. Nhập số lượng phần tử
# 2. Nhập danh sách số nguyên với số lượng phần tử đã cho
# 3. In danh sách các số chính phương nằm tại vị trí lẻ ra màn hình
n = nhap_so_luong_phan_tu()
lst = nhap_danh_sach(n)
print("Các số chính phương nằm tại vị trí lẻ trong danh sách là: ", end="")
xuat_so_chinh_phuong(lst)
