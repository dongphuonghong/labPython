# Nhâp vao giơ, phut, giây. Kiêm tra xem giơ, phut, giây đo co hơp lê hay không? In kêt qua ra man hinh.
# tạo   biến  giờ, phút, giây và nhập giá trị từ bàn phím
gio=int(input("Nhap vao gio: "))
phut=int(input("Nhap vao phut: "))
giay=int(input("Nhap vao giay: "))
# kiểm tra giờ, phút, giây có hợp lệ hay không
# nếu giờ từ 0 đến 23 và phút, giây từ 0 đến 59 thì thời gian nhập vào hợp lệ
if gio>=0 and gio<=23 and phut>=0 and phut<=59 and giay>=0 and giay<=59:
    print("thoi gian nhap vao hop le")
# ngược lại thời gian nhập vào không hợp lệ
else:
    print("thoi gian nhap vao khong hop le")