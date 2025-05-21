import random

def play():
    user = input("Choose 'rock', 'paper', or 'scissors': ").lower()
    computer = random.choice(['rock', 'paper', 'scissors'])

    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}\n")

    if user == computer:
        return "It's a tie! 🤝"

    # Win conditions for the user
    if (user == "rock" and computer == "scissors") or \
       (user == "scissors" and computer == "paper") or \
       (user == "paper" and computer == "rock"):
        return "You win! 🎉"
    
    return "You lose! 😢"

# Run the game
print(play())
