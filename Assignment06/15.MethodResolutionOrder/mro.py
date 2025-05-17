# Assignment 15:
'''Create four classes: Method Resolution Order (MRO) and Diamond Inheritance


A with a method show(),

B and C that inherit from A and override show(),

D that inherits from both B and C.

Create an object of D and call show() to observe MRO.'''

class A:
    def show(sellf):
        print("A")
        
class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print(C)

class D(B,C):
    pass

d = D()

print(d.show()) 
                       

