# 17. Giải và biện luận phương trình bậc hai ax^2 + bx + c = 0.
import math
# tạo biến a,b,c lấy giá trị từ bàn phím
a = float(input('Nhap a: '))
b = float(input('Nhap b: '))
c = float(input('Nhap c: '))
# tính delta bằng công thức d=b^2-4ac
d = b**2-4*a*c
# kiểm tra điều kiện của delta
# nếu d<0 thì phương trình vô nghiệm
if d < 0:
    print('Phuong trinh vo nghiem')
# nếu d=0 thì phương trình có nghiệm kép
elif d == 0:
    x = -b/(2*a)
    print('Phuong trinh co nghiem kep x= ', x)
# nếu d>0 thì phương trình có 2 nghiệm phân biệt x1,x2 tính theo công thức x1=(-b+sqrt(d))/(2a) và x2=(-b-sqrt(d))/(2a)
else:
    x1 = (-b+math.sqrt(d))/(2*a)
    x2 = (-b-math.sqrt(d))/(2*a)
    print('Phuong trinh co 2 nghiem phan biet: x1= ', x1, 'x2= ', x2)
    # cách 2 giải phương trình bậc 2 tính  x1,x2 không dùng thư viện math hàm sqrt
    """
    #Nhap vao 3 so a,b,c    
a= float(input("Nhập a: "))  
b= float(input("Nhập b: ")) 
c= float(input("Nhập c: ")) 
#Tính delta bằng công thức delta = b*b - 4*a*c
delta = b*b - 4*a*c 
#Xét điều kiện của delta
#Nếu delta < 0 thì phương trình vô nghiệm
if delta < 0:
    print("Phương trình vô nghiệm") 
#Nếu delta = 0 thì phương trình có nghiệm kép
elif delta == 0:    
    x = -b/(2*a)    
    print("Phương trình có nghiệm kép x1 = x2 = ", x)   
#Nếu delta > 0 thì phương trình có 2 nghiệm phân biệt x1 và x2 tính theo công thức x1 = (-b + delta**0.5)/(2*a) và x2 = (-b - delta**0.5)/(2*a) trong đó  *0.5 là căn bậc 2 của delta
else:    
    x1 = (-b + delta**0.5)/(2*a)    
    x2 = (-b - delta**0.5)/(2*a)    
    print("Phương trình có 2 nghiệm phân biệt x1 = ", x1, " và x2 = ", x2)  
    """
