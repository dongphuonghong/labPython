# 64. Viết chương trình nhập số nguyên dương n gồm k chữ số, sắp xếp các chữ số của n theo thứ tự tăng dần. Ví dụ: Nhập n=1536, Kết quả sau khi sắp xếp: 1356.
# Đây là hàm sắp xếp các chữ số của một số nguyên dương n theo thứ tự tăng dần.
# Hàm này sẽ chuyển đổi số nguyên n thành một danh sách các chữ số, sau đó sắp xếp danh sách này và trả về kết quả.
# Hàm này sẽ trả về một danh sách các chữ số đã được sắp xếp
def sapXepChuSo(n):
    """Sắp xếp chữ số của n theo thứ tự tăng dần.

    Args:
        n (int): Số nguyên dương.

    Returns:
        list[int]: Danh sách chữ số đã sắp xếp.
    """
    chu_so = []
    while n > 0:
        chu_so.append(n % 10)
        n //= 10
    chu_so.sort()
    return chu_so
# Đây là hàm chính để chạy chương trình
# Hàm này sẽ yêu cầu người dùng nhập một số nguyên dương n.
# Nếu n không hợp lệ (không phải số nguyên dương), nó sẽ yêu cầu nhập lại.
# Sau khi nhập hợp lệ, nó sẽ gọi hàm sapXepChuSo để sắp xếp các chữ số của n và in ra kết quả.


def main():
    """Hàm chính: nhập n và in các chữ số sau sắp xếp."""
    while True:
        n = int(input("Nhập số nguyên dương n (n > 0): "))
        if n > 0:
            break
        print("Vui lòng nhập một số nguyên dương lớn hơn 0.")
    ket_qua = sapXepChuSo(n)
    print(f"Kết quả sau khi sắp xếp: {''.join(map(str, ket_qua))}")


main()
