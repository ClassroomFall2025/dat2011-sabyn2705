#ASM.01
from ASM_CL import NhanVien, TiepThi, TruongPhong

ds_nv = []

#1
def nhap_danh_sach_nv():                          
    n = int(input("Nhập số lượng nhân viên: "))
    for i in range(n):
        print(f"\n--- Nhập nhân viên thứ {i+1} ---")
        loai = input("Loại nhân viên (1: Hành chính | 2: Tiếp thị | 3: Trưởng phòng): ")

        ma_nv = input("Mã nhân viên: ")
        ho_ten = input("Họ tên: ")
        luong = float(input("Lương cơ bản: "))

        if loai == "2": 
            doanh_so = float(input("Doanh số: "))
            hoa_hong = float(input("Hoa hồng (ví dụ: 0.05): "))
            nv = TiepThi(ma_nv, ho_ten, luong, doanh_so, hoa_hong)
        elif loai == "3":  
            trach_nhiem = float(input("Lương trách nhiệm: "))
            nv = TruongPhong(ma_nv, ho_ten, luong, trach_nhiem)
        else: 
            nv = NhanVien(ma_nv, ho_ten, luong)

        ds_nv.append(nv)

    print("\n Đã nhập danh sách nhân viên thành công!")

def luu_vao_file():
    pass

def doc_tu_file():
    pass

#3
def tim_nv_theo_ma():                             
    ma = input("Nhập mã nhân viên cần tìm: ")
    for nv in ds_nv:
        if nv.ma_nv == ma:
            nv.xuat()
            return
    print("Không tìm thấy nhân viên có mã này.")

def xoa_nv_theo_ma():
    pass

def capnhat_nv_theo_ma():
    pass

#6
def tim_nv_theo_khoang_luong():
    min_l = float(input("Nhập lương tối thiểu: "))
    max_l = float(input("Nhập lương tối đa: "))
    found = False

    for nv in ds_nv:
        if min_l <= nv.getThuNhap() <= max_l:
            nv.xuat()
            found = True

    if not found:
        print("Không có nhân viên trong khoảng lương này.")

#7
def sapxep_theo_hoten():
    ds_nv.sort(key=lambda nv: nv.ho_ten)
    print("\n Danh sách nhân viên (sắp xếp theo họ tên):")
    for nv in ds_nv:
        nv.xuat()

#8
def sapxep_theo_thunhap():
    ds_nv.sort(key=lambda nv: nv.getThuNhap(), reverse=True)
    print("\n Danh sách nhân viên (sắp xếp theo thu nhập):")
    for nv in ds_nv:
        nv.xuat()
#9
def top5_thunhap():
    print("\n Top 5 nhân viên có thu nhập cao nhất:")
    top5 = sorted(ds_nv, key=lambda nv: nv.getThuNhap(), reverse=True)[:5]
    for nv in top5:
        nv.xuat()
