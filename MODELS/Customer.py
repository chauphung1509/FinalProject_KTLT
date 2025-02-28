class Customer:
    def __init__(self, id=None):
        self.id = id
        self.type = None  # loại khách hàng: cá nhân/ tổ chức
        self.customers = []

    def add_customer(self, c):  # them customer
        self.customers.append(c)

    def add_customers(self, arr_cus):  # them nhieu customer
        self.customers.extend(arr_cus)

    def remove_customers(self, id):  # xoa customer
        self.customers = [c for c in self.customers if c.id != id]

    def print_all_customers(self):  # in ra tat ca cac customer
        for c in self.customers:
            print(c)

    def discount_rate(self):
        pass

    def __str__(self):
        pass


class Business(Customer):
    def __init__(self, id=None, name=None, person=None, phone=None, address=None):
        super().__init__(id)
        self.name = name  # tên tổ chức
        self.person = person  # tên người đại diện liên hệ
        self.phone = phone  # số điện thoại liên hệ
        self.address = address  # địa chỉ giao hàng
        self.type = "Business"

    def __str__(self):
        return (
            f"{self.id}\t{self.type}\t{self.name}\t"
            f"{self.person}\t{self.phone}\t{self.address}"
        )

    def discount_rate(self):  # trả về mức ưu đãi khi mua sỉ
        return 0.1


class Individual(Customer):
    def __init__(self, id=None, name=None, phone=None, address=None):
        super().__init__(id)
        self.name = name  # tên của cá nhân
        self.phone = phone  # số điện thoại liên hệ
        self.address = address  # địa chỉ giao hàng
        self.type = "Individual"

    def __str__(self):
        return (
            f"{self.id}\t{self.type}\t{self.name}\t"
            f"{self.phone}\t{self.address}"
        )

    def discount_rate(self):
        return 0.0

