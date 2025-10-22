# main.py
from tai_khoan import TaiKhoan
from file_handler import doc_tai_khoan_tu_csv, ghi_tai_khoan_vao_csv
from utils import sao_luu_du_lieu, khoi_phuc_du_lieu, format_tien

def tim_tk(danh_sach, so_tk):
    for tk in danh_sach:
        if tk.so_tk == so_tk:
            return tk
    return None

def menu():
    danh_sach = doc_tai_khoan_tu_csv()

    while True:
        print("""
========= MENU CHÍNH =========
1. Tạo tài khoản mới
2. Gửi tiền
3. Rút tiền
4. Kiểm tra số dư
5. Danh sách tất cả tài khoản
6. Đóng tài khoản
7. Chỉnh sửa tài khoản
8. Tìm kiếm theo tên
9. Xuất báo cáo
10. Sao lưu dữ liệu
11. Khôi phục dữ liệu
12. Thoát
==============================
        """)

        chon = input("Chọn chức năng: ").strip()

        if chon == "1":
            so_tk = input("Nhập số tài khoản: ")
            ten = input("Nhập Họ và tên: ")
            loai = input("Nhập loại (T/C): ").upper()
            so_du = float(input("Nhập số dư ban đầu: "))
            tk = TaiKhoan(so_tk, ten, loai, so_du)
            danh_sach.append(tk)
            ghi_tai_khoan_vao_csv(danh_sach)
            print(" Đã tạo tài khoản thành công.")

        elif chon == "2":
            so_tk = input("Nhập số tài khoản cần gửi: ")
            tk = tim_tk(danh_sach, so_tk)
            if tk:
                so_tien = float(input("Nhập số tiền gửi: "))
                tk.gui_tien(so_tien)
                ghi_tai_khoan_vao_csv(danh_sach)
                print(" Gửi tiền thành công!")
            else:
                print(" Không tìm thấy tài khoản.")

        elif chon == "3":
            so_tk = input("Nhập số tài khoản cần rút: ")
            tk = tim_tk(danh_sach, so_tk)
            if tk:
                so_tien = float(input("Nhập số tiền rút: "))
                tk.rut_tien(so_tien)
                ghi_tai_khoan_vao_csv(danh_sach)
            else:
                print(" Không tìm thấy tài khoản.")

        elif chon == "4":
            so_tk = input("Nhập số tài khoản: ")
            tk = tim_tk(danh_sach, so_tk)
            if tk:
                print(f"Số dư hiện tại: {format_tien(tk.so_du)}")
            else:
                print(" Không tìm thấy tài khoản.")

        elif chon == "5":
            print("\n DANH SÁCH TÀI KHOẢN:")
            for tk in danh_sach:
                tk.hien_thi()

        elif chon == "6":
            so_tk = input("Nhập số tài khoản cần xóa: ")
            danh_sach = [tk for tk in danh_sach if tk.so_tk != so_tk]
            ghi_tai_khoan_vao_csv(danh_sach)
            print(" Đã xóa tài khoản.")

        elif chon == "7":
            so_tk = input("Nhập số tài khoản cần chỉnh sửa: ")
            tk = tim_tk(danh_sach, so_tk)
            if tk:
                tk.ten = input("Tên mới: ") or tk.ten
                tk.loai = input("Loại mới (T/C): ") or tk.loai
                tk.so_du = float(input("Số dư mới: ") or tk.so_du)
                ghi_tai_khoan_vao_csv(danh_sach)
                print(" Đã cập nhật thông tin.")
            else:
                print(" Không tìm thấy tài khoản.")

        elif chon == "8":
            keyword = input("Nhập từ khóa tên: ").lower()
            ket_qua = [tk for tk in danh_sach if keyword in tk.ten.lower()]
            for tk in ket_qua:
                tk.hien_thi()

        elif chon == "9":
            tong_tk = len(danh_sach)
            tong_tien = sum(tk.so_du for tk in danh_sach)
            with open("data/baocao.txt", "w", encoding="utf-8") as f:
                f.write(f"Tổng số tài khoản: {tong_tk}\n")
                f.write(f"Tổng số dư: {format_tien(tong_tien)}\n")
            print(" Đã xuất báo cáo ra data/baocao.txt")

        elif chon == "10":
            sao_luu_du_lieu()

        elif chon == "11":
            khoi_phuc_du_lieu()
            danh_sach = doc_tai_khoan_tu_csv()  # cập nhật lại dữ liệu

        elif chon == "12":
            print(" Thoát chương trình. Tạm biệt Bủn!")
            break

        else:
            print(" Lựa chọn không hợp lệ, thử lại nha.")
if __name__ == "__main__":
    menu()
