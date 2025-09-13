# 112. Viết hàm sắp xếp các phần tử chẵn giảm dần.
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


def sap_xep_chan_giam_dan(lst):
    """Sắp xếp giảm dần các phần tử chẵn trong danh sách.

    Các phần tử lẻ giữ nguyên vị trí tương đối; chỉ những phần tử chẵn được so sánh và hoán đổi để tạo thứ tự giảm dần.

    Args:
        lst (list[int]): Danh sách các số nguyên.

    Returns:
        list[int]: Danh sách sau khi các phần tử chẵn đã được sắp xếp giảm dần tại chỗ.
    """
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] % 2 == 0 and lst[j] % 2 == 0 and lst[i] < lst[j]:
                lst[i], lst[j] = lst[j], lst[i]  # Hoán đổi hai phần tử
    return lst


n = nhap_so_luong_phan_tu()
lst = nhap_danh_sach(n)
lst_sorted = sap_xep_chan_giam_dan(lst)
print("Danh sách sau khi sắp xếp:", lst_sorted)
