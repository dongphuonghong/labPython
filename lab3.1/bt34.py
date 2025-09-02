# 34. Tính S(n) = 1 + 1/2 + 1/3 + ... + 1/n (n ≥ 1).
# Tính tổng dãy số điều hòa từ 1 đến 1/n
# Nhập giá trị n từ bàn phím
n = int(input("Nhap n: "))
# Khởi tạo biến sum = 0 để lưu tổng kiểu float
sum = float(0)
# Dùng vòng lặp while để tính tổng từ 1 đến n
i = 1
while i <= n:
    # Mỗi lần lặp cộng 1/i vào biến sum
    sum += 1/i
    # Tăng i lên 1 để tiếp tục lặp
    i += 1
# In ra kết quả
print("Tong S =", sum)
