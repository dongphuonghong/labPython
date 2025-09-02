# 70. Viết chương trình nhập danh sách (Python list) các số nguyên và xuất các phần tử âm trong danh sách.
# Hàm nhap_so_luong_phan_tu
# Mô tả: Yêu cầu người dùng nhập số lượng phần tử của danh sách (số nguyên dương).
# Tham số: không có.
# Trả về: n (int) — số lượng phần tử (>0).
# Hành vi: Nếu nhập không hợp lệ (<=0), in thông báo và yêu cầu nhập lại cho đến khi hợp lệ.
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
# Mô tả: Nhập lần lượt n số nguyên từ bàn phím và lưu vào danh sách.
# Tham số: n (int) — số lượng phần tử cần nhập.
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


# Hàm phan_tu_am
# Mô tả: In tất cả các phần tử âm trong danh sách.
# Tham số: lst (list[int]) — danh sách các số nguyên.
# Hành vi: Duyệt danh sách, nếu phần tử < 0 thì in ra.
def phan_tu_am(lst):
    """In các phần tử âm trong danh sách.

    Args:
        lst (list[int]): Danh sách số nguyên.
    """
    for x in lst:
        if x < 0:
            print(x, end=" ")
    print()
# Chương trình chính
# 1. Nhập số lượng phần tử
# 2. Nhập danh sách số nguyên với số lượng phần tử đã cho
# 3. In danh sách các phần tử âm ra màn hình


n = nhap_so_luong_phan_tu()
lst = nhap_danh_sach(n)
print("Các phần tử âm trong danh sách là: ", end="")
phan_tu_am(lst)
