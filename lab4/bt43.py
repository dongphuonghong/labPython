# 43. Viết chương trình tính diện tích và chu vi của hình chữ nhật với chiều dài và chiều rộng được nhập từ bàn phím.
# Đây là hàm tính diện tích hình chữ nhật 
# theo công thức: diện tích = chiều dài * chiều rộng
def tinhDienTich(chieuDai, chieuRong):
    return chieuDai * chieuRong
# Đây là hàm tính chu vi hình chữ nhật
# theo công thức: chu vi = 2 * (chiều dài + chiều rộng)
def tinhChuVi(chieuDai, chieuRong):
    return 2 * (chieuDai + chieuRong)
# Đây là hàm main để chạy chương trình nhập dữ liệu và hiển thị kết quả
# Hàm main sẽ gọi các hàm tính diện tích và chu vi
def main():
    chieuDai = float(input("Nhập chiều dài của hình chữ nhật: "))
    chieuRong = float(input("Nhập chiều rộng của hình chữ nhật: "))
    dienTich = tinhDienTich(chieuDai, chieuRong)
    chuVi = tinhChuVi(chieuDai, chieuRong)
    print(f"Diện tích của hình chữ nhật là: {dienTich}")
    print(f"Chu vi của hình chữ nhật là: {chuVi}")
main()