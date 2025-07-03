# 58. Viết chương trình nhập số nguyên dương n gồm k chữ số, đếm xem n có bao nhiêu chữ số là số nguyên tố.
#đây là hàm kiểm tra số nguyên tố
# Một số nguyên tố là số lớn hơn 1 chỉ có hai ước số là 1 và chính nó.
# Hàm này sẽ lặp qua các số từ 2 đến căn bậc hai của n và kiểm tra xem n có chia hết cho bất kỳ số nào trong khoảng này hay không.
# Nếu có, n không phải là số nguyên tố, ngược lại n là số nguyên tố.
def kiemTraSoNguyenTo(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
# Đây là hàm đếm số lượng chữ số nguyên tố trong một số nguyên dương n
# Hàm này sẽ lặp qua từng chữ số của n, kiểm tra xem chữ số đó có phải là số nguyên tố hay không, và đếm số lượng chữ số nguyên tố.
# Nếu chữ số là số nguyên tố, biến đếm sẽ tăng lên 1.
def demSoNguyenTo(n):
    d = 0
    while n > 0:
        chu_so = n % 10
        if kiemTraSoNguyenTo(chu_so):
            d += 1
        n //= 10
    return d
# Đây là hàm chính để chạy chương trình
# Hàm này sẽ yêu cầu người dùng nhập một số nguyên dương n. 
# Nếu n không hợp lệ (n <= 0), chương trình sẽ yêu cầu nhập lại.
## Sau khi nhập hợp lệ, nó sẽ gọi hàm demSoNguyenTo để đếm số lượng chữ số nguyên tố trong n.
# Cuối cùng, nó sẽ in ra số lượng chữ số nguyên tố.
def main():
    while True:
        n = int(input("Nhập số nguyên dương n (n > 0): "))
        if n > 0:
            break
        print("Vui lòng nhập một số nguyên dương lớn hơn 0.")
    soNguyenTo = demSoNguyenTo(n)
    print(f"Số lượng chữ số nguyên tố trong {n} là: {soNguyenTo}")
main()
