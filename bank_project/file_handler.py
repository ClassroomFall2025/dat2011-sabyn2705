import csv
from tai_khoan import TaiKhoan
import os

DATA_FILE = "data/taikhoan.csv"
os.makedirs("data", exist_ok=True)

def doc_tai_khoan_tu_csv():
    danh_sach = []
    try:
        with open(DATA_FILE, "r", newline='', encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                tk = TaiKhoan(row["soTaiKhoan"], row["ten"], row["loai"], float(row["soDu"]))
                danh_sach.append(tk)
    except FileNotFoundError:
        pass 
    return danh_sach

def ghi_tai_khoan_vao_csv(danh_sach):
    with open(DATA_FILE, "w", newline='', encoding="utf-8") as f:
        fieldnames = ["soTaiKhoan", "ten", "loai", "soDu"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for tk in danh_sach:
            writer.writerow(tk.to_dict())
