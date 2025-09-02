# 54. Viết chương trình tính tổng nghịch đảo của n giai thừa.
# Hàm này tính tổng nghịch đảo của giai thừa từ 2 đến n.
# Đây là hàm tính tổng nghịch đảo của giai thừa từ 2 đến n
def tongNghichDaoGiaiThua(n):
    """Tính tổng các nghịch đảo giai thừa từ 2! đến n!.

    Args:
        n (int): Số nguyên dương n.

    Returns:
        float: Tổng 1/2! + 1/3! + ... + 1/n! (0 nếu n < 2).
    """
    tong = 0
    giai_thua = 1
    for i in range(2, n + 1):
        giai_thua *= i
        tong += 1 / giai_thua
    return tong
# Đây là hàm main để chạy chương trình nhập dữ liệu và hiển thị kết quả
# Hàm main sẽ gọi hàm tongNghichDaoGiaiThua để tính tổng nghịch đảo giai thừa


def main():
    """Hàm chính: nhập n và in tổng nghịch đảo giai thừa."""
    while True:
        n = int(input("Nhập số nguyên dương n: "))
        if n > 0:
            break
        print("Vui lòng nhập một số nguyên dương lớn hơn 0.")
        tong_nghich_dao = tongNghichDaoGiaiThua(n)
        print(f"Tổng nghịch đảo giai thừa của {n} là: {tong_nghich_dao}")


main()
