# 31. Tinh,  vơin n S n 1 ) 1 ( 4 3 2 1 ) (         0  n
# Tạo biến n và nhập giá trị từ bàn phím
n=int(input("Nhap n lon hon 0: "))
# Khởi tạo biến sum với giá trị ban đầu là 0
sum=0
# Dùng vòng lặp for để duyệt qua các số từ 1 đến n
for i in range(1,n+1):
    #kiểm tra Nếu i là số chẵn, thì trừ i vào sum
        if i%2==0:
            sum-=i
    # Nếu i là số lẻ, thì cộng i vào sum
        else:
            sum+=i
# In kết quả S(n) ra màn hình
print("S(n) = ", sum)
        #cách 2 Dùng công thức rút gọn để tính nhanh không cần dùng vòng lặp:
# - Nếu n là số chẵn:     S(n) = -n / 2
# - Nếu n là số lẻ:       S(n) = (n + 1) / 2
        """
          # Tạo biến n và nhập giá trị từ bàn phím
n=int(input("Nhap n lon hon 0: "))
# Khởi tạo biến sum với giá trị ban đầu là 0
sum=0
# Dùng vòng lặp for để duyệt qua các số từ 1 đến n
for i in range(1,n+1):
    #kiểm tra Nếu i là số chẵn, thì trừ i vào sum
        if i%2==0:
            sum-=i
    # Nếu i là số lẻ, thì cộng i vào sum
        else:
            sum+=i
# In kết quả S(n) ra màn hình
           print("S(n) = ", sum)
        #cách 2 Dùng công thức rút gọn để tính nhanh không cần dùng vòng lặp:
# - Nếu n là số chẵn:     S(n) = -n / 2
# - Nếu n là số lẻ:       S(n) = (n + 1) / 2
        """
          
              """
              """