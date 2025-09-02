# 30. Tính S(n) = (1 + 3 + 5 + ... + (2n+1)) × (1 + 2 + 3 + ... + n).
# Tích của tổng các số lẻ và tổng các số tự nhiên từ 1 đến n
# Nhập giá trị n từ bàn phím
n = int(input("Nhap n: "))
# Khởi tạo biến tổng các số lẻ và tổng các số tự nhiên
tong_so_le = 0
tong_tu_nhien = 0
# Sử dụng vòng lặp while để tính tổng các số lẻ từ 1 đến (2n+1)
i = 0
while i <= n:
    # Tính số lẻ tại vị trí i, công thức là 2*i + 1
    # Cộng dồn vào biến tong_so_le
    tong_so_le += 2*i + 1
    # Tăng i lên 1 để tiếp tục vòng lặp
    i += 1
# Tính tổng các số tự nhiên từ 1 đến n
j = 1
while j <= n:
    # Cộng dồn giá trị j vào biến tong_tu_nhien
    tong_tu_nhien += j
    # Tăng j lên 1 để tiếp tục vòng lặp
    j += 1
# Tính kết quả S = tổng số lẻ × tổng số tự nhiên
kq = tong_so_le*tong_tu_nhien
# In ra kết quả
print("Ket qua S la:", kq)
