"""
Ejercicio 1: Sistema de comida rápida
 
Implementar un paquete llamado ‘products' que tiene dos módulos: ‘food_package.py' y ‘product.py', con la siguiente estructura:

products/
        __init__.py
        food_package.py
        product.py

El módulo food_package.py contendrá una clase abstracta denominada 'FoodPackage' con dos funciones abstractas: 'def pack(self)  -> str ' y 'def material(self) -> str '. Esta clase nos permite crear un tipo específico de paquete o envoltura dependiendo del tipo de alimento a empacar, por ejemplo:

Un vaso de soda puede ser empacado en un paquete tipo vaso y el material puede ser cartón. 
Una hamburguesa puede ser empacada en un paquete tipo envoltura de papel y el material puede ser aluminio.

En el mismo módulo se deberán incluir las implementaciones concretas para cada una de las siguientes clases ‘Wrapping’, ‘Bottle’, ‘Glass’ y ‘Box’, es decir, estas deben implementar los métodos anteriores y devolver un valor. Por ejemplo, la clase ‘Wrapping’ se puede definir como:

class Wrapping(FoodPackage):  
  def pack(self):
    return "Food Wrap Paper"
  def material(self):
    return "Aluminium" 

El módulo 'product.py’ contendrá una clase abstracta denominada 'Product' con dos funciones abstractas: 'def type(self) -> str' y 'def foodPackage(self)-> FoodPackage. Esta clase nos permita crear un producto específico y relacionarlo con su tipo de empaque por ejemplo:

Un producto con código de barras G1, es una soda Sprite cuyo precio es de 5 euros, pertenece al tipo Soda y puede ser empacado en un paquete tipo vaso y el material puede ser cartón. 
Un producto con código de barras H1, es una hamburguesa Bacon  cuyo precio es de 15 euros, pertenece al tipo Hamburger y puede ser empacado en un paquete un paquete tipo envoltura de papel y el material puede ser aluminio.

En el mismo módulo se deberán incluir las implementaciones concretas para cada una de las clases ‘Hamburger’, ‘Soda’, ‘Drink’ y ‘HappyMeal’, es decir, de forma parecida al módulo anterior, estas deben implementar los métodos anteriores y devolver un valor. Por ejemplo, la clase ‘Hamburger’, se puede definir como:

class Hamburger(Product):
    def __init__(self, id:str, name:str, price:float):
        super().__init__(id,name,price)
    def type(self) -> str:
        return "Hamburger"
    def foodPackage(self) -> FoodPackage:
        return Wrapping()
        
Implementar un paquete llamado ‘users' que tiene un módulo ‘user.py', con la siguiente estructura:

users/
        __init__.py
        user.py

El módulo 'user.py' contendrá una clase abstracta denominada ‘User’ que tiene un constructor por defecto para los siguientes datos 'def __init__(self, dni:str, name:str, age:int) ', con una función abstracta: 'def describe(self) '.

Luego en el mismo módulo se deberán incluir las implementaciones concretas para cada una de las clases ‘Cashier’ y ‘Customer’, es decir, estas deben implementar los métodos anteriores y devolver un valor. Adicionalmente, estas clases se diferencian por los parámetros que reciben sus constructores, por tanto, debemos hacer uso de herencia para inicializar el constructor de la clase padre y agregar características propias a cada clase.  

Implementar un paquete llamado 'util' que tiene dos módulos, denominados 'file_manager.py' y 'converter.py’, con la siguiente estructura:

util/
        __init__.py
        file_manager.py
        converter.py

El módulo ‘file_manager.py' contendrá una clase ‘CSVFileManager’ la cual es una implementaciòn libre y debe incluir las funciones:

La función 'def read(self)' lee un archivo en formato CSV y permite exportar su resultado como un Data Frame.
La función 'def write(self, dataFrame)' convierte un Data Frame en un archivo CSV. Esta es una función opcional, se deja al estudiante la implementación.

Los archivos en formato CSV se encuentran en la ruta “data/”, a continuación, se describe el contenido de cada archivo:

cashiers.csv: Información de los cajeros que harán uso del sistema.
customers.csv: Información de los clientes que harán uso del sistema.
drinks.csv: Información de los diferentes tipos de bebidas.
sodas.csv: Información de los diferentes tipos de gaseosas.
hamburgers.csv: Información de los diferentes tipos de hamburguesas.
happyMeal.csv: Información de los diferentes tipos de happy meals.

El módulo 'converter.py' contendrá una clase denominada ‘Converter’ con una función abstracta para convertir las filas de un Data Frame en instancias de objetos. La función sería ‘def convert(self, dataFrame, *args) -> list’. Adicionalmente esta clase debe incluir un método que permite imprimir la información de los objetos ‘def print(self, list)’. En el mismo módulo se deberán incluir las implementaciones específicas que permitan leer los archivos en formato CSV y convertir sus filas en objetos de cada clase utilizando los paquetes product y users.

Implementar un paquete llamado 'orders' que tiene un módulo 'order.py', con la siguiente estructura:

orders/
        __init__.py
        order.py

El módulo 'order.py' contendrá una clase denominada ‘Order’ con un constructor ‘def __init__(self, cashier:Cashier, customer:Customer):’, el cual permite inicializar la clase con los datos del cajero, del cliente y la lista de productos vacía por defecto. Además, debe incluir tres funciones para agregar productos, calcular el total de la orden solicitada y mostrar la información de la orden que está siendo procesada. Las funciones son ‘def add(self, product: Product)', ' def calculateTotal(self) -> float' y ‘def show(self)’, respectivamente.

Finalmente tendremos una clase principal que se llamará ‘PrepareOrder’ en la cual se deberá realizar una implementación que permita integrar los diferentes módulos empleados para leer los archivos en formato CSV y convertirlos en objetos. La implementación de esta clase es libre, es decir, no indicaremos las funciones que debe contener, pero la funcionalidad de la clase debe permitir crear una opción de menú que permita buscar los clientes, los cajeros y los productos para finalmente crear una orden. 

Se sugiere utilizar los métodos de entrada de teclado para leer los datos del dni cajero, cliente e id de los productos. 


A grandes rasgos, la aplicación seguiría los siguientes pasos:

1)	Leer archivos en formato csv: 
a.	Leer cada archivo en formato csv: Utilizar una instancia de la clase 'CSVFileManager' y llamar al método 'read()'.
2)	Convertir a listas de objetos:
a.	Convertir cajeros: Función creada por el alumno  
b.	Convertir clientes: Función creada por el alumno 
c.	Convertir productos: Función creada por el alumno 
3)	Preparar Orden:
a.	Buscar cajero por dni: Función creada por el alumno y debe devolver una instancia de tipo cajero.
b.	Buscar cliente por dni. Función creada por el alumno y debe devolver una instancia de tipo cliente.
c.	Inicializar Orden: Utilizar una instancia la clase 'Order', e inicializar con su constructor por defecto.
d.	Mostrar productos a vender: Función creada por el alumno.
e.	Escoger productos: Función creada por el alumno.
f.	Agregar productos: Utilizar la instancia la clase 'Order', del paso c y llamar al método 'add()'.
4)	Mostrar Orden: Utilizar la instancia la clase 'Order', del paso c y llamar al método 'show()'


"""

from util import *
from users import *
from products import *
from orders import *    
import os

def clear_display():
  os.system("cls")
  os.system("clear")

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
        return None

    def search_customer_by_dni(self, dni):
        for customer in self.customers:
            if str(customer.dni) == dni:
                return customer
        return None

    def show_available_products(self):
        clear_display()
        print("We have following categories of products: ")
        print("Hamburgers")
        print("Drinks")
        print("Sodas")
        print("Happy Meal")
           

    def choose_products(self):
     chosen_products = []

     hamburgers=self.hamburgers
     sodas=self.sodas
     meals=self.meals 
     drinks=self.drinks

    
     def find_product_by_id(products, product_id):
           for product in products:
             if product.id == product_id:
              return product
             return None 
    
    ## El corazón de mi app
     while True:
        product_type = input("Enter the type of the product (e.g., Hamburger, Soda, Drink, HappyMeal, or 'done' to finish): ")
        if product_type.lower() == 'done':
            return chosen_products
         
        
        if product_type.lower()=='hamburger':
              for hamburger in self.hamburgers:
               print(f"ID: {hamburger.id}, Name: {hamburger.name}, Price: {hamburger.price} euros")
              product_id = input("Enter the ID of the product you want to add: ").upper()
              index = find_product_by_id(hamburgers, product_id) 
              if index is None:
                      print("Wrong ID")
              else:
               chosen_products.append(index)  
      
        elif product_type.lower()=='happy meal':
              for meal in self.meals:
               print(f"ID: {meal.id}, Name: {meal.name}, Price: {meal.price} euros")
              product_id = input("Enter the ID of the product you want to add: ").upper()
              index = find_product_by_id(meals, product_id) 
              if index is None:
                      print("Wrong ID")
              else:
                chosen_products.append(index)  
        
        elif product_type.lower()=='soda':
              for soda in self.sodas:
               print(f"ID: {soda.id}, Name: {soda.name}, Price: {soda.price} euros") 
              product_id = input("Enter the ID of the product you want to add: ").upper()
              index = find_product_by_id(sodas, product_id) 
              if index is None:
                      print("Wrong ID")
              else:
               chosen_products.append(index)  
       
        
        elif product_type.lower()=='drink':
              for drink in self.drinks:
               print(f"ID: {drink.id}, Name: {drink.name}, Price: {drink.price} euros")
              product_id = input("Enter the ID of the product you want to add: ").upper()
              index = find_product_by_id(drinks, product_id) 
              if index is None:
                      print("Wrong ID")
              else:
               chosen_products.append(index)       
        clear_display()

    def run_order_creation(self):
      clear_display()
      while True : 
        dni_cashier = input("Enter the DNI of the cashier: ")
        cashier = self.search_cashier_by_dni(dni_cashier)
        if not cashier:
            print("Cashier not found.")
            
        else:  
         dni_customer = input("Enter the DNI of the customer: ")
         customer = self.search_customer_by_dni(dni_customer)
         if not customer:
            print("Customer not found.")
            
         if customer and cashier:
                break
      order = Order(cashier, customer)
      print(f"\nOrder created for cashier {cashier.name} and customer {customer.name}.\n")

      self.show_available_products()
      selected_products = self.choose_products()

      for product in selected_products:
            order.add(product)

      total_amount = order.calculateTotal()
      clear_display()
      order.show()