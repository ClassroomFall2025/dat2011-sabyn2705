# sinh viên xây dựng các hàm trong lớp 4 ở đây

# Bài 1: Tính tiền nước sinh hoạt
def tinh_tien_nuoc(so_m3):
    gia_ban_nuoc = (7500, 8800, 12000, 24000)
    if so_m3 <= 10:
        return so_m3 * gia_ban_nuoc[0]
    elif so_m3 <= 20:
        return 10 * gia_ban_nuoc[0] + (so_m3 - 10) * gia_ban_nuoc[1]
    elif so_m3 <= 30:
        return (10 * gia_ban_nuoc[0] +
                10 * gia_ban_nuoc[1] +
                (so_m3 - 20) * gia_ban_nuoc[2])
    else:
        return (10 * gia_ban_nuoc[0] +
                10 * gia_ban_nuoc[1] +
                10 * gia_ban_nuoc[2] +
                (so_m3 - 30) * gia_ban_nuoc[3])

# Bài 2: Tính nguyên liệu làm hộp bánh
def tinh_nguyen_lieu(so_banh_dau_xanh, so_banh_thap_cam, so_banh_deo):
    sugar = so_banh_dau_xanh * 0.04 + so_banh_thap_cam * 0.06 + so_banh_deo * 0.05
    bean = so_banh_dau_xanh * 0.07 + so_banh_thap_cam * 0 + so_banh_deo * 0.02
    return {"sugar": sugar, "bean": bean}

# Bài 3: Lọc số chẵn từ danh sách
def loc_so_chan(ds):
    try:
        return list(filter(lambda x: int(x) % 2 == 0, ds))
    except ValueError:
        raise ValueError("Danh sách phải chứa toàn số nguyên!")

# Bài 4: Thực đơn menu
def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Tính tiền nước sinh hoạt")
        print("2. Tính nguyên liệu làm hộp bánh")
        print("3. Lọc số chẵn từ dãy số")
        print("4. Thoát")
        try:
            choice = int(input("Chọn chức năng (1-4): "))
            if choice == 1:
                so_m3 = int(input("Nhập số m3 nước: "))
                print("Tiền nước phải trả:", tinh_tien_nuoc(so_m3))
            elif choice == 2:
                dx = int(input("Số bánh đậu xanh: "))
                tc = int(input("Số bánh thập cẩm: "))
                deo = int(input("Số bánh dẻo: "))
                print("Nguyên liệu cần:", tinh_nguyen_lieu(dx, tc, deo))
            elif choice == 3:
                ds = input("Nhập dãy số, cách nhau bởi khoảng trắng: ").split()
                ds_int = [int(x) for x in ds]
                print("Số chẵn:", loc_so_chan(ds_int))
            elif choice == 4:
                print("Thoát chương trình.")
                break
            else:
                print("Vui lòng nhập số từ 1-4!")
        except ValueError:
            print("Lỗi: bạn phải nhập số hợp lệ.")