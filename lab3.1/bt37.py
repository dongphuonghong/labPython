# 37. Tính S(n) = 1 + 1/1! + 1/2! + 1/3! + ... + 1/n! (tổng nghịch đảo giai thừa)
# Nhập giá trị n từ bàn phím
n=int(input("nhập n: "))
# Khởi tạo biến giaithua để lưu giá trị giai thừa, bắt đầu bằng 1
giaithua=1
# Khởi tạo biến sum để lưu tổng, bắt đầu bằng 1 (số hạng đầu tiên)
sum = 1
# Dùng vòng lặp while để tính tổng nghịch đảo giai thừa từ 1! đến n!
i=1
while i<=n:
    # Tính giai thừa tại bước i bằng cách nhân dồn với i
    giaithua*=i
    # Cộng dồn nghịch đảo giai thừa vào tổng sum
    sum+=1/giaithua
    # Tăng i lên 1 để tiếp tục vòng lặp
    i+=1
# In ra kết quả tổng S(n)
print("sum =",sum)