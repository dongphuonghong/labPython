"""
8. Viết chương trình cho phép nhập vào thời gian của một công việc nào đó tính bằng giây. Hãy chuyển đổi và in ra màn hình thời gian trên dưới dạng bao nhiêu giờ, bao nhiêu phút, bao nhiêu giây.
"""
#tạo biến cv nhập giá trị từ bàn phím
cv=float(input(" nhap so giay cong viet"))    
#tính giờ
gio= cv//3600   
#tính phút
phut= (cv%3600)//60 
#tính giây
giay=cv%60        
#xuất kết quả
print("so gio la",gio)  
print("so phut la",phut)    
print("so giay la",giay)