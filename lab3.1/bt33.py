# 33. Tính S(n) = 1² + 2² + 3² + ... + n² (với n ≥ 0)
# Tính tổng bình phương các số từ 1 đến n
# Nhập giá trị n từ bàn phím
n=int(input("nhap n: "))
# Khởi tạo biến sum = 0 để lưu tổng
sum=0
# Dùng vòng lặp while để tính tổng bình phương từ 1 đến n
i=1
while i <= n:
    # Cộng bình phương của i vào biến sum (i² = i * i)
    sum += i * i
    # Tăng i lên 1 để tiếp tục vòng lặp
    i += 1
# In ra kết quả tổng S(n)
print("Tổng S(n) là:", sum)