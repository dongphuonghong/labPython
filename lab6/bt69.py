# 69. Viết chương trình phát sinh ngẫu nhiên danh sách (Python list) các số nguyên sao cho danh sách có thứ tự tăng dần (không sắp xếp).
import random


# Hàm nhap_so_luong_phan_tu
# Mô tả: Yêu cầu người dùng nhập số lượng phần tử của danh sách (số nguyên dương).
# Tham số: không có.
# Trả về: n (int) — số lượng phần tử (>0).
# Hành vi: Nếu nhập không hợp lệ (<=0), in thông báo và yêu cầu nhập lại cho đến khi hợp lệ.

def nhap_so_luong_phan_tu():
    while True:
        n = int(input("Nhập số lượng phần tử của mảng: "))
        if n > 0:
            break
        print("Số lượng phần tử phải lớn hơn 0. Vui lòng nhập lại.")
    return n


# Hàm nhap_danh_sach
# Mô tả: Sinh một danh sách gồm n số nguyên tăng dần bằng cách sinh phần tử đầu
# và sau đó cộng thêm một số ngẫu nhiên dương cho phần tử trước đó.
# Tham số: n (int) — số lượng phần tử cần sinh.
# Trả về: lst (list[int]) — danh sách gồm n phần tử theo thứ tự tăng dần.
# Hành vi: Sinh ngẫu nhiên phần tử đầu tiên, sau đó mỗi phần tử tiếp theo
#           bằng phần tử trước cộng thêm một số dương ngẫu nhiên.
def nhap_danh_sach(n):
    lst = []
    x = random.randint(1, 100)
    lst.append(x)
    for i in range(n, -1):
        x = lst[-1] + random.randint(1, 100)
        lst.append(x)
    return lst


# Chương trình chính
# 1. Nhập số lượng phần tử
# 2. Phát sinh danh sách số nguyên tăng dần với phần tử đã cho
# 3. In danh sách ra màn hình
n = nhap_so_luong_phan_tu()
lst = nhap_danh_sach(n)
print("Danh sách vừa nhập là: ")
print(*lst)
