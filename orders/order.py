from users import *
from products import *

class Order:
    def __init__(self, cashier: Cashier, customer: Customer):
        self.cashier = cashier
        self.customer = customer
        self.products = []

    def add(self, product: Product):
        self.products.append(product)
        print(f"Product '{product.name}' added to the order.")

    def calculateTotal(self) -> float:
        total_price = sum(product.get_price() for product in self.products)
        return total_price

    def show(self):
        print("Hello: " + self.customer.describe())
        print("Was attended by: " + self.cashier.describe())
        print("Order Details:")
        for i, product in enumerate(self.products, 1):
            print(f"{i}. {product.describe()} - Price: {product.get_price()} euros")
        print(f"Total price: {self.calculateTotal()} euros")
