    # 29. Tinh,  vơi) 1 2 ( 5 . 3 . 1 ) (   n n P 
# Đây là tích của dãy các số lẻ liên tiếp bắt đầu từ 1 đến (2n + 1)
# tạo biến n nhập giá trị từ bàn phím
n=int (input("Nhap n: "))
# Khởi tạo biến t với giá trị 1 (biến lưu tích)
t=1
# sử dụng vòng lặp for để tính tích của dãy số từ 1 đến n
for i in range(0,n+1):
        # Tính giá trị lẻ theo công thức (2 * i) + 1
    sum=(2*i)+1
        # Nhân t với giá trị vừa tính
t*=sum
# in ra kết quả
print("tich cua day so tu 1 den n la: ",t)    