# 89. Viết chương tri ̀nh nhập vào mộ t dãy số a gồm n số thực (), nhập vào dãy số b gồm m số thực ().100 n100 mo In ra những phần tử chi ̉ xuất hiện trong dãy a mà không xuất hiện trong dãy b.o In ra những phần tử xuất hiện ở cả hai dãy.


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


def nhap_danh_sach(n):
    """Nhập danh sách gồm n số thực từ bàn phím.

    Args:
        n (int): Số lượng phần tử cần nhập.

    Returns:
        list[float]: Danh sách các số thực đã nhập.
    """
    lst = []
    for i in range(n):
        x = float(input("Nhập phần tử thứ {}: ".format(i+1)))
    lst.append(x)
    return lst


def KiemtraTrungLap(lst, x):
    """Kiểm tra phần tử đã xuất hiện trước đó trong danh sách.

    Args:
        lst (list): Danh sách cần kiểm tra.
        x (Any): Giá trị cần kiểm tra trùng lặp.

    Returns:
        bool: True nếu có trùng lặp, ngược lại False.
    """
    for y in lst:
        if y == x:
            return True
    return False


def kiemTraTonTai(lst, x):
    """Kiểm tra phần tử có tồn tại trong danh sách hay không.

    Args:
        lst (list): Danh sách cần kiểm tra.
        x (Any): Giá trị cần tìm.

    Returns:
        bool: True nếu tồn tại, ngược lại False.
    """
    for y in lst:
        if y == x:
            return True
    return False


def in_a_not_in_b(a, b):
    """In các phần tử chỉ xuất hiện trong a và không xuất hiện trong b.

    Args:
        a (list): Danh sách thứ nhất.
        b (list): Danh sách thứ hai.
    """
    print("Các phần tử chỉ xuất hiện trong mảng a mà không xuất hiện trong mảng b:")
    for x in a:
        if not kiemTraTonTai(b, x) and not KiemtraTrungLap(a, x):
            print(x, end=" ")
    print()


def in_a_and_b(a, b):
    """In các phần tử xuất hiện ở cả hai danh sách a và b.

    Args:
        a (list): Danh sách thứ nhất.
        b (list): Danh sách thứ hai.
    """
    print("Các phần tử xuất hiện ở cả hai mảng a và b:")
    for x in a:
        if kiemTraTonTai(b, x) and not KiemtraTrungLap(a, x):
            print(x, end=" ")
    print()


def main():
    """Chương trình chính: nhập hai mảng và in kết quả theo yêu cầu."""
    print("Nhập mảng a:")
    n = nhap_so_luong_phan_tu()
    a = nhap_danh_sach(n)
    print("Nhập mảng b:")
    m = nhap_so_luong_phan_tu()
    b = nhap_danh_sach(m)
    in_a_not_in_b(a, b)
    in_a_and_b(a, b)


main()
