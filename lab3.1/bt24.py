#24. Viết chương trình nhâp̣ số nguyên dương n. Kiểm tra n có phải là số nguyên tố hay không.
# Số nguyên tố là số chỉ chia hết cho 1 và chính nó
# Nhập số nguyên dương từ bàn phím
n=int (input("Nhập số nguyên dương n: "))   
# Kiểm tra nếu n nhỏ hơn 2 thì không phải là số nguyên tố
if n < 2:
    print(n, "không phải là số nguyên tố")
# dùng vòng lập while  Duyệt từ 2 đến n* 0.5  để kiểm tra tính nguyên tố trong đó *05 là căn bậc hai của n
i=2
while i<=n*0.5:
        if n%i==0:
            print(n, "không phải là số nguyên tố")
            break
        i+=1
else:
    print(n, "là số nguyên tố")