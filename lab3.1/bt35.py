# 35. Tính S(n) = 1³ + 2³ + 3³ + ... + n³.
# Nhập giá trị n từ bàn phím
n = int(input("Nhap n: "))
# Khởi tạo biến sum = 0 để lưu tổng
sum = 0
# Dùng vòng lặp while để tính tổng
i = 1
while i <= n:
    # Cộng dồn giá trị i³ (lập phương của i) vào biến sum
    sum += i**3
    i += 1
# In ra kết quả tổng
print("S = ", sum)
