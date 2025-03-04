
class MonAn :
    def __init__(self, ten, gia):
        """
        Khởi tạo một món ăn với tên và giá.
        :param ten:
        :param gia:
        """
        self.ten= ten
        self.gia = gia
'''
class MonAn:
    def __init__(self, ten, gia, mo_ta="", hinh_anh=""):
        """
        Khởi tạo một món ăn với tên, giá, mô tả và hình ảnh.

        :param ten: Tên của món ăn.
        :param gia: Giá của món ăn.
        :param mo_ta: Mô tả của món ăn (tùy chọn).
        :param hinh_anh: Đường dẫn hình ảnh của món ăn (tùy chọn).
        """
        self.ten = ten  # Tên món ăn
        self.gia = gia  # Giá món ăn
        self.mo_ta = mo_ta  # Mô tả món ăn
        self.hinh_anh = hinh_anh  # Hình ảnh món ăn

    def hien_thi_thong_tin(self):
        """
        Hiển thị thông tin chi tiết về món ăn.
        """
        print(f"Tên: {self.ten}")
        print(f"Giá: {self.gia:,}đ")
        print(f"Mô tả: {self.mo_ta}")
        if self.hinh_anh:
            print(f"Hình ảnh: {self.hinh_anh}")
'''