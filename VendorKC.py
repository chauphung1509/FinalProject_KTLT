class Vendor:
    def __init__(self, vendor_number, name, address, contact_number, email):
        self.vendor_number = vendor_number
        self.name = name
        self.address = address
        self.contact_number = contact_number
        self.email = email
        self.albums = []  # Danh sách album mà vendor cung cấp

    def add_album(self, album):
        self.albums.append(album)

    def remove_album(self, album):
        if album in self.albums:
            self.albums.remove(album)

    def get_album_list(self): # Trả về danh sách album
        return self.albums

    def display_info(self):
        print(f"Vendor Number: {self.vendor_number}")
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Contact: {self.contact_number}")
        print(f"Email: {self.email}")
        print(f"Albums: {', '.join(self.albums) if self.albums else 'No albums available'}")

# Ví dụ sử dụng
vendor1 = Vendor(101, "Music World", "123 Street, City", "0123456789", "musicworld@email.com")
vendor1.add_album("Album A")
vendor1.add_album("Album B")
vendor1.display_info()
