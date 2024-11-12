# Giai va biên luân phương trinh:  ax + b = 0
#tạo biến a, b, nhập giá trị cho a, b từ bàn phím
a=float(input("Nhap a: "))
b=float(input("Nhap b: "))
#nếu a=0 thì phương trình có dạng: bx=0
if a==0:
    #nếu b=0 thì phương trình có vô số nghiệm
    if b==0:
        print("Phuong trinh co vo so nghiem")
    #nếu b!=0 thì phương trình vô nghiệm
    else:
        print("Phuong trinh vo nghiem")
#nếu a!=0 thì phương trình có nghiệm x=-b/a
else:
    print("Phuong trinh co nghiem x = ", -b/a)  