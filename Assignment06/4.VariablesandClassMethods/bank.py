# Assignment 4:
'''Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.'''


class Bank:
    bank_name = "State Bank Of Pakistan"
    
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
        
b1 = Bank()

print(f"Old Bank Name: {b1.bank_name}")
b1.change_bank_name("Bank Al-Habib")
print(f"New Bank Name : {b1.bank_name}")
        
        














