# 68. Viết chương trình phát sinh ngẫu nhiên danh sách (Python list) các số nguyên âm.
import random


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
# Mô tả: Tạo một danh sách gồm n số nguyên âm được sinh ngẫu nhiên trong phạm vi [-100, -1].
# Tham số: n (int) — số lượng phần tử cần sinh.
# Trả về: lst (list[int]) — danh sách chứa n số nguyên âm ngẫu nhiên.
# Hành vi: Sử dụng random.randint để sinh từng phần tử và thêm vào danh sách.
def nhap_danh_sach(n):
    """Sinh danh sách gồm n số nguyên âm ngẫu nhiên [-100, -1].

    Args:
        n (int): Số lượng phần tử cần sinh.

    Returns:
        list[int]: Danh sách số nguyên âm ngẫu nhiên.
    """
    lst = []
    for i in range(n):
        x = random.randint(-100, -1)
        lst.append(x)
    return lst

# Chương trình chính
# 1. Nhập số lượng phần tử
# 2. Phát sinh danh sách n số nguyên âm ngẫu nhiên
# 3. In danh sách ra màn hình


n = nhap_so_luong_phan_tu()
lst = nhap_danh_sach(n)
print("Danh sách vừa nhập là: ")
print(*lst)
