"""
6. Viết chương trình cho phép nhập vào một số đo nhiệt độ theo độ Fahrenheit và xuất ra nhiệt độ tương đương của nó theo độ Celsius, sử dụng công thức chuyển đổi:) 32 ( 9 5 0 0   F C
"""
#tạo biến df nhập giá trị độf từ bàn phím
df=float(input(" nhap do f")) 
#tính độC theo công thức chuyển đổi df=(df-32)*5/9
dc=(df-32)*5/9  
#xuất kết quả
print("Độ Celsius là:", dc)