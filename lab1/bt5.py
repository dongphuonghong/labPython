"""
5. Viết chương trình nhập một số nguyên dương N có 2 chữ số từ bàn phím, xuất ra màn hình tổng các chữ số của N.Ví dụ: Nhập N = 48, kết quả in ra màn hình là: 4+8=12Page 2 of 10
"""
#tạo biến n nhập giá trị từ bàn phím
n=int(input('nhap n'))  
#tìm hàng đơn vị và hàng chục
hdv=n%10    
#tìm hàng chục
hc=n/10
#tính tổng 2 chữ số
sum=hdv+hc  
#xuất kết quả
print('tong 2 chu so cuoi cua so nguyen duong n la:',sum)   