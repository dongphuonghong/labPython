# 62. Viết chương trình nhập vào số nguyên dương n, in ra màn hình n số nguyên tố đầu tiên.
# Đây là hàm kiểm tra xem một số nguyên dương n có phải là số nguyên tố hay không
# Một số nguyên tố là một số lớn hơn 1 chỉ có hai ước số là 1 và chính nó.
# Hàm này sẽ lặp qua các số từ 2 đến căn bậc hai của n và kiểm tra xem n có chia hết cho bất kỳ số nào trong khoảng này hay không.
# Nếu có, n không phải là số nguyên tố, ngược lại n là số nguyên
def kiemTraSoNguyenTo(n):
    """Kiểm tra số nguyên tố.

    Args:
        n (int): Số nguyên cần kiểm tra.

    Returns:
        bool: True nếu nguyên tố, False nếu không.
    """
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
# Đây là hàm liệt kê n số nguyên tố đầu tiên.
# Hàm này sẽ lặp từ 2 đến vô hạn, kiểm tra từng số xem nó có phải là số nguyên tố hay không.
# Nếu có, nó sẽ in ra số đó và tăng biến đếm d lên 1


def lietKeSoNguyenTo(n):
    """In n số nguyên tố đầu tiên.

    Args:
        n (int): Số lượng số nguyên tố cần in.
    """
    d = 0
    i = 2
    while d < n:
        if kiemTraSoNguyenTo(i):
            print(i, end=' ')
            d += 1
        i += 1
# Đây là hàm chính để chạy chương trình
# Hàm này sẽ yêu cầu người dùng nhập một số nguyên dương n (n > 0)
# Nếu n không hợp lệ, nó sẽ yêu cầu nhập lại.
# Sau khi nhập hợp lệ, nó sẽ gọi hàm lietKeSoNguyenTo để liệt kê n số nguyên tố đầu tiên.
# Cuối cùng, nó sẽ in ra kết quả.


def main():
    """Hàm chính: nhập n và in n số nguyên tố đầu tiên."""
    while True:
        n = int(input("Nhập số nguyên dương n (n > 0): "))
        if n > 0:
            break
        print("Vui lòng nhập một số nguyên dương lớn hơn 0.")
    print(f"Các số nguyên tố đầu tiên là: ", end='')
    lietKeSoNguyenTo(n)


main()
