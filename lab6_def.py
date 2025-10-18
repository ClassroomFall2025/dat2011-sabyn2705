class ChuNhat:
    def __init__(self, dai=0, rong=0):
        self.__dai = dai
        self.__rong = rong

    def get_chu_vi(self):
        return (self.__dai + self.__rong) * 2

    def get_dien_tich(self):
        return self.__dai * self.__rong

    def xuat(self):
        print(f"---HÌNH CHỮ NHẬT---:\n"
          f"Chiều dài là: {self.__dai}\n"
          f"Chiều rộng là: {self.__rong}\n"
          f"Chu vi là: {self.get_chu_vi()}\n"
          f"Diện tích là: {self.get_dien_tich()}")



class Vuong(ChuNhat):
    def __init__(self,canh=0):
        super().__init__(canh, canh)

    def xuat(self):
        print(f"---HÌNH VUÔNG---:\n"
          f"Cạnh là: {self.__dai}\n"
          f"Chu vi là: {self.get_chu_vi()}\n"
          f"Diện tích là: {self.get_dien_tich()}")
