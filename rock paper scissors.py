import tkinter as tk
import random

# Game options
CHOICES = ["Rock", "Paper", "Scissors"]
EMOJI = {"Rock": "✊", "Paper": "📄", "Scissors": "✂️"}

# Scores & counters
user_score = 0
comp_score = 0
rounds = 0
MAX_ROUNDS = 5  # Best of 5


def play(user_choice):
    global user_score, comp_score, rounds

    if rounds >= MAX_ROUNDS:
        result_label.config(text="Game over! Press Reset to play again.")
        return

    comp_choice = random.choice(CHOICES)

    # Determine result
    if user_choice == comp_choice:
        result = "Tie!"
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
            (user_choice == "Paper" and comp_choice == "Rock") or \
            (user_choice == "Scissors" and comp_choice == "Paper"):
        result = "You Win!"
        user_score += 1
    else:
        result = "You Lose!"
        comp_score += 1

    rounds += 1

    # Update result display
    result_label.config(
        text=f"You: {EMOJI[user_choice]} {user_choice}\n"
             f"Computer: {EMOJI[comp_choice]} {comp_choice}\n\n{result}"
    )
    score_label.config(text=f"Your Score: {user_score}   Computer Score: {comp_score}")

    # When 5 rounds are complete
    if rounds == MAX_ROUNDS:
        if user_score > comp_score:
            final_msg = "🎉 YOU WON THE MATCH!"
        elif user_score < comp_score:
            final_msg = "😢 COMPUTER WON THE MATCH!"
        else:
            final_msg = "🤝 MATCH TIED!"
        result_label.config(text=result_label.cget("text") + f"\n\n{final_msg}")


def reset_game():
    global user_score, comp_score, rounds
    user_score = 0
    comp_score = 0
    rounds = 0
    score_label.config(text="Your Score: 0   Computer Score: 0")
    result_label.config(text="Choose your move")
    

# GUI setup
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("380x420")
root.config(bg="#E8F0FF")

# Title
title = tk.Label(root, text="Rock • Paper • Scissors",
                 font=("Arial", 20, "bold"), bg="#E8F0FF")
title.pack(pady=10)

# Score Label
score_label = tk.Label(root, text="Your Score: 0   Computer Score: 0",
                       font=("Arial", 13), bg="#E8F0FF")
score_label.pack(pady=5)

# Result Display
result_label = tk.Label(root, text="Choose your move",
                        font=("Arial", 13), width=35, height=5,
                        bg="white", relief="groove")
result_label.pack(pady=15)

# Buttons Frame
btn_frame = tk.Frame(root, bg="#E8F0FF")
btn_frame.pack(pady=10)

# Choice Buttons
for i, choice in enumerate(CHOICES):
    tk.Button(
        btn_frame,
        text=f"{EMOJI[choice]} {choice}",
        font=("Arial", 12),
        width=12,
        command=lambda c=choice: play(c),
        bg="#D9E6FF",
        relief="raised"
    ).grid(row=0, column=i, padx=8, pady=5)

# Reset Button
reset_btn = tk.Button(
    root,
    text="Reset Game",
    font=("Arial", 12, "bold"),
    width=12,
    bg="#F9C8C8",
    command=reset_game
)
reset_btn.pack(pady=15)

# Exit Button
exit_btn = tk.Button(root, text="Exit", font=("Arial", 11), width=10,
                     command=root.destroy, bg="#FFD39B")
exit_btn.pack()

root.mainloop()
