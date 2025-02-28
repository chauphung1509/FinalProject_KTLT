from MODELS.Vendor import Vendor

if __name__ == "__main__":
    # Tạo vendor
    v1 = Vendor(1, "Music Store A", "123 Music St.", "0123456789", "contact@musica.com")
    v2 = Vendor(2, "Vinyl Shop B", "456 Vinyl Ave.", "0987654321", "info@vinylb.com")

    # Thêm album vào vendor
    v1.add_album("Greatest Hits - Artist A")
    v1.add_album("Rock Classics - Artist B")
    v2.add_album("Jazz Collection - Artist C")

    # Kiểm tra danh sách album
    print("Danh sách album của Vendor 1:", v1.get_album_list())
    print("Danh sách album của Vendor 2:", v2.get_album_list())

    # Xóa album khỏi vendor
    v1.remove_album("Rock Classics - Artist B")

    # Kiểm tra danh sách album sau khi xóa
    print("\nDanh sách album của Vendor 1 sau khi xóa:", v1.get_album_list())

    # In thông tin Vendor
    print("\nThông tin Vendor 1:")
    print(v1)

    print("\nThông tin Vendor 2:")
    print(v2)
