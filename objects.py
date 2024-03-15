from dataclasses import dataclass
#a class with three attributes and two methods 
@dataclass                      #dataclass decorator
class Product:
    name:str
    price:float
    discountPercent:int 
    #a method that uses two attributes to perform a calculation 
    def getdiscountAmount(self):
        return self.price * self.discountPercent/100
    
    #a method that calls another method to perform a calculation
    def getdiscountPrice(self):
        return self.price - self.getdiscountAmount()