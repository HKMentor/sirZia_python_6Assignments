'''20. Creating a Custom Exception
Assignment:
Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.

'''

# Step 1: Custom Exception
class InvalidAgeError(Exception):
    pass  # we don’t need to change anything, just create a named error

# Step 2: Function to check age
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older.")
    else:
        print("Access granted.")

# Step 3: Try-Except to handle it
try:
    check_age(16)  # try with age less than 18
except InvalidAgeError as e:
    print("InvalidAgeError caught:", e)
