class SinhVienPoly:
    def __init__(self, ho_ten, nganh):
        self.__ho_ten = ho_ten
        self.__nganh = nganh

    def get_diem(self):
        pass

    def get_hoc_luc(self):
        diem = self.get_diem()
        if diem is None:
            return "Chưa có điểm"
        elif diem >= 9:
            return "Xuất sắc"
        elif diem >= 8:
            return "Giỏi"
        elif diem >= 7:
            return "Khá"
        elif diem >= 5:
            return "Trung bình"
        else:
            return "Yếu"

    def xuat(self):
        print(f"Họ và tên: {self.__ho_ten}")
        print(f"Ngành học: {self.__nganh}")
        print(f"Điểm: {self.get_diem()}")
        print(f"Học lực: {self.get_hoc_luc()}")

class SinhVienIT(SinhVienPoly):
    def __init__(self, ho_ten, nganh, java, html, css):
        super().__init__(ho_ten, nganh)
        self.java = java
        self.html = html
        self.css = css

    def get_diem(self):
        return (2 * self.java + self.html + self.css) / 4


class SinhVienBiz(SinhVienPoly):
    def __init__(self, ho_ten, nganh, marketing, sales):
        super().__init__(ho_ten, nganh)
        self.marketing = marketing
        self.sales = sales

    def get_diem(self):
        return (2 * self.marketing + self.sales) / 3
