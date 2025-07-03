# 61. Viết chương trình nhập số nguyên dương n gồm k chữ số, kiểm tra xem các chữ số của n có toàn lẻ hay toàn chẵn không.
# Đây là hàm kiểm tra xem các chữ số của một số nguyên dương n có toàn chữ số chẵn hay toàn chữ số lẻ không.
# Hàm này sẽ lặp qua từng chữ số của n, kiểm tra xem chữ số đó là chẵn hay lẻ, và cập nhật hai biến toan_chan và toan_le.
# Nếu chữ số là chẵn, biến toan_le sẽ được đặt thành False, ngược lại nếu chữ số là lẻ, biến toan_chan sẽ được đặt thành False.
# Hàm này sẽ trả về hai giá trị: toan_chan và toan_le,
def kiemTraChuSoChanLe(n):
    toan_chan = True
    toan_le = True
    while n > 0:
        chu_so = n % 10
        if chu_so % 2 == 0:
            toan_le = False
        else:
            toan_chan = False
        n //= 10
    return toan_chan, toan_le

# Đây là hàm chính để chạy chương trình
# Hàm này sẽ yêu cầu người dùng nhập một số nguyên dương n. 
# Nếu n không hợp lệ (không phải số nguyên dương), nó sẽ yêu cầu nhập lại.
# Sau khi nhập hợp lệ, nó sẽ gọi hàm kiemTraChuSoChanLe
# để kiểm tra số lượng chữ số chẵn và lẻ trong n.
## Cuối cùng, nó sẽ in ra kết quả dựa trên giá trị của toan_chan và toan_le.
def main():
    while True:
        n = int(input("Nhập số nguyên dương n (n > 0): "))
        if n > 0:
            break
        print("Vui lòng nhập một số nguyên dương lớn hơn 0.")
    toan_chan, toan_le = kiemTraChuSoChanLe(n)
    if toan_chan:
        print(f"Tất cả các chữ số của {n} đều là chữ số chẵn.")
    elif toan_le:
        print(f"Tất cả các chữ số của {n} đều là chữ số lẻ.")
    else:
        print(f"Các chữ số của {n} vừa có chữ số chẵn vừa có chữ số lẻ.")
main()