from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, dni:str, name:str, age:int):
        self.dni = dni
        self.name = name
        self.age = age

    @abstractmethod
    def describe(self):
        pass

class Cashier(User):

        def __init__(self, name, dni, age, timetable, salary):
            self.name = name
            self.dni = dni
            self.age = age
            self.timetable = timetable
            self.salary = salary
      
        def describe(self):
         return f"Cashier - Name: {self.name}, DNI: {self.dni} , Timetable: {self.timeTable}, Salary: {self.salary}."

class Customer(User):
    def __init__(self, name,dni,age,email,postalcode):
            self.name = name
            self.dni = dni
            self.age = age
            self.email = email
            self.postalcode = postalcode


    def describe(self):
        return f"Customer - Name: {self.name}, DNI: {self.dni} , Age: {self.age}, Email: {self.email}, Postal Code: {self.postalCode}"
