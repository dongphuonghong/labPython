# 27. Một số hoàn thiện là một số có tổng các ước số của nó (không kể nó) bằng chính nó. Hãy nhập vào số nguyên dương n và kiểm tra xem n có phải là số hoàn thiện không. Ví dụ: số 6 là số hoàn thiện vì tổng các ước số là 1+2+3 = 6.
# Nhập số nguyên dương từ bàn phím
n=int(input("nhap so nguyen duong n: "))
# Tạo biến sum để lưu tổng các ước số = 0
sum=0
# Duyệt các số từ 1 đến n - 1 để tìm ước số
i=1
while i<n:
    # Kiểm tra nếu i là ước số của n thì cộng i vào biến sum
    if n%i==0:
        sum+=i
    i+=1
# Kiểm tra nếu sum bằng n thì in ra n là số hoàn thiện
if sum==n:
    print(n, "là số hoàn thiện")
# Nếu không thì in ra n không phải là số hoàn thiện
else:
    print(n, "không phải là số hoàn thiện")