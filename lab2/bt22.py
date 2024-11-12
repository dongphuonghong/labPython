#Nhâp vao 3 sô nguyên dương. Kiêm tra xem 3 sô đo co lâp thanh tam giac không? Nêu co hay cho biet tam giac đo la tam giac gi?
#tạo biến a,b,c nhập từ  giá trị nhập vào từ bàn phím
a=int(input("Nhập số nguyên dương a:"))
b=int(input("Nhập số nguyên dương b:"))
c=int(input("Nhập số nguyên dương c:"))
#Kiểm tra xem 3 số đó có lập thành tam giác không
# Nếu có thì kiểm tra xem tam giác đó là tam giác gì
#tam giác đều: 3 cạnh bằng nhau
#tam giác cân: 2 cạnh bằng nhau
#tam giác vuông: c^2=a^2+b^2
#tam giác thường: không phải tam giác đều, cân, vuông
#nếu a+b>c và a+c>b và b+c>a thì 3 số đó lập thành tam giác
if a+b>c and a+c>b and b+c>a:
    #nếu a=b=c thì đó là tam giác đều
    if a==b==c:
        print("Tam giác đều")
    #nếu a=b or a=c or b=c thì đó là tam giác cân
    elif a==b or a==c or b==c:
        print("Tam giác cân")
    #nếu c^2=a^2+b^2 or a^2=c^2+b^2 or b^2=a^2+c^2 thì đó là tam giác vuông
    elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
        print("Tam giác vuông")
    #nếu a!=b!=c!=a thì đó là tam giác thường
    else:
        print("Tam giác thường")    