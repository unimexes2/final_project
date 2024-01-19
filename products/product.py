from abc import ABC, abstractmethod

from .food_package import *

class Product(ABC):
    def __init__(self, id:str, name:str, price:float):
      self.id = id
      self.name = name
      self.price = price
    
    def describe(self):
        return f"Product - Type: {self.type()}, Name: {self.name}, Id: {self.id} , Price: {self.price} , {self.foodPackage().describe()}."   
    
    @abstractmethod
    def type(self) -> str:
        pass
    
    @abstractmethod
    def foodPackage(self) -> FoodPackage:
        pass  

class Hamburger(Product):
    def __init__(self, id:str, name:str, price:float):
        super().__init__(id, name, price)
        
    def type(self) -> str:
        return "Hamburguesa"
    
    def foodPackage(self) -> FoodPackage:
        return Wrapping()

class Soda(Product):
    def type(self) -> str:
        return "Soda"
    
    def foodPackage(self) -> FoodPackage:
        return Bottle()

class Drink(Product):
    def type(self) -> str:
        return "Bebida"
    
    def foodPackage(self) -> FoodPackage:
        return Glass()

class HappyMeal(Product):
    def type(self) -> str:
        return "Happy Meal"
    
    def foodPackage(self) -> FoodPackage:
        return Box()
