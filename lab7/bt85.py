#  Bài 85: Tìm số chẵn cuối cùng trong danh sách (không có trả về -1).
def nhap_so_luong_phan_tu():
    """Nhập số lượng phần tử của danh sách.

    Returns:
        int: Số lượng phần tử (>0).
    """
    while True:
        n = int(input("Nhập số lượng phần tử của mảng: "))
        if n > 0:
            break
        print("Số lượng phần tử phải lớn hơn 0. Vui lòng nhập lại.")
    return n


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


def tim_so_chan_cuoi_cung(lst):
    """Tìm số chẵn cuối cùng trong danh sách.

    Args:
        lst (list[int]): Danh sách số nguyên.

    Returns:
        int: Giá trị số chẵn cuối cùng; -1 nếu không có.
    """
    for i in range(len(lst)-1, -1, -1):
        if lst[i] % 2 == 0:
            return lst[i]
    return -1


n = nhap_so_luong_phan_tu()
danh_sach = nhap_danh_sach(n)
ket_qua = tim_so_chan_cuoi_cung(danh_sach)
if ket_qua != -1:
    print("Số chẵn cuối cùng trong danh sách là:", ket_qua)
else:
    print("Không có số chẵn trong danh sách.")
