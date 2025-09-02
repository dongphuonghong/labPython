# 65. Viết chương trình nhập vào một số nguyên n gồm tối đa 10 chữ số (4 bytes). In ra màn hình giá trị nhị phân của số trên. (Hướng dẫn: chia lấy dư cho 2 và xuất theo thứ tự ngược lại).
# Đây là hàm chuyển đổi một số nguyên dương n sang giá trị nhị phân.
# Hàm này sẽ lặp qua n, chia n cho 2 và lấy phần dư
# để xây dựng chuỗi nhị phân. Kết quả sẽ được trả về dưới dạng chuỗi.
# Hàm này sẽ trả về giá trị nhị phân của n dưới dạng chuỗi.
def chuyenDoiNhiPhan(n):
    """Chuyển số nguyên sang nhị phân.

    Args:
        n (int): Số nguyên không âm.

    Returns:
        str: Biểu diễn nhị phân.
    """
    if n == 0:
        return "0"
    nhi_phan = ""
    while n > 0:
        nhi_phan = str(n % 2) + nhi_phan
        n //= 2
    return nhi_phan
# Đây là hàm chính để chạy chương trình
# Hàm này sẽ yêu cầu người dùng nhập một số nguyên dương n (0 <= n < 2^32).
# Nếu n không hợp lệ (n < 0 hoặc n >= 2^32),
# chương trình sẽ yêu cầu nhập lại.
# Sau khi nhập hợp lệ, nó sẽ gọi hàm chuyenDoiNhiPhan để chuyển đổi n sang giá trị nhị phân
# và in ra kết quả.


def main():
    """Hàm chính: nhập n và in biểu diễn nhị phân."""
    while True:
        n = int(input("Nhập số nguyên dương n (0 <= n < 2^32): "))
        if 0 <= n < 2**32:
            break
        print("Vui lòng nhập một số nguyên dương trong khoảng từ 0 đến 2^32 - 1.")
    nhi_phan = chuyenDoiNhiPhan(n)
    print(f"Giá trị nhị phân của {n} là: {nhi_phan}")


main()
