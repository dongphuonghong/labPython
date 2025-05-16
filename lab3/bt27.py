# 27. Môt sô hoan thiên la môt sô co tông cac ươc sô cua no (không kê no) băng chinh no. Hay nhập vào số nguyên dương n và kiểm tra xem n có phải là số hoàn thiện không.Vi du: sô 6 la sô hoan thiên vi tông cac ươc sô la 1+2+3 = 6.
# Nhập số nguyên dương từ bàn phím
n=int(input("nhap so nguyen duong n: "))
# tạo biến sum để lưu tổng các ước số
sum=0
# Duyệt các số từ 1 đến n - 1 để tìm ước số
for i in range(1,n):
    # kiểm tra nếu i chia hết cho n thì cộng i vào biến sum
    if n%i==0:
        sum+=i
# kiểm tra nếu sum bằng n thì in ra n là số hoàn thiện
if sum==n:
            print(n,"la so hoan thien")
# nếu không thì in ra n không phải là số hoàn thiện
else:
        print(n,"khong phai la so hoan thien")
        # cách 2 dùng thư viện math
        """
        import math
# Nhập số nguyên dương từ bàn phím
n=int(input("Nhập số nguyên dương n: "))
# tạo biến sum để lưu tổng các ước số
sum=0
# sử dụng vòng lặp for để duyệt từ 1 đến căn bậc 2 của n
for i in range(1,int(math.sqrt(n))+1):
    #kiểm tra nếu i là ước số của n thì cộng i vào biến sum
    if n%i==0:
        # cộng i vào biến sum
        sum+=i
        # kiểm tra nếu i không phải là n và i không phải là 1 thì cộng n//i vào biến sum
        if i!=n//i and i!=1:
            # cộng n//i vào biến sum
            sum+=n//i
# kiểm tra nếu sum bằng n thì in ra n là số hoàn thiện
if sum==n:
    print(n,"là số hoàn thiện")
# nếu không thì in ra n không phải là số hoàn thiện
else:
    print(n,"không phải là số hoàn thiện")
        """