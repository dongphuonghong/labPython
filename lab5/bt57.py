# 57. Viết chương trình nhập số nguyên dương n gồm k chữ số, đếm xem n có bao nhiêu chữ số chẵn và bao nhiêu chữ số lẻ. 57. Viêt chương trinh nhâp sô nguyên dương n gôm k chư sô, đêm xem n co bao nhiêu chư sô chăn va bao nhiêu chư sô le.) 5 0 (  k
#đây là hàm kiểm tra số chữ số chẵn và lẻ trong một số nguyên dương n
# Hàm này sẽ lặp qua từng chữ số của n, kiểm tra xem chữ số đó là chẵn hay lẻ, và đếm số lượng chữ số chẵn và lẻ.
# Nếu chữ số là chẵn, biến đếm chữ số chẵn sẽ tăng lên 1, ngược lại nếu chữ số là lẻ, biến đếm chữ số lẻ sẽ tăng lên 1.
# Hàm này sẽ trả về hai giá trị: số lượng chữ số chẵn và số lượng chữ số lẻ.
def kiemTraChuSoChanLe(n):
    chan = 0
    le = 0
    while n > 0:
        chu_so = n % 10
        if chu_so % 2 == 0:
            chan += 1
        else:
            le += 1
        n //= 10
    return chan, le
# Đây là hàm chính để chạy chương trình
# Hàm này sẽ yêu cầu người dùng nhập một số nguyên dương n .
# Nếu n không hợp lệ (không phải số nguyên dương), nó sẽ yêu cầu nhập lại.
# Sau khi nhập hợp lệ, nó sẽ gọi hàm kiemTraChuSoChanLe để kiểm tra số lượng chữ số chẵn và lẻ trong n.
# Cuối cùng, nó sẽ in ra số lượng chữ số chẵn và lẻ.
def main():
    while True:
        n = int(input("Nhập số nguyên dương n (n > 0): "))
        if n > 0:
            break
        print("Vui lòng nhập một số nguyên dương lớn hơn 0.")
    chan, le = kiemTraChuSoChanLe(n)
    print(f"Số lượng chữ số chẵn: {chan}, Số lượng chữ số lẻ: {le}")
main()