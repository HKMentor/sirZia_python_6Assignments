# guess_the_number_computer.py

import random

# Step 1: Generate a random number
secret_number = random.randint(1, 100)

# Step 2: Start guessing
guess = None  # Initially no guess

while guess != secret_number:
    guess = int(input("Guess the number (between 1 and 100): "))

    if guess < secret_number:
        print("Too low! Try again. 🔽")
    elif guess > secret_number:
        print("Too high! Try again. 🔼")
    else:
        print("Congratulations! 🎉 You guessed it right! ✅")
