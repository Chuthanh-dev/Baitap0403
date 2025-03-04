from  mon_an import MonAn
from Hoa_don import HoaDon
def main():
    """
    Hàm chính để thực hiện chương trình.
    """
    # Khởi tạo các món ăn
    ga_ran = MonAn("Gà rán", 30000)  # Món Gà rán
    hamburger = MonAn("Hamburger", 25000)  # Món Hamburger
    cocacola = MonAn("Cocacola", 10000)  # Món Cocacola

    # Khởi tạo hóa đơn
    hoa_don = HoaDon()

    print("Chào mừng các bạn đến với nhà hàng thức ăn nhanh!")
    print("Mời bạn nhập số lượng từng món ăn:")

    # Nhập số lượng từng món ăn từ người dùng
    so_luong_ga_ran = int(input(f"{ga_ran.ten}: "))  # Nhập số lượng Gà rán
    so_luong_hamburger = int(input(f"{hamburger.ten}: "))  # Nhập số lượng Hamburger
    so_luong_cocacola = int(input(f"{cocacola.ten}: "))  # Nhập số lượng Cocacola

    # Thêm món ăn vào hóa đơn
    hoa_don.them_monan(ga_ran, so_luong_ga_ran)
    hoa_don.them_monan(hamburger, so_luong_hamburger)
    hoa_don.them_monan(cocacola, so_luong_cocacola)

    # In hóa đơn
    hoa_don.in_hoa_don()


# Gọi hàm chính khi chạy chương trình
if __name__ == "__main__":
    main()
