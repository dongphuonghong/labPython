# 26. Viêt chương trinh đêm sô ươc sô cua sô nguyên dương N.Vi du:  N=12sô ươc sô cua 12 la 6
# Nhập số nguyên dương từ bàn phím
n=int(input("Nhap so nguyen duong N: "))
# Khởi tạo biến đếm số ước số = 0
d=0
# Dùng vòng lặp while để đếm số ước số của n
i=1
while i<=n:
    # Kiểm tra nếu n chia hết cho i thì i là ước số của n
    if n%i==0:
        d+=1
    i+=1
# In ra tổng số ước số của n
print("Tổng số ước của", n, "là", d)