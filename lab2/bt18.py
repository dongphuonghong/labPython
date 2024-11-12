#Viêt chương trinh nhâp vao môt sô nguyên n gôm ba chư sô. Xuât ra man hinh chư sô lơn nhât ơ vi tri nao?
a=int(input("Nhap vao so nguyen n gom ba chu so: "))
tram=a/100
chuc=(a%100)//10
donvi=a%10
max=tram
ketqua="tram"
if chuc>max:
    max=chuc
    ketqua="chuc"
if donvi>max:
    max=donvi
    ketqua="donvi"
    print("Chu so lon nhat trong so nguyen n la: ",max," va o vi tri ",ketqua)
    #cách 2 sử dụng if else
    """
    #nhap v so nguyen n gom ba chu so 
n = int(input("Nhập vào một số nguyên n gồm ba chữ số: "))  
tram = n // 100 
chuc = (n % 100) // 10  
donvi = n % 10  
#tìm chữ số lớn nhất ở vị trí nào   
if tram >= chuc and tram >= donvi:  
    print("Chữ số lớn nhất ở vị trí hàng trăm")  
elif chuc >= tram and chuc >= donvi:    
    print("Chữ số lớn nhất ở vị trí  hàng chục")
else:   
    print("Chữ số lớn nhất ở vị trí hàng đơn vị")    
    """