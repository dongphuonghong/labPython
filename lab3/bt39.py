# 39. Tính S(n) = 1/1 + 1/(1+2) + 1/(1+2+3) + ... + 1/(1+2+...+n)
# Tạo biến n và nhập giá trị từ bàn phím
n=int(input("Nhap n: "))
# Khởi tạo biến sum kiểu float để lưu tổng S(n)
sum=float(0)
# Tạo biến t để lưu tổng các số từ 1 đến i (tức là 1 + 2 + ... + i)
t = 0
# Dùng vòng lặp for để duyệt qua từng số từ 1 đến n
for i in range(1,n+1):
    # Cộng dồn vào tổng t
    t+=i
    # Cộng 1/t vào sum
    sum+=1/t
# In ra giá trị của biến sum với 4 chữ số thập phân và sử dụng hàm format để định dạng số thập phân
print("Tong S(n) la: {:.4f}".format(sum))