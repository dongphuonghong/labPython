# 14. Cho ba số a, b, c (nhập từ bàn phím). In ra màn hình thứ tự tăng dần của ba số.
# tạo biến a,b,c nhập giá trị từ bàn phím
a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))
c = int(input("Nhap so c: "))
# kiểm tra từng trường hợp
# nếu a<b<c thì in ra a,b,c
if a < b and a < c:
    if b < c:
        print(a, b, c)
        # nếu a<c<b thì in ra a,c,b
    else:
        print(a, c, b)
        # nếu b<a<c thì in ra b,a,c
elif b < a and b < c:
    if a < c:
        print(b, a, c)
        # nếu b<c<a thì in ra b,c,a
    else:
        print(b, c, a)
        # nếu c<a<b thì in ra c,a,b
else:
    if a < b:
        print(c, a, b)
        # nếu c<b<a thì in ra c,b,a
    else:
        print(c, b, a)
# cách 2 sử dụng hàm max() và min()
"""
#Cho ba sô a, b, c đoc vao tư ban phim. Hay in ra man hinh theo thư tư tăng dân cac sô.
# nhap so a,b,c tu ban phim 
a = int(input("Nhap so a: "))   
b = int(input("Nhap so b: "))   
c = int(input("Nhap so c: "))   
# sắp xếp 3 số a,b,c bằng cách sử dụng hàm max() và min()
max=max(a,b,c)
min=min(a,b,c)
# tìm số giữa bằn cách sử dụng công thức a+b+c-max-min
mid=a+b+c-max-min
# in ra kết quả sau khi sắp xếp
print("Thu tu tang dan cua 3 so la: ",min,mid,max)
"""
# cách 3 sử dụng phép hoán vị
"""
#Cho ba sô a, b, c đoc vao tư ban phim. Hay in ra man hinh theo thư tư tăng dân cac sô.
# nhap so a,b,c tu ban phim 
a = int(input("Nhap so a: "))   
b = int(input("Nhap so b: "))   
c = int(input("Nhap so c: "))   
# so sanh so sánh a,b,c dùng phép hoán vị
# nếu a>b thì tạo biến tạm temp = a, a=b, b=temp temp để lư giá trị a ban đầu
if a>b:
    temp=a
    a=b
    b=temp
# so sánh a,c nếu a>c thì tạo biến tạm temp = a, a=c, c=temp temp để lư giá trị a ban đầu
if a>c:
    temp=a
    a=c
    c=temp
# so sánh b,c nếu b>c thì tạo biến tạm temp = b, b=c, c=temp temp để lư giá trị b ban đầu
if b>c:
    temp=b
    b=c
    c=temp
    #xuất kết quả
print("Cac so duoc sap xep theo thu tu tang dan la: ",a,b,c)
"""
