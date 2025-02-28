# 🌟 **Ví dụ sử dụng**
from MODELS.Admin import WarehouseStaff, LoginManager

if __name__ == "__main__":
    print("/nTEST WAREHOUSE STAFF")
    staff1 = WarehouseStaff("S001", "Alice Johnson", "Manager", "555-1234", "alice@company.com")
    staff2 = WarehouseStaff("S002", "Bob Smith", "Stock Keeper", "555-5678", "bob@company.com")
    print(staff1)
    print(staff2)

    print("/nTEST LOGIN MANAGER ")
    login_manager = LoginManager()
    login_manager.register_account(staff1, "alice_admin", "password123")
    login_manager.register_account(staff2, "bob_keeper", "password456")
    login_manager.register_account(staff1, "alice_admin", "newpass")  # Thử đăng ký lại tài khoản đã tồn tại

    login_manager.login("alice_admin", "password123")  # Đăng nhập thành công
    login_manager.login("bob_keeper", "wrongpassword")  # Sai mật khẩu

    login_manager.display_registered_accounts()