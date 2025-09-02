# 29. Tính P(n) = 1 × 3 × 5 × ... × (2n + 1).
# Đây là tích của dãy các số lẻ liên tiếp bắt đầu từ 1 đến (2n + 1)
# Nhập giá trị n từ bàn phím
n = int(input("Nhap n: "))
# Khởi tạo biến tích t = 1 để lưu kết quả tích
t = 1
# Dùng vòng lặp while để tính tích các số lẻ từ 1 đến (2n + 1)
i = 0
while i <= n:
    # Tính số lẻ tại vị trí i, công thức là (2*i + 1)
    sum = (2*i)+1
    # Nhân dồn vào biến tích t
    t *= sum
    # Tăng i lên 1 để tiếp tục vòng lặp
    i += 1
# In ra kết quả tích của dãy số lẻ
print("Tich cua day so le tu 1 den", (2*n+1), "la:", t)
