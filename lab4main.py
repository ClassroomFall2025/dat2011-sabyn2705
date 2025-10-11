# Sinh viên code Lab ở đây import Lab4
from lab4 import loc_so_chan 
from lab4 import tinh_nguyen_lieu
from lab4 import tinh_tien_nuoc
from lab4 import menu

# Bài 1
print("Bài 1: Tính tiền nước")
for m3 in [12, 23, 34]:
    print(f"{m3} m3 => {tinh_tien_nuoc(m3)} VND")

# Bài 2
print("\nBài 2: Nguyên liệu hộp bánh")
print(tinh_nguyen_lieu(2, 3, 1)) 

# Bài 3
print("\nBài 3: Lọc số chẵn")
ds = [1, 2, 3, 4, 5, 6]
print("Danh sách:", ds)
print("Số chẵn:", loc_so_chan(ds))

# Bài 4
menu()