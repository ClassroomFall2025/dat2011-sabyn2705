#ASM.01
from ASM_CL import NhanVien, TiepThi, TruongPhong

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

def tim_nv_theo_ma():
    pass

def xoa_nv_theo_ma():
    pass

def capnhat_nv_theo_ma():
    pass

def tim_nv_theo_khoang_luong():
    pass

def sapxep_theo_hoten():
    pass

def sapxep_theo_thunhap():
    pass

def top5_thunhap():
    pass
