
from abc import ABC, abstractmethod
class FoodPackage (ABC): 
    @abstractmethod
    def pack(self)  -> str:
        pass
    
    @abstractmethod
    def material(self) -> str:
        pass
    
    def describe(self):
        return f"Empaque: {self.pack()}, Material: {self.material()}"    

class Wrapping(FoodPackage):  
    def pack(self):
        return "Envoltura de papel"
    
    def material(self):
        return "Aluminio"

class Bottle(FoodPackage):  
    def pack(self):
        return "Botella"
    
    def material(self):
        return "Vidrio"
      
class Glass(FoodPackage):  
    def pack(self):
        return "Vaso"
    
    def material(self):
        return "Cartón"

class Box(FoodPackage):  
    def pack(self):
        return "Caja"
    
    def material(self):
        return "Cartón"
