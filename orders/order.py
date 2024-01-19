

class Order:
    def __init__(self, cashier, customer):
        self.cashier = cashier
        self.customer = customer
        self.products = []

    def add(self, product):
        self.products.append(product)

    def calculateTotal(self):
        if None in self.products :
           print("The product list is empty")
           return
        else :
         total_amount = sum(product.price for product in self.products)
         return total_amount

    def show(self):
        
        
        
        
        print(f"Order details:")
        print(f"Cashier: {self.cashier.name}, Customer: {self.customer.name}")
        if None in self.products :
           print("........ending.")
           return
        
            
        print("Products:")
        for product in self.products:
            print(f"  - {product.name} ({product.type()}), Price: {product.price} euros")
        print(f"Total amount: {self.calculateTotal()} euros")
