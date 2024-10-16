class Customer:
    def __init__(self, name, address):
        # Constructor to initialize name and address attributes
        self.name = name
        self.address = address

    def __str__(self):
        return f"Customer: {self.name}, Address: {self.address}"
 
 
#display
print()
print("Customer Details:")   
customer_1 = Customer("John Wick", "Continental-street")
customer_2 = Customer("Elon Musk", "Kingston-street")
print(customer_1)
print(customer_2)