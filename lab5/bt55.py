# 55. Cho 2 số nguyên a, b. Viết hàm hoán vị giá trị 2 số trên.
#đây là hàm hoán vị giá trị của hai số nguyên a và b
# Hàm này sẽ trả về giá trị của a và b sau khi hoán vị
def hoanVi(a, b):
    return b, a
#đây là Hàm chính để chạy chương trình
# Hàm này sẽ yêu cầu người dùng nhập hai số nguyên a và b, sau đó gọi hàm hoanVi để hoán vị giá trị của chúng.
# Cuối cùng, nó sẽ in ra giá trị của a và b sau khi hoán
def main():
    a= int(input("Nhập số nguyên a: "))
    b= int(input("Nhập số nguyên b: "))
    a, b = hoanVi(a, b)
    print(f"Sau khi hoán vị: a = {a}, b = {b}")