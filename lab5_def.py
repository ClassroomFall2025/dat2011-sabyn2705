class SanPham:
    def __init__(self,ten_san_pham="", gia=0, giam_gia=0): # truyền vào tham số để chương trình luôn chạy được
        self.__ten_san_pham = ten_san_pham
        self.__gia = gia
        self.__giam_gia = giam_gia

    def thue_nhap_khau(self):
        return self.__gia * 0.1
    
    # def ghi_giam_gia(self,giam_gia_moi):
    #     self.__giam_gia = giam_gia_moi

    def nhap_thong_tin_san_pham(self):
        self.__ten_san_pham = input("Nhập tên sản phẩm: ")
        self.__gia = float(input("Nhập giá sản phẩm: "))
        self.__giam_gia = float(input("Nhập giảm giá sản phẩm: "))

#getter và setter "Tên SP"
    def get_ten_sp  (self):
        return self.__ten_san_pham
    def set_ten_sp(self,_ten_san_pham):
        self.__ten_san_pham = _ten_san_pham

#getter và setter "Giá SP"
    def get_gia(self):
        return self.__gia
    def set_gia(self,_gia):
        self.__gia = _gia

#getter và setter "Giảm Giá"
    def get_giam_gia(self):
        return self.__giam_gia  
    def set_giam_gia(self,_giam_gia):
        self.__giam_gia = _giam_gia
    
    # Hàm để xuất in thông tin ra terminal  
    def xuat_thong_tin_san_pham(self):
        print(f"Sản Phẩm {self.__ten_san_pham} có giá {self.__gia} \nGiảm giá {self.__giam_gia} \nThuế nhập khẩu là {self.thue_nhap_khau()}")

    def __str__(self):
        return f"Sản Phẩm {self.__ten_san_pham} có giá {self.__gia} \nGiảm giá {self.__giam_gia} \nThuế nhập khẩu là {self.thue_nhap_khau()}"

