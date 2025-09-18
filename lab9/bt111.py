# 111. Viết hàm sắp xếp các phần tử lẻ tăng dần.
def nhap_so_luong_phan_tu():
    """Nhập số lượng phần tử của danh sách.

    Yêu cầu người dùng nhập số lượng phần tử (số nguyên dương) cho danh sách.

    Returns:
        int: Số lượng phần tử (> 0).
    """
    while True:
        n = int(input("Nhập số lượng phần tử của mảng: "))
        if n > 0:
            break
        print("Số lượng phần tử phải lớn hơn 0. Vui lòng nhập lại.")
    return n


def nhap_danh_sach(n):
    """Nhập danh sách gồm n số nguyên từ bàn phím.

    Args:
        n (int): Số lượng phần tử cần nhập (n > 0).

    Returns:
        list[int]: Danh sách các số nguyên được nhập.
    """
    lst = []
    for i in range(n):
        x = int(input("Nhập phần tử thứ {}: ".format(i+1)))
        lst.append(x)
    return lst


def sap_xep_le_tang_dan(lst):
    """Sắp xếp tăng dần các phần tử lẻ trong danh sách.

    Các phần tử chẵn giữ nguyên vị trí tương đối; chỉ những phần tử lẻ được so sánh và hoán đổi.

    Args:
        lst (list[int]): Danh sách các số nguyên.

    Returns:
        list[int]: Danh sách sau khi các phần tử lẻ đã được sắp xếp tăng dần tại chỗ.
    """
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] % 2 != 0 and lst[j] % 2 != 0 and lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]  # Hoán đổi hai phần tử
    return lst


n = nhap_so_luong_phan_tu()
lst = nhap_danh_sach(n)
lst_sorted = sap_xep_le_tang_dan(lst)
print("Danh sách sau khi sắp xếp:", lst_sorted)
