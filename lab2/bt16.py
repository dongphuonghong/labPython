# 16. Giải và biện luận phương trình bậc hai ax^2 + bx + c = 0.
import math
# nhập a,b,c từ bàn phím
a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
c = float(input("Nhap c: "))
# Tính delta công thức d=b^2-4ac
d = b**2-4*a*c
# Xét điều kiện của delta
# Nếu elta<0 thì phương trình vô nghiệm
if d < 0:
    print("Phuong trinh vo nghiem")
# Nếu delta=0 thì phương trình có nghiệm kép
elif d == 0:
    x = -b/(2*a)
    print("Phuong trinh co nghiem kep x= ", x)
# Nếu delta>0 thì phương trình có 2 nghiệm phân biệt x1,x2 tính theo công thức
# x1= (-b+math.sqrt(d))/(2*a)
# x2= (-b-math.sqrt(d))/(2*a)
else:
    x1 = (-b+math.sqrt(d))/(2*a)
    x2 = (-b-math.sqrt(d))/(2*a)
    print("Phuong trinh co 2 nghiem phan biet: x1= ", x1, "x2= ", x2)
# cách 2 giải phương trình bậc 2 tính  x1,x2 không dùng thư viện math hàm sqrt
    """
#Nhap vao 3 so a,b,c    
    
    """
