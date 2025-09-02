# 36. Tính S(n) = 1/1² + 1/2² + 1/3² + ... + 1/n².
# Nhập giá trị n từ bàn phím
n = int(input("Nhap n: "))
# Khởi tạo biến sum = 0 để lưu tổng
sum = 0
# Dùng vòng lặp while để tính tổng từ 1 đến n
i = 1
while i <= n:
    # Cộng dồn nghịch đảo bình phương của i vào biến sum
    sum += 1/(i**2)
    # Tăng i lên 1 để tiếp tục vòng lặp
    i += 1
# In ra kết quả
print("S =", sum)
