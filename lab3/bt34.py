# 34. Tính S(n) = 1 + 1/2 + 1/3 + ... + 1/n (n ≥ 1).
# Tính tổng dãy số điều hòa từ 1 đến 1/n
# Nhập giá trị n từ bàn phím
n = int(input("Nhap n: "))
# Khởi tạo biến sum = 0 để lưu tổng
sum = float(0)
# Dùng vòng lặp for để tính tổng từ 1 đến n
for i in range(1, n+1):
    # Mỗi lần lặp cộng 1/i vào biến sum
    sum += 1/i
# In ra kết quả
print("S =", sum)
