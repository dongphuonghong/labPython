# 56. Viết chương trình nhập số nguyên dương n gồm 5 chữ số, kiểm tra xem các chữ số n có phải là số đối xứng hay không. Ví dụ: Đối xứng: 13531, Không đối xứng: 13921
# Đây là hàm kiểm tra số đối xứng
# Một số đối xứng là số mà khi đọc từ trái sang phải và từ phải sang trái đều giống nhau.
# Ví dụ: 13531 là số đối xứng vì đọc từ trái sang phải là 13531 và từ phải sang trái cũng là 13531.
# Hàm này sẽ chuyển đổi số nguyên n thành chuỗi, sau đó so sánh chuỗi đó với chuỗi đảo ngược của nó.
# Nếu hai chuỗi giống nhau, thì n là số đối xứng, ngược lại, n không phải là số đối xứng.
# Hàm này sẽ trả về True nếu n là số đối xứng, ngược lại False.
def kiemTraSoDoiXung(n):
    """Kiểm tra số đối xứng.

    Args:
        n (int): Số nguyên cần kiểm tra (5 chữ số theo đề bài).

    Returns:
        bool: True nếu đối xứng, False nếu không.
    """
    str_n = str(n)
    return str_n == str_n[::-1]
# Đây là hàm chính để chạy chương trình
# Hàm này sẽ yêu cầu người dùng nhập một số nguyên dương n gồm 5 chữ số.
# Nếu n không hợp lệ (không phải số nguyên dương hoặc không có 5 chữ số), nó sẽ yêu cầu nhập lại.
# Sau khi nhập hợp lệ, nó sẽ gọi hàm kiemTraSoDoiXung để kiểm tra xem n có phải là số đối xứng hay không.
# Cuối cùng, nó sẽ in ra kết quả kiểm tra.


def main():
    """Hàm chính: nhập n (5 chữ số) và in kết quả kiểm tra đối xứng."""
    while True:
        n = int(input("Nhập số nguyên dương n (n > 0): "))
        if 10000 <= n < 99999:
            break
        print("Vui lòng nhập một số nguyên dương lớn hơn 0.")
    if kiemTraSoDoiXung(n):
        print(f"{n} là số đối xứng.")
    else:
        print(f"{n} không phải là số đối xứng.")


main()
