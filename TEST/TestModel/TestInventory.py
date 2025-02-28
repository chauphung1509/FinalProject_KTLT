# 🌟 **Ví dụ sử dụng**
from MODELS.Album import Album
from MODELS.Inventory import Inventory
from MODELS.Vendor import Vendor

if __name__ == "__main__":
    inventory = Inventory()
    vendor1 = Vendor("V001", "Universal Music", "New York, USA", "123-456-789", "contact@universal.com")

    album1 = Album("Thriller", "Michael Jackson", "Pop", "US/UK", 1982, 15.99, 0)
    album2 = Album("Born Pink", "Blackpink", "Pop", "Kpop", 2022, 18.99, 0)

    vendor1.add_album(album1)
    vendor1.add_album(album2)

    inventory.add_stock(vendor1, album1, 50)
    inventory.add_stock(vendor1, album2, 30)

    inventory.display_stock()

    inventory.remove_stock(album1.id, 10)
    inventory.display_stock()
