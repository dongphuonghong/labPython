# 45. Nhập số nguyên dương n (n>0). Liệt kê tất cả các số nguyên tố nhỏ hơn n.
# Đây là hàm kiểm tra số nguyên tố.
# Một số nguyên tố là một số lớn hơn 1 chỉ có hai ước số là 1 và chính nó.
# Để kiểm tra số nguyên tố, ta sẽ kiểm tra xem nó có chia hết cho bất kỳ số nào từ 2 đến căn bậc hai của nó hay không.
def kiemTraSoNguyenTo(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
# Đây là hàm liệt kê các số nguyên tố nhỏ hơn n.
# Nó sẽ lặp qua tất cả các số từ 2 đến n-1 và kiểm tra xem số đó có phải là số nguyên tố hay không.
# Nếu là số nguyên tố, nó sẽ in ra số đó.
def lietKeSoNguyenTo(n):
    for i in range(2, n):
        if kiemTraSoNguyenTo(i):
            print(i, end=' ')
# Đây là hàm chính để chạy chương trình.
# Nó sẽ yêu cầu người dùng nhập một số nguyên dương n và sau đó gọi hàm liệt kê các số nguyên tố nhỏ hơn n.
# Nếu người dùng nhập số không hợp lệ (nhỏ hơn hoặc bằng 0), nó sẽ yêu cầu nhập lại.
def main():
    while True:
        n = int(input("Nhập số nguyên dương n (n > 0): "))
        if n > 0:
            break
        print("Vui lòng nhập một số nguyên dương lớn hơn 0.")
    print(f"Các số nguyên tố nhỏ hơn {n} là:")
    lietKeSoNguyenTo(n)
main()