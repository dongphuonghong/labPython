# 28. Tính n! với n ≥ 0
# Giai thừa của n là tích của tất cả các số nguyên dương từ 1 đến n
# Nhập giá trị n từ bàn phím
n=int(input("Nhap n: "))
# Kiểm tra nếu n là số âm thì không tính được giai thừa
if n<0:
    print("Khong tinh duoc giai thua")
else:
    # Khởi tạo biến giaithua = 1 để lưu giá trị giai thừa
    giaithua=1
    # Dùng vòng lặp while để tính giai thừa
    i=2
    while i<=n:
        # Nhân dồn giaithua với i
        giaithua*=i
        # Tăng i lên 1 để tiếp tục tính giai thừa
        i+=1
    # In ra kết quả giai thừa của n
    print("Giai thua cua",n,"la",giaithua)