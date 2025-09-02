# 38. Tính S(n) = 1 + (1+2)/2! + (1+2+3)/3! + ... + (1+2+...+n)/n!.
# CÁCH 1: Dùng while loop để tính tổng và giai thừa
# Nhập giá trị n từ bàn phím
n = int(input("Nhap n: "))
# Khởi tạo biến sum = 1 để bắt đầu với số hạng đầu tiên là 1
sum = float(1)  # Bắt đầu với số hạng đầu tiên là 1
# Dùng vòng lặp while để tính tổng từ 2 đến n
i = 2
while i <= n:
    # tạo biến tử số với giá trị=0
    tu_so = 0
    # dùng vòng lặp while để tính tổng từ 1 đến i
    j = 1
    while j <= i:
        # Cộng dồn giá trị j vào biến tử số
        tu_so += j
        # Tăng j lên 1 để tiếp tục vòng lặp
        j += 1
        # tạo biến giai thừa với giá trị=1
    giaithua = 1
    # Dùng vòng lặp while để tính giai thừa từ 1 đến i
    k = 1
    while k <= i:
        # Nhân dồn giá trị k vào biến giai thừa
        giaithua *= k
        # Tăng k lên 1 để tiếp tục vòng lặp
        k += 1
    # Cộng phần tử tu_so/giaithua vào tổng sum
    sum += tu_so/giaithua
    # Tăng i lên 1 để tiếp tục vòng lặp
    i += 1
# In ra kết quả tổng S(n)
print("S(n) = ", sum)
# CÁCH 2: Dùng công thức toán học để tính tử số, tối ưu hơn cách đầu tiên (chỉ dùng 2 vòng lặp)
""" 
# 38. Tính S(n) = 1 + (1+2)/2! + (1+2+3)/3! + ... + (1+2+...+n)/n!
# Nhập giá trị n từ bàn phím
n=int(input("Nhap n: "))
# Khởi tạo biến sum = 1 để bắt đầu với số hạng đầu tiên là 1
sum=float(1)  # Bắt đầu với số hạng đầu tiên là 1
# Dùng vòng lặp while để tính tổng từ 2 đến n
i=2
while i<=n:
    # Tính tử số là tổng từ 1 đến i
    tu_so = i * (i + 1) // 2  
    # tạo biến giaithua để tính giai thừa, giá trị = 1
    giaithua = 1
    # Dùng vòng lặp while để tính giai thừa i!
    j=1    while j<=i:
        # Tính giai thừa bằng cách nhân dồn với j
        giaithua*=j
        # Tăng j lên 1 để tiếp tục vòng lặp
        j+=1
    # Cộng phần tử tu_so/i! vào tổng
    sum += tu_so / giaithua    # Tăng i lên 1 để tiếp tục vòng lặp
    i+=1
# In ra kết quả tổng S(n)
print("S(n) = ", sum)
 """
