# 60. Viết chương trình nhập số nguyên dương n gồm k chữ số, tìm ước số lẻ lớn nhất của n. Ví dụ: Ước số lẻ lớn nhất của 27 là 9.
# Đây là hàm tìm ước số lẻ lớn nhất của một số nguyên dương n
# Hàm này sẽ lặp qua tất cả các số từ 1 đến n và kiểm tra xem chúng có phải là ước số của n và là số lẻ hay không.
# Nếu là ước số lẻ, nó sẽ cập nhật giá trị max_le nếu ước số lẻ đó lớn hơn giá trị hiện tại của max_le.
# Hàm này sẽ trả về giá trị max_le, nếu không có ước số l
def uocSoLeLonNhat(n):
    max_le = -1
    for i in range(1, n + 1):
        if n % i == 0 and i % 2 != 0:
            max_le = i
    return max_le
# Đây là hàm chính để chạy chương trình
# Hàm này sẽ yêu cầu người dùng nhập một số nguyên dương n.
# Nếu n không hợp lệ (n <= 0), chương trình sẽ yêu cầu nhập lại.
# Sau khi nhập hợp lệ, nó sẽ gọi hàm uocSoLeLonNhat
# để tìm ước số lẻ lớn nhất của n và in ra kết quả.
def main():
    while True:
        n = int(input("Nhập số nguyên dương n (n > 0): "))
        if n > 0:
            break
        print("Vui lòng nhập một số nguyên dương lớn hơn 0.")
    
    max_uoc_so_le = uocSoLeLonNhat(n)
    if max_uoc_so_le != -1:
        print(f"Ước số lẻ lớn nhất của {n} là: {max_uoc_so_le}")
main()