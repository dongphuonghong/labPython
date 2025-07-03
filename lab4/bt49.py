# 49. Viết chương trình tính tiền thuê máy dịch vụ Internet và in ra màn hình kết quả. Với dữ liệu nhập vào là giờ bắt đầu thuê (GBD), giờ kết thúc thuê (GKT), số máy thuê (SoMay).- Điều kiện cho dữ liệu nhập: 6<=GBD<GKT<=21. Giờ là số nguyên.- Đơn giá: 2500đ cho mỗi giờ máy trước 17 giờ và 3000đ cho mỗi giờ máy từ sau 17.
# Đây là hàm tính tiền thuê máy dựa trên giờ bắt đầu, giờ kết thúc và số máy thuê
# Nếu giờ bắt đầu và giờ kết thúc không hợp lệ, hàm sẽ trả về thông báo lỗi
# Nếu hợp lệ, hàm sẽ tính tiền thuê máy theo quy định và trả về kết quả
# Quy định: 2500 đồng/giờ/máy trước 17 giờ, 3000 đồng/giờ/máy sau 17 giờ
def tinh_tien_thue_may(GBD, GKT, SoMay):
    if not (6 <= GBD < GKT <= 21):
        return "Dữ liệu nhập vào không hợp lệ."
    tien_thue = 0
    for gio in range(GBD, GKT):
        if gio < 17:
                    tien_thue += 2500 * SoMay
        else:
                tien_thue += 3000 * SoMay
    return f"Tổng tiền thuê máy: {tien_thue} đồng"
# Chương trình chính để nhập dữ liệu và gọi hàm tính tiền thuê máy
# Nó sẽ yêu cầu người dùng nhập giờ bắt đầu, giờ kết thúc và số máy thuê
def main():
    while True:
        GBD = int(input("Nhập giờ bắt đầu thuê (GBD, từ 6 đến 20): "))
        GKT = int(input("Nhập giờ kết thúc thuê (GKT, từ 7 đến 21): "))
        if 6 <= GBD < GKT <= 21:
            break
        print("Vui lòng nhập giờ hợp lệ.")  
    SoMay = int(input("Nhập số máy thuê: "))
    ket_qua = tinh_tien_thue_may(GBD, GKT, SoMay)
    print(ket_qua)
main()