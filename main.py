from util import *
from users import *
from products import *
from orders import *     
        
     





class PrepareOrder:
    def __init__(self):
        self.converter = Converter()
        self.cashiers = self.read_cashiers_from_csv("data/cashiers.csv")
        self.customers = self.read_customers_from_csv("data/customers.csv")
        self.hamburgers = self.read_hamburgers_from_csv("data/hamburgers.csv")
        self.drinks = self.read_drinks_from_csv("data/drinks.csv")
        self.sodas = self.read_sodas_from_csv("data/sodas.csv")
        self.meals = self.read_meals_from_csv("data/happyMeal.csv")
    
    def read_cashiers_from_csv(self, csv_path):
        cashiers_data = CSVFileManager(csv_path).read()
        if cashiers_data is not None:
        
         return self.converter.convert_csv_cachier(cashiers_data,Cashier)
        else:
            return []


    def read_customers_from_csv(self, csv_path):
        customers_data = CSVFileManager(csv_path).read()
        if customers_data is not None:
            
            return self.converter.convert_csv_user(customers_data,Customer)
        else:
            return []

    def read_hamburgers_from_csv(self, csv_path):
        hamburgers_data = CSVFileManager(csv_path).read()
        if hamburgers_data is not None:
         
           return self.converter.convert_csv_product(hamburgers_data,Hamburger)
        else:
            return []



    def read_drinks_from_csv(self, csv_path):
        drinks_data = CSVFileManager(csv_path).read()
        if drinks_data is not None:
        
           return self.converter.convert_csv_product(drinks_data,Drink)
        else:
            return []
        
    def read_sodas_from_csv(self, csv_path):
        sodas_data = CSVFileManager(csv_path).read()
        if sodas_data is not None:
      
           return self.converter.convert_csv_product(sodas_data,Soda)
        else:
            return []

    def read_meals_from_csv(self, csv_path):
        meals_data = CSVFileManager(csv_path).read()
        if meals_data is not None:
       
           return self.converter.convert_csv_product(meals_data,HappyMeal)
        else:
            return []


    def search_cashier_by_dni(self, dni):

        for cashier in self.cashiers:
            m= cashier.dni
            if str(cashier.dni) == dni:
                return cashier
        print("Cashier not found.")
        return None

    def search_customer_by_dni(self, dni):
        for customer in self.customers:
            if str(customer.dni) == dni:
                return customer
        return None

    def show_available_products(self):
        print("We have following categories of products: ")
        print("Hamburgers")
        print("Drinks")
        print("Sodas")
        print("Happy Meal")
           

    def choose_products(self):
     chosen_products = []
     
     product_class_mapping = {
        'Hamburger': Hamburger,
        'Soda': Soda,
        'Drink': Drink,
        'HappyMeal': HappyMeal
    }
     hamburgers=self.hamburgers
     sodas=self.sodas
     meals=self.meals 
     drinks=self.drinks

    
     def find_product_by_id(products, product_id):
           for product in products:
             if product.id == product_id:
              return product
             return None 
    
    
     while True:
        product_type = input("Enter the type of the product (e.g., Hamburger, Soda, Drink, HappyMeal, or 'done' to finish): ")
        if product_type.lower() == 'done':
            return chosen_products
         
        
        if product_type.lower()=='hamburger':
              for hamburger in self.hamburgers:
               print(f"ID: {hamburger.id}, Name: {hamburger.name}, Price: {hamburger.price} euros")
              product_id = input("Enter the ID of the product you want to add: ")
              index = find_product_by_id(hamburgers, product_id) 
              chosen_products.append(index)  
      
        elif product_type.lower()=='happy meal':
              for meal in self.meals:
               print(f"ID: {meal.id}, Name: {meal.name}, Price: {meal.price} euros")
              product_id = input("Enter the ID of the product you want to add: ")
              index = find_product_by_id(meals, product_id) 
              chosen_products.append(index)  
        
        elif product_type.lower()=='sodas':
              for soda in self.sodas:
               print(f"ID: {soda.id}, Name: {soda.name}, Price: {soda.price} euros") 
              product_id = input("Enter the ID of the product you want to add: ")
              index = find_product_by_id(sodas, product_id) 
              chosen_products.append(index)  
       
        
        elif product_type.lower()=='drinks':
              for drink in self.drinks:
               print(f"ID: {drink.id}, Name: {drink.name}, Price: {drink.price} euros")
              product_id = input("Enter the ID of the product you want to add: ")
              index = find_product_by_id(drinks, product_id) 
              chosen_products.append(index)       
   

    def run_order_creation(self):
        dni_cashier = input("Enter the DNI of the cashier: ")
        cashier = self.search_cashier_by_dni(dni_cashier)
        if not cashier:
            print("Cashier not found.")
            return

        dni_customer = input("Enter the DNI of the customer: ")
        customer = self.search_customer_by_dni(dni_customer)
        if not customer:
            print("Customer not found.")
            return

        order = Order(cashier, customer)
        print(f"\nOrder created for cashier {cashier.name} and customer {customer.name}.\n")

        self.show_available_products()
        selected_products = self.choose_products()

        for product in selected_products:
            order.add(product)

        total_amount = order.calculateTotal()
        print(f"\nTotal amount for the order: {total_amount} euros")


        order.show()



if __name__ == "__main__":
    order_manager = PrepareOrder()
    order_manager.run_order_creation()
