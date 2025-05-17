'''18. Property Decorators: @property, @setter, and @deleter
Assignment 18:
Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.'''
class Product:
    def __init__ (self, price):
        self._price = price
        
    @property 
    def price(self):  # get
        return self._price   
    
    @price.setter
    def price(self, value):  # set
        self._price = value
        
    @price.deleter
    def price(self):   # delete
        del self._price    

# Use
p = Product(1000)

print(p.price)     # Output: 1000
p.price = 2000
print(p.price)     # Output: 2000
del p.price
