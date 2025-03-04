from mon_an import MonAn
def main():
    # Khởi tạo các món ăn với mô tả và hình ảnh
    ga_ran = MonAn("Gà rán", 30000, "Gà chiên giòn, nóng hổi.", "images/ga_ran.jpg")
    hamburger = MonAn("Hamburger", 25000, "Bánh mì kẹp thịt bò, phô mai.", "images/hamburger.jpg")
    cocacola = MonAn("Cocacola", 10000, "Nước ngọt có ga, mát lạnh.", "images/cocacola.jpg")

    # Hiển thị thông tin chi tiết về các món ăn
    ga_ran.hien_thi_thong_tin()
    print()
    hamburger.hien_thi_thong_tin()
    print()
    cocacola.hien_thi_thong_tin()

# Gọi hàm chính khi chạy chương trình
if __name__ == "__main__":
    main()
