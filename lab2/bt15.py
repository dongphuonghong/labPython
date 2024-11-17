# Giai va biên luân phương trinh:  ax + b = 0
#tạo biến a, b, nhập giá trị cho a, b từ bàn phím
a=float(input("Nhap a: "))
b=float(input("Nhap b: "))
#nếu a=0 và b=0 thì phương trình vô số nghiệm
if a==0 and b==0:
    print("Phuong trinh vo so nghiem")
#nếu a=0 và b!khác 0 thì phương trình vô nghiệm
elif a==0 and b!=0:
    print("Phuong trinh vo nghiem")
#nếu akhác 0 thì phương trình có nghiệm x=-b/a
else:
    x=-b/a
    print("Phuong trinh co nghiem x = ", x) 