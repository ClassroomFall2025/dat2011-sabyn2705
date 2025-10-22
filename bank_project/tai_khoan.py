class TaiKhoan:
    def __init__(self, so_tk, ten, loai, so_du):
        self.so_tk = so_tk
        self.ten = ten
        self.loai = loai
        self.so_du = so_du

    def hien_thi(self):
        print(f"Số TK: {self.so_tk}, Tên: {self.ten}, Loại: {self.loai}, Số dư: {self.so_du:,.0f} VNĐ")

    def gui_tien(self, so_tien):
        self.so_du += so_tien

    def rut_tien(self, so_tien):
        if so_tien <= self.so_du:
            self.so_du -= so_tien
        else:
            print("Không đủ số dư!")

    def to_dict(self):
        return {"soTaiKhoan": self.so_tk, "ten": self.ten, "loai": self.loai, "soDu": self.so_du}
