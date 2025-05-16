#24. Viết chương trình nhâp̣ số nguyên dương n. Kiểm tra n có phải là số nguyên tố hay không.
# Số nguyên tố là số chỉ chia hết cho 1 và chính nó
# Nhập số nguyên dương từ bàn phím
n=int(input("Nhap n: "))    
    # Duyệt từ 2 đến căn bậc hai của n (đã làm tròn xuống)
for i in range(2,n,int(n**0.5)+1):
    #kiểm tra Nếu tồn tại i chia hết cho n thì n không phải là số nguyên tố
    if n%i==0:
        print(n,"khong phai la so nguyen to")
        # Thoát khỏi vòng lặp nếu tìm được ước
        break
    #trường hợp còn lại n là số nguyên tố
else:
        # Nếu không có ước nào chia hết, n là số nguyên tố
        print(n,"la so nguyen to")
        # cách 2 dùng thư viện math và hàm math.sqrt để tính căn bậc 2 của n
        """
        import math
# Nhập số nguyên dương từ bàn phím
n=int(input("Nhap n: "))    
    # Duyệt từ 2 đến căn bậc hai của n (dùng math.sqrt để lấy căn bậc 2)
for i in range(2,int(math.sqrt(n))+1):
# kiểm tra nếu n chia hết cho i thì n không phải là số nguyên tố
    if n%i==0:
        print(n,"khong phai la so nguyen to")
        # Thoát khỏi vòng lặp nếu tìm được ước
        break
else:
        # Nếu không có ước nào chia hết, n là số nguyên tố
        print(n,"la so nguyen to")
        """