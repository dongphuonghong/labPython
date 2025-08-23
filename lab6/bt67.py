# 67. Viết chương trình khởi tạo giá trị các phần tử là 0 cho danh sách (Python list) các số nguyên gồm n phần tử.
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


# Hàm Khoi_tao_danh_sach
# Mô tả: Tạo một danh sách có n phần tử, tất cả phần tử bằng 0.
# Tham số: n (int) — số lượng phần tử.
# Trả về: list[int] — danh sách gồm n phần tử bằng 0.
def Khoi_tao_danh_sach(n):
    return [0] * n
# Chương trình chính
# 1. Nhập số lượng phần tử
# 2. Khởi tạo danh sách với n phần tử bằng 0
# 3. In danh sách ra màn hình


n = nhap_so_luong_phan_tu()
lst = Khoi_tao_danh_sach(n)
print("Danh sách vừa khởi tạo là: ")
print(*lst)
