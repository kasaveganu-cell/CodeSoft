import random

choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0

def get_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "win"
    else:
        return "lose"

print("🎮 Welcome to Rock-Paper-Scissors Game!")
print("Rules: Rock > Scissors, Scissors > Paper, Paper > Rock")

while True:
    user_choice = input("\nEnter rock, paper, or scissors: ").lower()

    if user_choice not in choices:
        print("❌ Invalid choice! Try again.")
        continue

    computer_choice = random.choice(choices)

    print("👉 You:", user_choice)
    print("💻 Computer:", computer_choice)

    result = get_winner(user_choice, computer_choice)

    if result == "win":
        print("🎉 You win this round!")
        user_score += 1
    elif result == "lose":
        print("😢 Computer wins this round!")
        computer_score += 1
    else:
        print("🤝 It's a tie!")

    print(f"📊 Score → You: {user_score} | Computer: {computer_score}")

    play_again = input("Play again? (y/n): ").lower()
    if play_again != 'y':
        print("\n🏁 Final Score")
        print(f"You: {user_score} | Computer: {computer_score}")
        print("Thanks for playing!")
        break