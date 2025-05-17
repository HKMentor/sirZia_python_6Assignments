#  Assignment:
'''Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.'''

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"My name is {self.name} and my metriccls marks are {self.marks}.")


# Object create karte hain
s1 = Student("Hooria", 84)
s1.display()




















