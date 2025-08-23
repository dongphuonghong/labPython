# 19. Nhập vào số nguyên n gồm ba chữ số; in ra các chữ số theo thứ tự tăng dần.
n = int(input("Nhap vao so nguyen n: "))
tram = n/100
chuc = (n//10) % 10
donvi = n % 10
# Trường hợp 1: hàng trăm nhỏ nhất
if tram < chuc and tram < donvi:
    if chuc < donvi:
        print(int(tram), int(chuc), int(donvi))
    else:
        print(int(tram), int(donvi), int(chuc))
# Trường hợp 2: hàng chục nhỏ nhất
elif chuc < tram and chuc < donvi:
    if tram < donvi:
        print(int(chuc), int(tram), int(donvi))
    else:
        print(int(chuc), int(donvi), int(tram))
# Trường hợp 3: hàng đơn vị nhỏ nhất
else:
    if tram < chuc:
        print(int(donvi), int(tram), int(chuc))
    else:
        print(int(donvi), int(chuc), int(tram))
# Cách 2 (tham khảo): dùng hàm max/min để tìm max, min và suy ra phần tử ở giữa
"""
n = int(input("Nhap so nguyen n gom ba chu so: "))  
tram = n // 100     
chuc = (n // 10) % 10 
donvi = n % 10  
# sắp xếp 3 chữ số bằng hàm max, min
max_val = max(tram, chuc, donvi)
min_val = min(tram, chuc, donvi)
# tìm chữ số ở giữa bằng cách lấy tổng 3 chữ số trừ đi chữ số max và chữ số min
mid = tram + chuc + donvi - max_val - min_val   
print(int(min_val), int(mid), int(max_val))
"""
# Cách 3 (tham khảo): sắp xếp bằng hoán vị
"""
# tạo biến n; nhập giá trị từ bàn phím gồm 3 chữ số
n = int(input("Nhap so nguyen n gom ba chu so: "))  
tram = n // 100     
chuc = (n // 10) % 10 
donvi = n % 10  
# sắp xếp 3 chữ số của n theo thứ tự tăng dần bằng hoán vị
if tram > chuc:
    temp = tram
    tram = chuc
    chuc = temp
if tram > donvi:
    temp = tram
    tram = donvi
    donvi = temp
if chuc > donvi:
    temp = chuc
    chuc = donvi
    donvi = temp
print("thu tu tang dan cua 3 chu so cua so nguyen n la: ", tram, chuc, donvi)
"""
