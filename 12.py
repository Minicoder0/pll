import tkinter as tk
from tkinter import messagebox
import random

def play_game():
    if var.get() == 1:
        play_rps_game()
    elif var.get() == 2:
        play_number_guessing_game()

def play_rps_game():
    choices = ["rock", "paper", "scissor"]
    computer_choice = random.choice(choices)
    user_choice = user_entry.get().lower()

    result = ""

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissor") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissor" and computer_choice == "paper")
    ):
        result = "You win!"
    else:
        result = "Computer wins!"

    result_label.config(text=result)
    computer_choice_label.config(text=f"Computer chose: {computer_choice.capitalize()}")

def play_number_guessing_game():
    min_range = int(min_range_entry.get())
    max_range = int(max_range_entry.get())
    secret_number = random.randint(min_range, max_range)
    lives = 5

    def check_guess():
        nonlocal lives
        user_guess = int(guess_entry.get())
        if user_guess == secret_number:
            messagebox.showinfo("Congratulations", "You guessed the correct number!")
            game_window.destroy()
        else:
            lives -= 1
            lives_label.config(text=f"Lives: {lives}")
            if lives == 0:
                messagebox.showinfo("Game Over", f"You ran out of lives. The correct number was {secret_number}.")
                game_window.destroy()

    game_window = tk.Toplevel(root)
    game_window.title("Number Guessing Game")

    guess_label = tk.Label(game_window, text="Enter your guess:")
    guess_label.pack()

    guess_entry = tk.Entry(game_window)
    guess_entry.pack()

    submit_button = tk.Button(game_window, text="Submit Guess", command=check_guess)
    submit_button.pack()

    lives_label = tk.Label(game_window, text=f"Lives: {lives}")
    lives_label.pack()

# Create the main window
root = tk.Tk()
root.title("Game Selector")

# Create and place widgets
game_label = tk.Label(root, text="Choose a game:")
game_label.pack()

var = tk.IntVar()

rps_radio = tk.Radiobutton(root, text="Rock, Paper, Scissors", variable=var, value=1)
rps_radio.pack()

number_guessing_radio = tk.Radiobutton(root, text="Number Guessing Game", variable=var, value=2)
number_guessing_radio.pack()

play_button = tk.Button(root, text="Play", command=play_game)
play_button.pack()

user_entry = tk.Entry(root, width=20)
user_entry.pack()

result_label = tk.Label(root, text="")
result_label.pack()

computer_choice_label = tk.Label(root, text="")
computer_choice_label.pack()

min_range_label = tk.Label(root, text="Minimum Range:")
min_range_label.pack()

min_range_entry = tk.Entry(root)
min_range_entry.pack()

max_range_label = tk.Label(root, text="Maximum Range:")
max_range_label.pack()

max_range_entry = tk.Entry(root)
max_range_entry.pack()

# Start the GUI event loop
root.mainloop()
