class NhanVien:
    def __init__(self, ma_nv, ho_ten, luong):
        self.ma_nv = ma_nv
        self.ho_ten = ho_ten
        self.luong = luong

    def getThuNhap(self):
        return self.luong

    def getThueTN(self):
        thu_nhap = self.getThuNhap()
        if thu_nhap > 15000000:
            return thu_nhap * 0.12
        elif thu_nhap >= 9000000:
            return thu_nhap * 0.10
        else:
            return 0

    def xuat(self):
        thu_nhap = self.getThuNhap()
        thue = self.getThueTN()
        print(f"Mã NV: {self.ma_nv} | Tên: {self.ho_ten} | Lương: {self.luong} VNĐ")
        print(f"    -> Thu nhập: {thu_nhap} VNĐ | Thuế: {thue} VNĐ")

class TiepThi(NhanVien):
    def __init__(self, ma_nv, ho_ten, luong, doanh_so, hoa_hong):
        super().__init__(ma_nv, ho_ten, luong)
        self.doanh_so = doanh_so
        self.hoa_hong = hoa_hong

    def getThuNhap(self):
        return super().getThuNhap() + (self.doanh_so * self.hoa_hong)

class TruongPhong(NhanVien):
    def __init__(self, ma_nv, ho_ten, luong, trach_nhiem):
        super().__init__(ma_nv, ho_ten, luong)
        self.trach_nhiem = trach_nhiem

    def getThuNhap(self):
        return super().getThuNhap() + self.trach_nhiem