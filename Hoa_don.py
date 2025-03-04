class HoaDon :
    def __init__(self):
        """
        Khởi tạo hóa đơn rỗng.
        """
        self.mon_an_list = [] #Khởi tạo ds rỗng đễ lưu món ăn
        self.so_luong = {} #Số lượng từng món ăn
    def them_mon_an(self, mon_an, so_luong):
        """
        Thêm món ăn và số lượng vào hóa đơn.
        :param mon_an:
        :param so_luong:
        :return:
        """
        self.mon_an_list.append(mon_an) #Thêm món ăn vào ds
        self.so_luong[mon_an.ten] = so_luong #Lưu số lượng món ăn
    def tinh_tong(self ):
        """
        tính tổng tiền cho hóa đơn và chi tiết hóa đơn.
        :return: tổng tiền và chi tiết hóa đơn
        """
        tong_tien =0
        chi_tiet_hoa_don =[] #DS chi tiết hóa đơn
        #Duyệt qua từng món ăn để tính tiền
        for mon_an in self.mon_an_list:
            so_luong_mua = self.so_luong[mon_an.ten] #số lượng món ăn
            tien = mon_an.gia * so_luong_mua #tính tiền món ăn
            chi_tiet_hoa_don.append((mon_an.ten, mon_an.gia, so_luong_mua, tien)) #lưu chi tiết
            tong_tien +=tien
        return tong_tien , chi_tiet_hoa_don
    def in_hoa_don(self ):
        """
        In hóa đơn với thông tin chi tiết và tổng tiền
        :return:
        """
        tong_tien, chi_tiet_hoa_don = self.tinh_tong()
        thue = tong_tien * 0.05
        tong_tien_sau_thue = tong_tien + thue
        print("\nHóa đơn:")
        #in hóa đơn chi tiết
        for mon_an, gia, so_luong_mua, tien in chi_tiet_hoa_don:
            print(f"{mon_an: <20} {gia:,}đ x {so_luong_mua}")
        #in tổng tiền
        print(f"\nTổng:")
        for mon_an, gia, so_luong_mua, tien in chi_tiet_hoa_don:
            print(f"{mon_an:<20} {tien:,}đ")
        print(f"Tổng trước thuế: {tong_tien:,}đ")
        print(f"Thuế (5%): {thue:,.0f}đ")
        print(f"Tổng sau thuế: {tong_tien_sau_thue:,.0f}đ")




'''
class HoaDon:
    def __init__(self):
        """
        Khởi tạo hóa đơn rỗng.
        """
        self.monan_list = []  # Danh sách các món ăn
        self.so_luong = {}  # Số lượng từng món ăn

    def them_monan(self, mon_an, so_luong):
        """
        Thêm món ăn và số lượng vào hóa đơn.

        :param mon_an: Đối tượng món ăn.
        :param so_luong: Số lượng món ăn.
        """
        self.monan_list.append(mon_an)  # Thêm món ăn vào danh sách
        self.so_luong[mon_an.ten] = so_luong  # Lưu số lượng món ăn

    def tinh_tong(self):
        """
        Tính tổng tiền cho hóa đơn và chi tiết hóa đơn.

        :return: Tổng tiền và chi tiết hóa đơn.
        """
        tong_tien = 0  # Tổng tiền
        chi_tiet_hoa_don = []  # Danh sách chi tiết hóa đơn

        # Duyệt qua từng món ăn để tính tiền
        for mon_an in self.monan_list:
            so_luong_mua = self.so_luong[mon_an.ten]  # Số lượng món ăn
            tien = mon_an.gia * so_luong_mua  # Tính tiền cho món ăn
            chi_tiet_hoa_don.append((mon_an.ten, mon_an.gia, so_luong_mua, tien))  # Lưu chi tiết
            tong_tien += tien  # Cộng dồn vào tổng tiền

        return tong_tien, chi_tiet_hoa_don  # Trả về tổng tiền và chi tiết hóa đơn

    def in_hoa_don(self):
        """
        In hóa đơn với thông tin chi tiết và tổng tiền.
        """
        tong_tien, chi_tiet_hoa_don = self.tinh_tong()  # Tính tổng tiền
        thue = tong_tien * 0.05  # Tính thuế (5%)
        tong_sau_thue = tong_tien + thue  # Tính tổng sau thuế

        print("\nHóa đơn:")
        # In chi tiết hóa đơn
        for mon_an, gia, so_luong_mua, tien in chi_tiet_hoa_don:
            print(f"{mon_an:<20} {gia:,}đ x {so_luong_mua}")  # Định dạng in ra

        # In tổng tiền
        print(f"\nTổng:")
        for mon_an, gia, so_luong_mua, tien in chi_tiet_hoa_don:
            print(f"{mon_an:<20} {tien:,}đ")
        print(f"Tổng trước thuế: {tong_tien:,}đ")
        print(f"Thuế (5%): {thue:,.0f}đ")
        print(f"Tổng sau thuế: {tong_sau_thue:,.0f}đ")
'''