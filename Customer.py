class Customer:
    def __init__(self,Id,Name,Address,Phonenumber):
        self.Id=Id
        self.Name=Name
        self.Address=Address
        self.Phonenumber=Phonenumber
    def __str__(self):
        return f"{self.Id}\t{self.Name}\t{self.Address}\t{self.Phonenumber}"