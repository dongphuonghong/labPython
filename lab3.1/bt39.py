# 39. Tính S(n) = 1/1 + 1/(1+2) + 1/(1+2+3) + ... + 1/(1+2+...+n)
# Tạo biến n và nhập giá trị từ bàn phím
n=int(input("Nhap n: "))
# Khởi tạo biến sum để lưu tổng với giá trị ban đầu là 0
sum=float(0)
#khởi tạo biến t để lưu tổng của các số từ 1 đến i
t = 0
# Sử dụng vòng lặp while để tính tổng từ 1 đến n
i=1
while i<=n:
    # Cộng dồn tổng của các số từ 1 đến i vào biến t
    t+=i
    # Cộng nghịch đảo của t vào biến sum
    sum+=1/t
    # Tăng i lên 1 để tiếp tục vòng lặp
    i+=1
print("Tong S(n) la: {:.4f}".format(sum))