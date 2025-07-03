# 51. Nhập vào 3 số thực a, b, c và kiểm tra xem chúng có thành lập thành 3 cạnh của một tam giác hay không? Nếu có hãy tính diện tích, chiều dài mỗi đường cao của tam giác và in kết quả ra màn hình.- Công thức tính diện tích s = sqrt(p*(p-a)*(p-b)*(p-c) )- Công thức tính các đường cao: ha = 2s/a, hb=2s/b, hc=2s/c.(Với p là nửa chu vi của tam giác).
# Đây là hàm kiểm tra xem ba cạnh a, b, c có thể tạo thành một tam giác hay không
# Nếu tổng của hai cạnh bất kỳ lớn hơn cạnh còn lại thì ba cạnh đó có thể tạo thành tam giác
import math
def kiem_tra_tam_giac(a, b, c):
        return a + b > c and a + c > b and b + c > a
# Đây là hàm tính diện tích tam giác theo công thức Heron
# Công thức Heron: diện tích = sqrt(p * (p - a) * (p - b) * (p - c))
def tinh_dien_tich(a, b, c):
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return s
# Đây là hàm tính chiều cao tương ứng với mỗi cạnh của tam giác
# Chiều cao tương ứng với cạnh a là ha = 2s/a, với cạnh b là hb = 2s/b, với cạnh c là hc = 2s/c
def tinh_cao(a, b, c):
    s = tinh_dien_tich(a, b, c)
    if s == 0:
        return 0, 0, 0
    ha = 2 * s / a
    hb = 2 * s / b
    hc = 2 * s / c
    return ha, hb, hc
# Đây là hàm main để chạy chương trình nhập dữ liệu và hiển thị kết quả
# Hàm main sẽ gọi các hàm kiểm tra, tính diện tích và chiều cao
def main():
    a = float(input("Nhập cạnh a: "))
    b = float(input("Nhập cạnh b: "))
    c = float(input("Nhập cạnh c: "))
    if kiem_tra_tam_giac(a, b, c):
        s = tinh_dien_tich(a, b, c)
        ha, hb, hc = tinh_cao(a, b, c)
        print(f"Các cạnh {a}, {b}, {c} có thể tạo thành tam giác.")
        print(f"Diện tích tam giác là: {s:.2f}")
        print(f"Chiều cao tương ứng là: ha = {ha:.2f}, hb = {hb:.2f}, hc = {hc:.2f}")
    else:
        print(f"Các cạnh {a}, {b}, {c} không thể tạo thành tam giác.")
main()