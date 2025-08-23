# 13. Cho ba số nguyên a, b, c (nhập từ bàn phím). Tìm giá trị lớn nhất và in ra màn hình.
# tạo biến a,b,c nhập giá trị từ bàn phím
a = int(input('nhap a'))
b = int(input('nhap b'))
c = int(input('nhap c'))
# điều kiện nếu a lớn hơn b và c thì in ra a là giá trị lớn nhất
if a >= b and a >= c:
    print('a la gia tri lon nhat')
# điều kiện nếu b lớn hơn a và c thì in ra b là giá trị lớn nhất
elif b >= a and b >= c:
    print('b la gia tri lon nhat')
# điều kiện nếu c lớn hơn a và b thì in ra c là giá trị lớn nhất
else:
    print('c la gia tri lon nhat')
    # cách2 giả định a là số lớn nhất và so sánh với b,c để tìm ra số lớn nhất
    """
    #tạo a,b,c nhập từ bàn phím, 
a=int(input("nhap a: "))
b=int(input("nhap b: "))
c=int(input("nhap c: "))
#tìm số lớn nhất bằng giả định a là số lớn nhấtvới biến max
# và so sánh max với b,c để tìm số lớn nhất
max=a
#nếu b>max thì max=b
if b>max:
    max=b
#nếu c>max thì max=c
if c>max:
    max=c
#in ra kết quả
print("so lon nhat la: ",max)
    """
    # cách 3 sử dụng hàm max để tìm ra số lớn nhất
    """
    #tạo a,b,c nhập từ bàn phím, tìm số lớn nhất
a=int(input("nhap a: "))
b=int(input("nhap b: "))
c=int(input("nhap c: "))
#sử dụng hàm max của python để tìm số lớn nhất
max=max(a,b,c)
#in ra kết quả
print("so lon nhat la: ",max1)
    """
    # cách 4 sử dụng if else rút gọn của python
    """
    #tạo a,b,c nhập từ bàn phím, tìm số lớn nhất
a=int(input("nhap a: "))
b=int(input("nhap b: "))
c=int(input("nhap c: "))
#tìm số lớn nhất bằng cách sử dụng if else rút gọn của python
max=(a if a>b else b) if ((a if a>b else b)>c) else c
#in ra kết quả
print("so lon nhat la: ",max)
    """
