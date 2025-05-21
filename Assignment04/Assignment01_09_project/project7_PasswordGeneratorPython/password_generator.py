import random  # To generate random characters
import string  # To get letters, digits, and punctuation

# Step 1: Ask user how many passwords they want to generate
num_passwords = int(input("🔢 How many passwords do you want to generate? "))

# Step 2: Ask for password length
password_length = int(input("🔐 What should be the length of each password? "))

# Step 3: Create a set of characters to choose from
characters = string.ascii_letters + string.digits + string.punctuation

# Step 4: Loop through and generate passwords
for i in range(num_passwords):
    password = ''.join(random.choice(characters) for _ in range(password_length))
    print(f"🔒 Password {i+1}: {password}")
