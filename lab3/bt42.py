# 42. In ra dãy số Fibonacci với n phần tử.
# CÁCH 1: Dùng for loop
# Nhập giá trị n từ bàn phím (số lượng phần tử cần in trong dãy)
n = int(input("Nhap n: "))
# Khởi tạo hai phần tử đầu tiên của dãy Fibonacci
a = 0
b = 1
# In ra phần tử đầu tiên
print(a, end=" ")
# Dùng vòng lặp for để in ra các phần tử tiếp theo của dãy Fibonacci
for i in range(1, n):
    # In ra giá trị hiện tại của b
    print(b, end=" ")
    # Tính giá trị Fibonacci tiếp theo bằng tổng của hai số trước đó
    Fibonacci = a+b
    # Cập nhật lại a và b cho lần lặp sau
    a = b
    b = Fibonacci
# Xuống dòng sau khi in xong dãy
print()
