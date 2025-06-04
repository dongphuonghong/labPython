# 31. Tính S(n) = 1 - 2 + 3 - 4 + ... + (-1)^(n+1) * n
# Tính tổng xen kẽ dấu của dãy số từ 1 đến n (số lẻ dương, số chẵn âm)
# Nhập giá trị n từ bàn phím
n=int(input("Nhap n lon hon 0: "))
# Tạo biến sum với giá trị ban đầu là 0
sum=0
# Dùng vòng lặp while để duyệt qua các số từ 1 đến n
i=1
while i <= n:
    # Kiểm tra nếu i là số chẵn, thì trừ i vào sum
    if i % 2 == 0:
        sum -= i 
    # Nếu i là số lẻ, thì cộng i vào sum
    else:
        sum += i 
    # Tăng i lên 1 để tiếp tục vòng lặp
    i+= 1
# In kết quả
print("Tong S(n) =", sum)