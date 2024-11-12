# 19Viêt chương trinh nhâp vao sô nguyên n gôm ba chư sô. Xuât ra man hinh theo thư tư tăng dân cua cac chư sô.Vi du: n=291. Xuât ra 129.
n=int(input("Nhap vao so nguyen n: "))
tram=n/100     
chuc=(n//10)%10 
donvi=n%10  
if tram < chuc and  tram< donvi:
    if chuc < donvi:
        print(int(tram), int(chuc), int(donvi))
    else:
        print(int(tram), int(donvi), int(chuc))
elif chuc < tram and chuc < donvi:
    if tram < donvi:
        print(int(chuc), int(tram), int(donvi))
    else:
        print(int(chuc), int(donvi), int(tram))
else:
    if tram < chuc:
        print(int(donvi), int(tram), int(chuc))
    else:
        print(int(donvi), int(chuc), int(tram))
        # cách  2    sử dụng hàm max, min để sắp xếp 3 chữ số
        """
        #tạo  biến  n  nhập  giá trị  từ  bàn  phím gồm 3 chữ số
n = int(input("Nhap so nguyen n gom ba chu so: "))  
tram=n/100     
chuc=(n//10)%10 
donvi=n%10  
#sắp sếp 3 chữ số bằng hàm max, min
max=max(tram,chuc,donvi)   
min=min(tram,chuc,donvi)   
#tìm chữ số ở giữa bằng cách lấy tổng 3 chữ số trừ đi chữ số max và chữ số min
mid=tram+chuc+donvi-max-min   
#xuât kết quả
print(int(min),int(mid),int(max))
"""
# cách 3: sử dụng phép hoán vị đê sắp xếp 3 chữ số
"""
#tạo  biến  n  nhập  giá trị  từ  bàn  phím gồm 3 chữ số
n = int(input("Nhap so nguyen n gom ba chu so: "))  
tram=n/100     
chuc=(n//10)%10 
donvi=n%10  
#sắp xếp 3 chữ số của n theo thứ tự tăng dần bằng  cách sử dụng phép hoán vị
#nếu hàng trăm lớn hơn hàng chục thì đổi chỗ hai giá trị đó
if tram> chuc:
    temp=tram
    tram=chuc
    chuc=temp
#nếu hàng trăm lớn hơn hàng đơn vị thì đổi chỗ hai giá trị đó
if tram>donvi:
    temp=tram
    tram=donvi
    donvi=temp
#nếu hàng chục lớn hơn hàng đơn vị thì đổi chỗ hai giá trị đó
if chuc>donvi:
    temp=chuc
    chuc=donvi
    donvi=temp
#in ra thứ tự tăng dần của 3 chữ số của n
print("thu tu tang dan cua 3 chu so cua so nguyen n la: ",tram,chuc,donvi)
"""