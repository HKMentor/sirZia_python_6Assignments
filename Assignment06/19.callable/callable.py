'''19. callable() and __call__()
Assignment:
Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function.'''

class Multiplier:
    def __init__(self, factor):
        self.factor = factor   # store the factor

    def __call__(self, number):
        return self.factor * number  # multiply and return

# Create object
m = Multiplier(5)

# Test with callable()
print(callable(m))  

# Call object like a function
print(m(10))        
print(m(3))        

