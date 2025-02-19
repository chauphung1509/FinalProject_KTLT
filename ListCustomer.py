class ListCustomer:
    def __init__(self):
        self.customers=[]
    def add_customer(self,c):# them customer
        self.customers.append(c)
    def add_customers(self,arr_cus):#them nhieu customer
        self.customers.extend(arr_cus)
    def remove_customers(self,id):#xoa customer
        for c in self.customers:
            if c.Id==id:
               self.customers.remove(c)
    def print_all_customers(self):# in ra tat ca cac customer
        for c in self.customers:
            print(c)
