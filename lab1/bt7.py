"""
7. Viết chương trình cho phép nhập vào giờ, phút và giây, hãy đổi sang giây và in kết quả ra màn hình
"""
#tạo biến giờ nhập giá trị từ bàn phím
gio=int(input(" nhap Gio: ")) 
#tạo biến phút nhập giá trị từ bàn phím
phut=int(input(" nhap Phut: ")) 
#tạo biến giây nhập giá trị từ bàn phím
giay=int(input(" nhap Giay: ")) 
#chuyển đổi giờ sang giây
gio=gio*3600
#chuyển đổi phút sang giây
phut=phut*60
#tính tổng số giây
giay=giay*1
#tổng số giây
tong=gio+phut+giay
#xuất kết quả
print("Tong so giay la: ",tong)