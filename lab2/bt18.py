# 18. Nhập vào số nguyên n gồm ba chữ số; xác định chữ số lớn nhất và vị trí của nó.
# Tạo biến a nhập từ bàn phím.
a = int(input("Nhap vao so nguyen n gom ba chu so: "))
# Tách các chữ số hàng trăm
tram = a // 100
# hàng chục
chuc = (a % 100) // 10
# Tách các chữ số hàng đơn vị
donvi = a % 10
# Giả sử ban đầu giá trị lớn nhất là hàng trăm
max = tram
# Kết quả mặc định: hàng trăm
ketqua = "tram"
# Nếu hàng chục lớn hơn max: cập nhật max và vị trí
if chuc > max:
    max = chuc
    ketqua = "chuc"
# Nếu hàng đơn vị lớn hơn max: cập nhật max và vị trí
if donvi > max:
    max = donvi
    ketqua = "donvi"
# Xuất kết quả
print("Chu so lon nhat trong so nguyen n la: ", max, " va o vi tri ", ketqua)
# Cách 2: sử dụng if-else (tham khảo)
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
