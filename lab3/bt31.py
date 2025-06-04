# 31. Tính S(n) = 1 - 2 + 3 - 4 + ... + (-1)^(n+1) * n
# Tính tổng xen kẽ dấu của dãy số từ 1 đến n (số lẻ dương, số chẵn âm)
# Nhập giá trị n từ bàn phím
n=int(input("Nhap n: "))
# Khởi tạo biến sum với giá trị ban đầu là 0
sum=0
# Dùng vòng lặp for để duyệt qua các số từ 1 đến n
for i in range(1,n+1):
    # Kiểm tra nếu i là số chẵn, thì trừ i vào sum
    if i%2==0:
        sum-=i
    # Nếu i là số lẻ, thì cộng i vào sum
    else:
        sum+=i
# In kết quả S(n) ra màn hình
print("S(n) =", sum)