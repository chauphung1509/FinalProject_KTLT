#Xuất phiếu nhập hàng
class InventoryReceipt:
    def __init__(self, receipt_id, vendor, date):
        self.receipt_id = receipt_id  # Mã phiếu nhập
        self.vendor = vendor  # Nhà cung cấp
        self.date = date  # Ngày nhập hàng
        self.items = []  # Danh sách các album nhập

    def add_item(self, album, quantity, unit_price):
        """Thêm album vào phiếu nhập với số lượng và giá nhập"""
        self.items.append({
            'album': album,
            'quantity': quantity,
            'unit_price': unit_price,
            'total_price': quantity * unit_price
        })

    def display_receipt(self):
        """Hiển thị thông tin phiếu nhập hàng"""
        print(f"Phiếu Nhập Hàng: {self.receipt_id}")
        print(f"Nhà cung cấp: {self.vendor.name}\tNgày: {self.date}")
        print("-" * 50)
        print(f"{'Album ID':<10}{'Tên Album':<20}{'Số lượng':<10}{'Đơn giá':<10}{'Thành tiền':<10}")
        print("-" * 50)
        total_amount = 0
        for item in self.items:
            album = item['album']
            print(f"{album.id:<10}{album.title:<20}{item['quantity']:<10}{item['unit_price']:<10}{item['total_price']:<10}")
            total_amount += item['total_price']
        print("-" * 50)
        print(f"Tổng tiền: {total_amount}")