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

    def get_album_list(self):  # Trả về danh sách album
        return self.albums

    def __str__(self):
        return f"{self.vendor_number}\t{self.name}\t{self.address}\t{self.contact_number}\t{self.email}"
