# 29. Tính P(n) = 1 × 3 × 5 × ... × (2n + 1).
# Đây là tích của dãy các số lẻ liên tiếp bắt đầu từ 1 đến (2n + 1)
# Nhập giá trị n từ bàn phím
n = int(input("Nhap n: "))
# Khởi tạo biến tích t = 1 để lưu kết quả tích
t = 1
# Sử dụng vòng lặp for để tính tích các số lẻ từ 1 đến (2n + 1)
for i in range(0, n+1):
    # Tính giá trị lẻ theo công thức (2 * i) + 1
    sum = (2*i)+1
    # Nhân t với giá trị vừa tính
    t *= sum
# In ra kết quả tích của dãy số lẻ
print("Tich cua day so le tu 1 den", (2*n+1), "la:", t)
