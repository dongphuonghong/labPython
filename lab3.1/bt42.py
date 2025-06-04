# 42. In ra dãy số Fibonacci
# Nhập giá trị n từ bàn phím (số lượng phần tử cần in trong dãy)
n=int(input("Nhap n: "))
# Khởi tạo hai phần tử đầu tiên của dãy Fibonacci
a=0
b=1
# In ra phần tử đầu tiên
print(a, end=" ")
# Dùng vòng lặp while để in ra các phần tử tiếp theo của dãy Fibonacci
i=1
while i<n:
    # In ra giá trị hiện tại của b
    print(b, end=" ")
    # Tính giá trị Fibonacci tiếp theo bằng tổng của hai số trước đó
    Fibonacci=a+b
    # Cập nhật lại a và b cho lần lặp sau
    a=b
    b=Fibonacci
    # Tăng i lên 1 để tiếp tục vòng lặp
    i+= 1  
# Xuống dòng sau khi in xong dãy
print()