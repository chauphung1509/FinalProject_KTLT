from MODELS.Album import Album
from MODELS.Receipt import InventoryReceipt
from MODELS.Vendor import Vendor

if __name__ == "__main__":
    vendor1 = Vendor("V001", "Universal Music", "New York, USA", "123-456-789", "contact@universal.com")
    album1 = Album("Thriller", "Michael Jackson", "Pop", "US/UK", 1982, 15.99, 0)
    album2 = Album("Born Pink", "Blackpink", "Pop", "Kpop", 2022, 18.99, 0)

    receipt = InventoryReceipt("R001", vendor1, "2025-02-20")
    receipt.add_item(album1, 50, 12.99)
    receipt.add_item(album2, 30, 14.99)

    receipt.display_receipt()
