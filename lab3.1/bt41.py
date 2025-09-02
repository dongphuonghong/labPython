# 41. Tính S(n) = x² + x⁴ + x⁶ + ... + x^(2n).
# Tạo biến n và nhập giá trị từ bàn phím
n = int(input("Nhap n: "))
# Tạo biến x và nhập giá trị từ bàn phím
x = float(input("Nhap x: "))
# Tạo biến sum và khởi tạo giá trị bằng 0
sum = 0
# Tính x^2 = x*x
x1 = x*x  # x^2
# Khởi tạo biến luythua = x^2
luythua = x1
# Tính tổng các lũy thừa chẵn từ x^2 đến x^(2n) - sử dụng vòng lặp while
i = 1
while i <= n:
    # Cộng dồn lũy thừa vào tổng sum
    sum += luythua
    # Tăng lũy thừa lên bậc tiếp theo (nhân x^2)
    luythua *= x1
    i += 1
# In ra kết quả
print("S(n) = ", sum)
