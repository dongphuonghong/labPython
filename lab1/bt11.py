import math     
print('tam giac')
a = float(input( 'nhap do dai cua canh a:' ))    
b = float(input( 'nhap do dai cua canh b:' ))   
c = float(input( 'nhap do dai cua canh c:' ))   
h =float(input( 'nhap do dai cua chieu cao h:' ))    
dien_tich_tam_giac= (a*h) 
chu_vi_tam_giac= a+b+c  
print('dien tich tam giac:',dien_tich_tam_giac) 
print('chu vi tam giac:',chu_vi_tam_giac)   
print("\nHình vuông:")
a = float(input( 'nhap do dai cua canh a:' ))   
dien_tich_hinh_vuong= a**2   
chu_vi_hinh_vuong= 4*a  
print('dien tich hinh vuong:',dien_tich_hinh_vuong) 
print('chu vi hinh vuong:',chu_vi_hinh_vuong)   
print("\nHình chữ nhật:")
a= float(input( 'nhap do dai cua canh a:' ))    
b= float(input( 'nhap do dai cua canh b:' ))    
dien_tich_hinh_chu_nhat= a*b    
chu_vi_hinh_chu_nhat= 2*(a+b)   
print('dien tich hinh chu nhat:',dien_tich_hinh_chu_nhat)   
print('chu vi hinh chu nhat:',chu_vi_hinh_chu_nhat) 
print("\nHình tròn:")
r= float(input( 'nhap ban kinh r:' ))   
dien_tích_hình_tròn= math.pi*r**2   
chu_vi_hình_tròn= 2*math.pi*r   
print('dien tich hinh tron:',dien_tích_hình_tròn)   
print('chu vi hinh tron:',chu_vi_hình_tròn)