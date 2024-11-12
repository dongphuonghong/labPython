#4. Viết chương trình nhập vào 2 số nguyên dương a và b, cho biết kết quả chia lấy phần nguyên và phần dư của a với b.
#tạo  biến a,b nhập giá trị từ bàn phím
a=int(input("nhap  a"))    
b=int(input("nhap  b")) 
# tìm phần nguyên và phần dư
nguyen=(a/b)
#tìm phần dư
du=(a%b) 
#in kết quả
print("kết quả của phép chia phần nguyên là:",nguyen)
print("kết quả của phép chia phần dư là:",du)