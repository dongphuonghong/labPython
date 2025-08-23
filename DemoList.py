""" s = input("Nhập dãy số nguyên cách nhau bằng dấu cách: ").split()
a = []
for s in s:
    a.append(int(s))
print("Dãy số nguyên đã nhập là:", a)
 """
""" def nhap_so_nguyen_duong(thong_bao):
    while True:
        try:
            n = int(input(thong_bao))
            if n > 0:
                return n
            else:
                print("Vui lòng nhập một số nguyên dương lớn hơn 0.")
        except ValueError:
            print("Đây không phải là số nguyên. Vui lòng nhập lại.")

def nhap_danh_sach(n):
    ds = []
    print(f"Nhập {n} số nguyên:")
    for i in range(n):
        while True:
            try:
                x = int(input(f"Phần tử thứ {i + 1}: "))
                ds.append(x)
                break
            except ValueError:
                print("Không hợp lệ, vui lòng nhập lại.")
    return ds

def xuat_danh_sach(ds):
    print("Danh sách các số nguyên vừa nhập là:")
    print(" ".join(str(x) for x in ds))

# Chương trình chính
if __name__ == "__main__":
    n = nhap_so_nguyen_duong("Nhập số lượng phần tử: ")
    danh_sach = nhap_danh_sach(n)
    xuat_danh_sach(danh_sach)
 """