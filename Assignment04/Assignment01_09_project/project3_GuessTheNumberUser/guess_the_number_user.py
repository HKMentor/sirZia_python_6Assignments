import random

print("Think of a number between 1 and 100, and I will try to guess it!")

low = 1
high = 100
feedback = ''

while feedback != 'c':
    if low != high:
        guess = random.randint(low, high)
    else:
        guess = low  # or high, both are same here

    print(f"My guess is: {guess}")
    feedback = input("Is it (H)igh, (L)ow, or (C)orrect? ").lower()

    if feedback == 'h':
        high = guess - 1
    elif feedback == 'l':
        low = guess + 1

print(f"Yay! 🎉 I guessed your number {guess} correctly!")
