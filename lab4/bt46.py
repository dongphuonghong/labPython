# 46. Nhập số nguyên dương n (n>0). Liệt kê n số chính phương đầu tiên.
# Số chính phương là số có căn bậc hai là một số nguyên.
# Ví dụ: 1, 4, 9, 16, 25...
# Đây là hàm kiểm tra số chính phương
def kiemTraSoChinhPhuong(n):
    """Kiểm tra một số có phải số chính phương.

    Args:
        n (int): Số nguyên cần kiểm tra.

    Returns:
        bool: True nếu là số chính phương, False nếu không.
    """
    x = int(n**0.5)
    return x * x == n
# Đây là hàm liệt kê n số chính phương đầu tiên
# Hàm này sẽ lặp từ 1 đến vô hạn, kiểm tra từng số xem nó có phải là số chính phương hay không
# Nếu có, nó sẽ in ra số đó và tăng biến đếm d lên 1


def lietKeSoChinhPhuong(n):
    """In n số chính phương đầu tiên.

    Args:
        n (int): Số lượng số chính phương cần in.
    """
    d = 0
    i = 1
    while d < n:
        if kiemTraSoChinhPhuong(i):
            print(i, end=' ')
            d += 1
        i += 1
# Đây là hàm main để chạy chương trình
# Hàm này sẽ yêu cầu người dùng nhập một số nguyên dương n (n > 0)
# Nếu n không hợp lệ, nó sẽ yêu cầu nhập lại


def main():
    """Hàm chính: nhập n và in n số chính phương đầu tiên."""
    while True:
        n = int(input("Nhập số nguyên dương n (n > 0): "))
        if n > 0:
            break
        else:
            print("Vui lòng nhập một số nguyên dương lớn hơn 0.")
    print(f"Các số chính phương đầu tiên là: ", end='')
    lietKeSoChinhPhuong(n)


main()
