from MODELS.Album import Album
from MODELS.Vendor import Vendor


class Inventory:
    def __init__(self):
        self.stock = {}  # Dictionary để lưu số lượng album trong kho

    def add_stock(self, vendor, album, quantity):
        """Nhập hàng từ vendor và thêm vào kho."""
        if album not in vendor.get_album_list():
            print(f"Vendor {vendor.name} không cung cấp album {album.title}.")
            return

        if album.id in self.stock:
            self.stock[album.id]['quantity'] += quantity
        else:
            self.stock[album.id] = {'album': album, 'quantity': quantity}

        print(f"Nhập {quantity} bản album '{album.title}' từ {vendor.name} vào kho.")

    def remove_stock(self, album_id, quantity):
        #Xóa số lượng album khỏi kho khi bán hàng hoặc điều chỉnh.
        if album_id in self.stock:
            if self.stock[album_id]['quantity'] >= quantity:
                self.stock[album_id]['quantity'] -= quantity
                print(f"Đã xuất {quantity} bản album '{self.stock[album_id]['album'].title}' khỏi kho.")
                if self.stock[album_id]['quantity'] == 0:
                    del self.stock[album_id]
            else:
                print("Không đủ số lượng trong kho.")
        else:
            print("Album không tồn tại trong kho.")

    def display_stock(self):
        print("\nDanh sách hàng trong kho:")
        for album_id, data in self.stock.items():
            print(f"{album_id}\t{data['album'].title}\t{data['album'].artist}\tSố lượng: {data['quantity']}")


