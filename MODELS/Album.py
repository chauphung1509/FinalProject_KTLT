class Album:
    album_counter = {}  # Dictionary lưu số thứ tự album theo từng năm + thể loại
    MUSIC_TYPE_CODES = {
        "Kpop": "KP",
        "Vpop": "VP",
        "US/UK": "US",
        "Cpop": "CP",
        "Jpop": "JP",
        "Other": "OT"
    }

    def __init__(self, title, artist, genre, category, year, price, stock):
        self.title = title  # Tiêu đề album
        self.artist = artist  # Tên nghệ sĩ
        self.genre = genre  # Thể loại nhạc (Rock, Pop, ...) - listwidget
        self.category = category  # Thể loại âm nhạc (Kpop, US/UK, ...) - listwidget
        self.year = year  # Năm phát hành - year
        self.price = price  # Giá album
        self.stock = stock  # Số lượng tồn kho - auto cập nhật, nếu thêm mới thì stock = 0

        # Tạo ID dựa trên năm xuất bản + thể loại nhạc
        self.id = self.generate_album_id()

    def generate_album_id(self):
        #Tự động tạo id cho album được thêm mới
        year_short = str(self.year)[-2:]  # Lấy 2 số cuối của năm
        music_code = self.MUSIC_TYPE_CODES.get(self.category, "OT")  # Lấy mã thể loại, nếu không có thì mặc định "OT"

        # Kiểm tra nếu chưa có bộ đếm cho năm + thể loại này thì đặt về 1
        key = f"{year_short}{music_code}"
        if key not in Album.album_counter:
            Album.album_counter[key] = 1
        else:
            Album.album_counter[key] += 1

        counter = f"{Album.album_counter[key]:03d}"  #định dạng số thứ tự 3 chữ số (001, 002,...)
        return f"{year_short}{music_code}{counter}"

    def __str__(self):
        return f"{self.id}\t{self.title}\t{self.artist}\t{self.genre}\t{self.category}\t{self.year}\t${self.price}\tStock: {self.stock}"


class AlbumManager:
    def __init__(self):
        self.albums = []  # Danh sách chứa các album

    def add_album(self, album):
        self.albums.append(album)

    def remove_album(self, album_id): #xóa album theo id
        self.albums = [alb for alb in self.albums if alb.id != album_id]

    def print_all_albums(self):
        for alb in self.albums:
            print(alb)

    def find_album(self, search_term):
        #Tìm album theo bất kỳ loại input nào
        results = [alb for alb in self.albums if
                   search_term.lower() in alb.id.lower() or
                   search_term.lower() in alb.title.lower() or
                   search_term.lower() in alb.artist.lower() or
                   search_term.lower() in alb.genre.lower() or
                   search_term.lower() in alb.category.lower() or
                   search_term in str(alb.year)]
        return results if results else None
