# 42. In ra day sô Fibonaci
# Nhập giá trị n từ bàn phím (số lượng phần tử cần in trong dãy)
n=int(input("Nhap n: "))
# Khởi tạo hai phần tử đầu tiên của dãy Fibonaci
a=0
b=1
# In ra phần tử đầu tiên
print(a, end=" ")
# Dùng vòng lặp for để in ra các phần tử tiếp theo của dãy Fibonaci
for i in range(1,n):
    # In ra giá trị hiện tại của b
    print(b, end=" ")
        # Tính giá trị Fibonaci tiếp theo bằng tổng của hai số trước đó
    Fibonaci=a+b
        # Cập nhật lại a và b cho lần lặp sau
    a=b
b=Fibonaci
# Xuống dòng sau khi in xong dãy
print()