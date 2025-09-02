# 59. Viết chương trình nhập số nguyên dương n gồm k chữ số, tính tổng các ước số của n. Ví dụ: Nhập n=6, Tổng các ước số từ 1 đến n: 1+2+3+6=12.
# Đây là hàm tính tổng các ước số của một số nguyên dương n
# Hàm này sẽ lặp qua tất cả các số từ 1 đến n và kiểm tra xem chúng có phải là ước số của n hay không.
# Nếu là ước số, nó sẽ cộng vào tổng.
def tongUocSo(n):
    """Tính tổng các ước số của n.

    Args:
        n (int): Số nguyên dương.

    Returns:
        int: Tổng các ước số của n.
    """
    tong = 0
    for i in range(1, n + 1):
        if n % i == 0:
            tong += i
    return tong
# Đây là hàm chính để chạy chương trình
# Hàm này sẽ yêu cầu người dùng nhập một số nguyên dương n.
# Nếu n không hợp lệ (n <= 0), chương trình sẽ yêu cầu nhập lại.
# Sau khi nhập hợp lệ, nó sẽ gọi hàm tongUocSo để tính tổng
# các ước số của n và in ra kết quả.


def main():
    """Hàm chính: nhập n và in tổng các ước số."""
    while True:
        n = int(input("Nhập số nguyên dương n (n > 0): "))
        if n > 0:
            break
        print("Vui lòng nhập một số nguyên dương lớn hơn 0.")
    tong_uoc_so = tongUocSo(n)
    print(f"Tổng các ước số của {n} là: {tong_uoc_so}")


main()
