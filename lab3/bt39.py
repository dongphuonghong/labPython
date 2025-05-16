# 39.  Tinh,  vơin n S               3 2 1 1 3 2 1 1 2 1 1 1 ) (
# tạo biến n và nhập giá trị từ bàn phím
n=int(input("Nhap n: "))
# khởi tạo biến sum kiểu float để lưu tổng S(n)
sum=float(0)
# tạo biến t để lưu tổng các số từ 1 đến i (tức là 1 + 2 + ... + i)
t = 0
# dùng vòng lặp for để duyệt qua từng số từ 1 đến n
for i in range(1,n+1):
    # cộng dồn vào tổng t
    t+=i
    # cộng 1/t vào sum
    sum+=1/t
# in ra giá trị của biến sum với 4 chữ số thập phân và sử dụng hàm format để định dạng số thập phân
print("Tong S la: {:.4f}".format(sum))