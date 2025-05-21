import random  # To randomly select a word
import string  # To check for valid letters (a-z)

# Step 1: Create a function that chooses a word randomly
def get_valid_word(word_list):
    word = random.choice(word_list)  # Randomly pick a word
    while '-' in word or ' ' in word:
        word = random.choice(word_list)  # Avoid words with '-' or space
    return word.upper()  # Convert word to uppercase

# Step 2: Main function for the hangman game
def hangman():
    words = ['apple', 'banana', 'grapes', 'orange', 'mango']  # List of possible words
    word = get_valid_word(words)  # Pick a word
    word_letters = set(word)  # Letters in the word
    alphabet = set(string.ascii_uppercase)  # All capital letters A-Z
    used_letters = set()  # Letters the user has guessed

    lives = 6  # Total guesses allowed

    # Step 3: Run the game loop
    while len(word_letters) > 0 and lives > 0:
        # Show used letters
        print(f"You have {lives} lives left. Used letters: {' '.join(used_letters)}")

        # Display current word with underscores for unguessed letters
        word_display = [letter if letter in used_letters else '_' for letter in word]
        print("Current word: ", ' '.join(word_display))

        # Step 4: Get user's guess
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)  # Add guess to used letters
            if user_letter in word_letters:
                word_letters.remove(user_letter)  # Correct guess
                print("✅ Good guess!")
            else:
                lives -= 1  # Wrong guess, lose a life
                print("❌ Incorrect!")
        elif user_letter in used_letters:
            print("⚠️ You already guessed that letter.")
        else:
            print("❌ Invalid input. Please guess a letter A-Z.")

    # Step 5: Game over messages
    if lives == 0:
        print(f"\nYou lost! The word was: {word}")
    else:
        print(f"\n🎉 Congrats! You guessed the word: {word}")

# Step 6: Start the game
hangman()
