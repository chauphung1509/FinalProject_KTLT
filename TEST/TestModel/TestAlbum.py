""" TEST ALBUM """
from MODELS.Album import AlbumManager, Album
manager = AlbumManager()
# Thêm album với thể loại và năm xuất bản khác nhau
album1 = Album("Thriller", "Michael Jackson", "Pop", "US/UK", 1982, 15.99, 20)
album2 = Album("Born Pink", "Blackpink", "Pop", "Kpop", 2022, 18.99, 25)
album3 = Album("Midnights", "Taylor Swift", "Pop", "US/UK", 2022, 16.99, 30)
manager.add_album(album1)
manager.add_album(album2)
manager.add_album(album3)

print("Danh sách album trong kho:")
manager.print_all_albums()

print("\nTìm album có ID chứa '22KP':")
found_albums = manager.find_album("Blackpink")
if found_albums:
    for album in found_albums:
        print(album)
else:
    print("Không tìm thấy album.")

print("\nXóa album '82US001' và in lại danh sách:")
manager.remove_album("82US001")
manager.print_all_albums()

