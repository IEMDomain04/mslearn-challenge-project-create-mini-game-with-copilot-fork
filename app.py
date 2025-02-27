import random
import tkinter as tk
from tkinter import messagebox

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def play_game(user_choice):
    global user_score, computer_score
    computer_choice = get_computer_choice()
    winner = determine_winner(user_choice, computer_choice)
    
    if winner == "user":
        user_score += 1
        result = "You win this round!"
    elif winner == "computer":
        computer_score += 1
        result = "Computer wins this round!"
    else:
        result = "It's a draw!"
    
    result_message = f"Computer chose: {computer_choice}\n{result}\n\nScore -> You: {user_score}, Computer: {computer_score}"
    messagebox.showinfo("Result", result_message)

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    messagebox.showinfo("Game Reset", "Scores have been reset!")

user_score = 0
computer_score = 0

# Set up the main application window
root = tk.Tk()
root.title("Rock Paper Scissors")

# Create buttons for user choices
rock_button = tk.Button(root, text="Rock", command=lambda: play_game("rock"))
rock_button.pack(side=tk.LEFT, padx=20, pady=20)

paper_button = tk.Button(root, text="Paper", command=lambda: play_game("paper"))
paper_button.pack(side=tk.LEFT, padx=20, pady=20)

scissors_button = tk.Button(root, text="Scissors", command=lambda: play_game("scissors"))
scissors_button.pack(side=tk.LEFT, padx=20, pady=20)

# Create a button to reset the game
reset_button = tk.Button(root, text="Reset Game", command=reset_game)
reset_button.pack(side=tk.LEFT, padx=20, pady=20)

# Start the GUI event loop
root.mainloop()