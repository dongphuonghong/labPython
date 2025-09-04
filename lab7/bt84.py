# Bài 84: In các phần tử là bội của 3 hoặc 5.
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


def in_boi_cua_3_hoac_5(lst):
    """In các phần tử là bội của 3 hoặc 5.

    Args:
        lst (list[int]): Danh sách số nguyên.
    """
    print("Các phần tử là bội của 3 hoặc 5 trong mảng:")
    for x in lst:
        if x % 3 == 0 or x % 5 == 0:
            print(x, end=' ')
    print()  # In dòng mới sau khi in các phần tử


def main():
    """Hàm chính: nhập danh sách và in các phần tử là bội của 3 hoặc 5."""
    n = nhap_so_luong_phan_tu()
    lst = nhap_danh_sach(n)
    in_boi_cua_3_hoac_5(lst)
