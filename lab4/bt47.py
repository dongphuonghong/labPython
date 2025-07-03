# 47. Nhập số nguyên dương n (n>0). Đếm xem có bao nhiêu số hoàn thiện < n.
# Đây là hàm kiểm tra số hoàn thiện
# Theo định nghĩa, số hoàn thiện là số mà tổng các ước số của nó bằng chính nó
def kiem_tra_so_hoan_thien(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong == n
# Đây là hàm đếm số lượng số hoàn thiện nhỏ hơn n
# Hàm này sẽ lặp qua tất cả các số từ 1 đến n-1
def dem_so_hoan_thien(n):
    dem = 0
    for i in range(1, n):
        if kiem_tra_so_hoan_thien(i):
            dem += 1
    return dem
# Đây là hàm main để chạy chương trình nhập dữ liệu và hiển thị kết quả
# Hàm main sẽ yêu cầu người dùng nhập một số nguyên dương n và sau đó gọi hàm đếm số hoàn thiện nhỏ hơn n
# Nếu n không hợp lệ (n <= 0), chương trình sẽ yêu cầu nhập lại
def main():
    while True:
        n = int(input("Nhập số nguyên dương n (n > 0): "))
        if n > 0:
            break
        print("Vui lòng nhập một số nguyên dương lớn hơn 0.")
    so_hoan_thien = dem_so_hoan_thien(n)
    print(f"Số lượng số hoàn thiện nhỏ hơn {n} là: {so_hoan_thien}")
main()