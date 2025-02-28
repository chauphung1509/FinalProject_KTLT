class WarehouseStaff:
    def __init__(self, staff_id, name, position, contact_number, email):
        self.staff_id = staff_id  # Mã nhân viên
        self.name = name  # Tên nhân viên
        self.position = position  # Chức vụ
        self.contact_number = contact_number  # Số điện thoại liên hệ
        self.email = email  # Email nhân viên

    def __str__(self):
        return f"{self.staff_id}\t{self.name}\t{self.position}\t{self.contact_number}\t{self.email}"


class LoginManager:
    def __init__(self):
        self.valid_accounts = {}  # Danh sách tài khoản hợp lệ {username: password}
        self.staffs = {}  # Danh sách tài khoản gắn với thông tin nhân viên {username: WarehouseStaff}

    def register_account(self, staff, username, password):
        """Đăng ký tài khoản nếu nhân viên chưa có tài khoản."""
        if username in self.valid_accounts:
            print(f"Tài khoản {username} đã tồn tại. Đăng ký thất bại.")
        else:
            self.valid_accounts[username] = password
            self.staffs[username] = staff
            print(f"Tài khoản {username} đã được đăng ký thành công cho nhân viên {staff.name}.")

    def login(self, username, password):
        """Xác thực đăng nhập."""
        if username in self.valid_accounts and self.valid_accounts[username] == password:
            print("Đăng nhập thành công!")
            return True
        else:
            print("Sai tên đăng nhập hoặc mật khẩu.")
            return False

    def display_registered_accounts(self):
        """Hiển thị danh sách tài khoản đã đăng ký cùng thông tin nhân viên."""
        print("Danh sách tài khoản quản lý:")
        print(f"{'Username':<15}{'Staff ID':<10}{'Name':<20}{'Position':<15}{'Contact':<15}{'Email':<20}")
        print("-" * 90)
        for username, staff in self.staffs.items():
            print(
                f"{username:<15}{staff.staff_id:<10}{staff.name:<20}{staff.position:<15}{staff.contact_number:<15}{staff.email:<20}")
