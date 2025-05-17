# Assignment 8:
'''Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.

'''
class Person:
    
    def __init__(self, name):
        self.name = name
        
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name) 
        self.subject = subject
        
t = Teacher("Hooria  Khan" , "Python")
print(t.name, t.subject)               