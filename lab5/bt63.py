# 63. Viết chương trình nhập vào số nguyên dương n, in ra màn hình các số hoàn thiện nhỏ hơn 5000.
# Đây là hàm kiểm tra xem một số nguyên dương n có phải là số hoàn thiện hay không.
# Một số hoàn thiện là một số mà tổng các ước số của nó (không bao gồm chính nó) bằng chính nó.
# Hàm này sẽ lặp qua tất cả các số từ 1 đến n-1 và kiểm tra xem chúng có phải là ước số của n hay không.
# Nếu là ước số, nó sẽ cộng vào tổng. Cuối cùng, nó sẽ so sánh tổng với n và trả về True nếu chúng bằng nhau, ngược lại trả về False.
def kiemTraSoHoanThien(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong == n
# Đây là hàm chính để chạy chương trình
# Hàm này sẽ in ra các số hoàn thiện nhỏ hơn 5000.  
# Nó sẽ lặp qua tất cả các số từ 1 đến 4999 và kiểm tra xem số đó có phải là số hoàn thiện hay không.
# Nếu có, nó sẽ in ra số đó.
def main():
    print("Các số hoàn thiện nhỏ hơn 5000 là: ")
    for i in range(1, 5000):
        if kiemTraSoHoanThien(i):
            print(i, end=' ')
    print()
main()