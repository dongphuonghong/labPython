# 32. Tính S(n) = 1! + 2! + 3! + ... + n! (với n ≥ 0)
# Tính tổng các giai thừa từ 1! đến n!
# Nhập n từ bàn phím
n=int(input("nhập n: "))
# Khởi tạo biến giaithua = 1 để tính giai thừa từng bước
giaithua=1
# Khởi tạo biến sum để lưu tổng = 0
sum=0
# Duyệt từ 1 đến n để tính các giai thừa
i=1
while i <=n:
    # Tính giai thừa i bằng cách nhân dồn
    giaithua *= i
    # Cộng dồn giai thừa vào tổng
    sum += giaithua
    # Tăng i lên 1 để tiếp tục vòng lặp
    i += 1
# In ra kết quả tổng
print("sum =", sum)