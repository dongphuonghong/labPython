# 40. Tính P(x,n) = x¹ + x² + x³ + ... + xⁿ (tổng các lũy thừa của x từ 1 đến n)
# Tạo biến n và nhập giá trị từ bàn phím
n=int(input("Nhap n: "))
# Tạo biến x và nhập giá trị từ bàn phím
x=float(input("Nhap x: "))
# Khởi tạo biến luythua để lưu lũy thừa, giá trị ban đầu là 1
luythua=1
# Khởi tạo biến sum để lưu tổng các lũy thừa
sum=0
# Sử dụng vòng lặp while để tính tổng từ 1 đến n
i=1
while i<=n:
    # Tính lũy thừa x^i bằng cách nhân dồn x
    luythua*=x
    # Cộng dồn vào tổng sum
    sum+=luythua
    # Tăng i lên 1 để tiếp tục vòng lặp
    i+=1
# In ra kết quả tổng P(x, n)
print(f"Tong P(x,n) la: {sum}")