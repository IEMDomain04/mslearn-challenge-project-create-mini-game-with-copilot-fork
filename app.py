import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_user_choice():
    choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please try again.")
        choice = input("Enter your choice (rock, paper, scissors): ").lower()
    return choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)
        if winner == "user":
            user_score += 1
            print("You win this round!")
        elif winner == "computer":
            computer_score += 1
            print("Computer wins this round!")
        else:
            print("It's a draw!")

        print(f"Score -> You: {user_score}, Computer: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("Final Score:")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")

if __name__ == "__main__":
    play_game()