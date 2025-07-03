# 48. Nhập số nguyên dương n (0 <= n< 1000) và in ra cách đọc của n.
# Đây là hàm đọc số nguyên dương n (0 <= n < 1000) và trả về cách đọc của nó
# theo quy tắc đọc số tiếng Việt.
def doc_so(n):
    if n < 0 or n >= 1000:
        return "Số không hợp lệ. Vui lòng nhập số trong khoảng từ 0 đến 999."
    don_vi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", 
            "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]
    if n == 0:
        return "không"
    if n < 10:
        return don_vi[n]
    if n < 20:
        return chuc[1] + ("" if n == 10 else " lăm" if n == 15 else f" {don_vi[n % 10]}")
    if n < 100:
        return chuc[n // 10] + ("" if n % 10 == 0 else f" {don_vi[n % 10]}")
    return f"{don_vi[n // 100]} trăm" + ("" if n % 100 == 0 else f" {doc_so(n % 100)}")
# Đây là hàm main để chạy chương trình nhập dữ liệu và hiển thị kết quả
# Hàm main sẽ gọi hàm doc_so để đọc số và in ra kết quả
def main():
    n = int(input("Nhập số nguyên dương n (0 <= n < 1000): "))
    print(doc_so(n))
main()