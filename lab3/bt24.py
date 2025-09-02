# 24. Viết chương trình nhập số nguyên dương n; kiểm tra n có phải là số nguyên tố hay không.
# Số nguyên tố là số chỉ chia hết cho 1 và chính nó
# Nhập số nguyên dương từ bàn phím
n = int(input("Nhap n: "))
# Kiểm tra nếu n nhỏ hơn 2 thì không phải là số nguyên tố
if n < 2:
    print(n, "khong phai la so nguyen to")
# Duyệt từ 2 đến căn bậc hai của n
for i in range(2, int(n**0.5)+1):
    # kiểm tra nếu n chia hết cho i thì n không phải là số nguyên tố
    if n % i == 0:
        print(n, "khong phai la so nguyen to")
        # Thoát khỏi vòng lặp nếu tìm được ước
        break
else:
    # Nếu không có ước nào chia hết, n là số nguyên tố
    print(n, "la so nguyen to")
