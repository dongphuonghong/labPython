#Viêt chương trinh tinh tiên cươc TAXI. Biêt răng:- km đâu tiên la 13000đ.- Mỗi km tiếp theo la 12000đ.- Nêu lơn hơn 30km thi môi km thêm se la 11000đ.Hay nhâp sô km sau đo in ra sô tiên phai tra.
#tạo biến n để nhập số km
n=float(input("Nhập số km:"))
#tính số tiền phải trả
#nếu n<=1 thì số tiền phải trả là n*13000
if n<=1:
    print("Số tiền phải trả là:",n*13000)
#nếu n<=30 thì số tiền phải trả là 13000+(n-1)*12000
elif n<=30:
    print("Số tiền phải trả là:",13000+(n-1)*12000)
#nếu n>30 thì số tiền phải trả là 13000+29*12000+(n-30)*11000
else:
    print("Số tiền phải trả là:",13000+29*12000+(n-30)*11000)