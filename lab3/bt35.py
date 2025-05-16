# 35. Tinh,  vơin n n S       3 2 3 2 1 ) (0  n
# tạo biến n và nhập giá trị từ bàn phím
n=int(input("Nhap n: "))
# khởi tạo biến sum = 0 để lưu tổng
sum=0
# Dùng vòng lặp for để tính tổng
# Vòng lặp chạy từ 1 đến n+1 (range kết thúc trước n+2)
for i in range(1,n+2):
        # Cộng dồn giá trị 1/i vào biến sum
    sum+=1/i
# In ra kết quả tổng
print("S = ",sum)