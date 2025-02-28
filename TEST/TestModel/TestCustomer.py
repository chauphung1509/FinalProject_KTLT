# Tạo khách hàng tổ chức
from MODELS.Customer import Business, Individual, Customer

b1 = Business(101, "ABC Corp", "John Doe", "123456789", "123 Street A")
b2 = Business(102, "XYZ Ltd", "Jane Doe", "987654321", "456 Street B")

# Tạo khách hàng cá nhân
i1 = Individual(201, "Alice", "5551234", "789 Street C")
i2 = Individual(202, "Bob", "5555678", "101 Street D")

# Quản lý danh sách khách hàng
customer_manager = Customer()

# Thêm một khách hàng
customer_manager.add_customer(b1)
customer_manager.add_customer(i1)

# Thêm nhiều khách hàng
customer_manager.add_customers([b2, i2])

# In danh sách khách hàng
print("All Customers:")
customer_manager.print_all_customers()

# Xóa một khách hàng
customer_manager.remove_customers(101)

# In lại danh sách khách hàng sau khi xóa
print("\nCustomers after removing ID 101:")
customer_manager.print_all_customers()


