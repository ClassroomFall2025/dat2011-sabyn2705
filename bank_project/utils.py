import shutil
import os
from datetime import datetime

# Định dạng tiền tệ
def format_tien(so_tien):
    return f"{so_tien:,.0f} VNĐ"

# Tạo file sao lưu
def sao_luu_du_lieu(src="data/taikhoan.csv", dest_folder="backup"):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest_file = f"{dest_folder}/taikhoan_backup_{timestamp}.csv"
    shutil.copy(src, dest_file)
    print(f" Đã sao lưu dữ liệu vào: {dest_file}")

# Khôi phục dữ liệu từ file backup
def khoi_phuc_du_lieu(dest="data/taikhoan.csv"):
    backup_files = [f for f in os.listdir("backup") if f.endswith(".csv")]
    if not backup_files:
        print(" Không có file backup nào để khôi phục.")
        return
    print("\n Danh sách file backup:")
    for i, f in enumerate(backup_files, 1):
        print(f"{i}. {f}")

    chon = int(input("Chọn file số: "))
    if 1 <= chon <= len(backup_files):
        shutil.copy(f"backup/{backup_files[chon-1]}", dest)
        print(" Khôi phục dữ liệu thành công.")
    else:
        print(" Lựa chọn không hợp lệ.")
