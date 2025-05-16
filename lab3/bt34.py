# 34. Tinh,  vơin n S 1 3 1 2 1 1 ) (      0  n
# tạo biến n và nhập giá trị từ bàn phím
n=int(input("Nhap n: "))
# khởi tạo biến sum = 0 để lưu tổng
sum=0
#dùng vòng lặp for để tính tổng từ 1 đến n
for i in range(1,n+1):
        # mỗi lần lặp cộng 1/i vào biến sum
    sum+=1/i
# in ra kết quả
print("S = ",sum)