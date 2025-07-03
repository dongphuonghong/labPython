# 50. Viết chương trình tính tiền lương ngày cho công nhân, cho biết trước giờ vào ca, giờ ra ca của mỗi người. Biết rằng:- Tiền trả cho mỗi giờ trước 12 giờ là 6000đ và sau 12 giờ là 7500đ.- Giờ vào ca sớm nhất là 6 giờ sáng và giờ ra ca trễ nhất là 18 giờ (Giả sử giờ nhập vào nguyên).
# Đây là hàm tính tiền lương cho công nhân dựa trên giờ vào ca và giờ ra ca.
# Nó kiểm tra tính hợp lệ của giờ vào ca và ra ca, sau đó tính tổng
def tinh_tien_luong(vao_ca, ra_ca):    
    gio_vao = int(vao_ca.split(':')[0])
    gio_ra = int(ra_ca.split(':')[0])
    if gio_vao < 6 or gio_ra > 18 or gio_vao >= gio_ra:
        return "Giờ vào ca hoặc ra ca không hợp lệ."
    tien_luong = 0
    for gio in range(gio_vao, gio_ra):
        if gio < 12:
            tien_luong += 6000
        else:
            tien_luong += 7500
    return f"Tổng tiền lương: {tien_luong} đồng"
# Đây là hàm main để chạy chương trình nhập dữ liệu và hiển thị kết quả
# Hàm main sẽ gọi hàm tinh_tien_luong để tính tiền lương và in ra kết quả
def main():
    vao_ca = input("Nhập giờ vào ca (định dạng HH:MM): ")
    ra_ca = input("Nhập giờ ra ca (định dạng HH:MM): ")
    ket_qua = tinh_tien_luong(vao_ca, ra_ca)
    print(ket_qua)
main()