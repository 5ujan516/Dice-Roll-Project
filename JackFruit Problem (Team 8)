# Number Guessing Game



import random
import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as tb


class GuessGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🎮 Number Guessing Game")

        # Allow resizing and start maximized
        self.root.state("zoomed")  # Windows
        # self.root.attributes("-zoomed", True)  # Linux/macOS

        # Apply modern theme
        style = tb.Style("superhero")

        self.secret_number = None
        self.count = 0
        self.max_range = 100
        self.high_score = None

        # ===== Main Layout Frame =====
        self.main_frame = tk.Frame(root, bg="#1c1c1c")
        self.main_frame.pack(fill="both", expand=True)

        # Title
        self.title_label = tk.Label(self.main_frame, text="🎲 Number Guessing Challenge 🎲",
                                    font=("Helvetica", 26, "bold"), fg="gold", bg="#1c1c1c")
        self.title_label.pack(pady=20)

        # Difficulty Selection
        difficulty_frame = tk.Frame(self.main_frame, bg="#1c1c1c")
        difficulty_frame.pack(pady=10)

        tk.Label(difficulty_frame, text="Select Difficulty:",
                 font=("Arial", 14, "bold"), fg="white", bg="#1c1c1c").pack(side=tk.LEFT, padx=5)

        self.difficulty = tb.Combobox(difficulty_frame,
                                      values=["Easy (1-50)", "Medium (1-100)", "Hard (1-500)"],
                                      state="readonly", width=18, bootstyle="info")
        self.difficulty.current(1)
        self.difficulty.pack(side=tk.LEFT, padx=5)

        start_button = tb.Button(difficulty_frame, text="🚀 Start Game",
                                 bootstyle="success", command=self.start_game)
        start_button.pack(side=tk.LEFT, padx=10)

        # Entry
        self.entry = tb.Entry(self.main_frame, font=("Arial", 18), justify="center",
                              state="disabled", width=18)
        self.entry.pack(pady=20)

        # Guess button
        self.guess_button = tb.Button(self.main_frame, text="🎯 Guess",
                                      bootstyle="primary", command=self.check_guess,
                                      state="disabled", width=20)
        self.guess_button.pack(pady=5)

        # Feedback
        self.feedback_label = tk.Label(self.main_frame, text="",
                                       font=("Arial", 18, "bold"), fg="white", bg="#1c1c1c")
        self.feedback_label.pack(pady=20)

        # Progress bar
        self.progress = tb.Progressbar(self.main_frame, mode="determinate",
                                       bootstyle="striped-info")
        self.progress.pack(fill="x", padx=50, pady=10)

        # Stats
        stats_frame = tk.Frame(self.main_frame, bg="#1c1c1c")
        stats_frame.pack(pady=10)

        self.tries_label = tk.Label(stats_frame, text="Tries: 0", font=("Arial", 14),
                                    fg="white", bg="#1c1c1c")
        self.tries_label.pack(side=tk.LEFT, padx=20)

        self.high_score_label = tk.Label(stats_frame, text="🏆 Best Score: None",
                                         font=("Arial", 14, "bold"), fg="gold", bg="#1c1c1c")
        self.high_score_label.pack(side=tk.LEFT, padx=20)

        # Reset button
        self.reset_button = tb.Button(self.main_frame, text="🔄 Restart Game",
                                      bootstyle="warning", state="disabled", width=20,
                                      command=self.reset_game)
        self.reset_button.pack(pady=20)

        # Footer / Status Bar
        self.footer = tk.Label(root, text="© 2025 Number Guessing Game | Built with ❤️ in Python",
                               font=("Arial", 10), fg="lightgray", bg="#1c1c1c")
        self.footer.pack(side="bottom", fill="x", pady=5)

    def start_game(self):
        difficulty = self.difficulty.get()
        if "Easy" in difficulty:
            self.max_range = 50
        elif "Medium" in difficulty:
            self.max_range = 100
        else:
            self.max_range = 500

        self.secret_number = random.randint(1, self.max_range)
        self.count = 0
        self.entry.config(state="normal")
        self.guess_button.config(state="normal")
        self.reset_button.config(state="normal")
        self.feedback_label.config(
            text=f"✨ Game started! Guess between 1 and {self.max_range}", fg="lightblue")
        self.tries_label.config(text="Tries: 0")
        self.progress["value"] = 0

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.count += 1

            if guess < 1 or guess > self.max_range:
                self.feedback_label.config(
                    text=f"⚠️ Enter a number between 1 and {self.max_range}", fg="orange")
                return

            if guess > self.secret_number:
                self.feedback_label.config(text="🔽 Too high! Try lower.", fg="red")
            elif guess < self.secret_number:
                self.feedback_label.config(text="🔼 Too low! Try higher.", fg="cyan")
            else:
                self.feedback_label.config(
                    text=f"🎉 Correct! The number was {self.secret_number}", fg="lime")
                self.guess_button.config(state="disabled")

                # Animate progress bar full
                for i in range(101):
                    self.root.after(i * 5, lambda v=i: self.progress.config(value=v))

                # Update high score
                if self.high_score is None or self.count < self.high_score:
                    self.high_score = self.count
                    self.high_score_label.config(
                        text=f"🏆 Best Score: {self.high_score} tries")
                    messagebox.showinfo("🎉 New High Score!",
                                        f"You set a new best score in {self.count} tries!")

            # Update stats
            self.tries_label.config(text=f"Tries: {self.count}")

            # Progress bar closeness
            closeness = max(
                0, 100 - (abs(self.secret_number - guess) * 100 / self.max_range))
            self.progress["value"] = closeness

            self.entry.delete(0, tk.END)

        except ValueError:
            self.feedback_label.config(text="❌ Please enter a valid number!", fg="orange")

    def reset_game(self):
        self.secret_number = random.randint(1, self.max_range)
        self.count = 0
        self.entry.config(state="normal")
        self.guess_button.config(state="normal")
        self.feedback_label.config(
            text=f"🔄 New game started! Range 1-{self.max_range}", fg="lightyellow")
        self.tries_label.config(text="Tries: 0")
        self.progress["value"] = 0
        self.entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tb.Window(themename="superhero")
    game = GuessGame(root)
    root.mainloop()
#-----------------------------------------------------------------------------------------------------------------



# Rock Paper Scissors


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
#----------------------------------------------------------------------------------------------------------------



# Dice Roll Simulation with stats



import random
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk, ImageFilter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ---------- FONTS ----------
TITLE_FONT = ("Inter", 18, "bold")
LABEL_FONT = ("Poppins", 11)
BUTTON_FONT = ("Inter", 12, "bold")
RESULT_FONT = ("Poppins", 12)
ENTRY_FONT = ("Poppins", 11)

# Custom dice image folder
DICE_PATH = r"C:/Users/sujan/OneDrive/Desktop/python/"

# ---------- THEME ----------
BG_MAIN = "#0E1A2A"
BLOCK_BG = "#162436"
BLOCK_SHADOW = "#0A141F"


def style_gui(root):
    root.configure(bg=BG_MAIN)
    style = ttk.Style()
    style.theme_use("clam")

    # Styled rounded button
    style.configure("Rounded.TButton", background="#335C81", foreground="white", 
                    font=BUTTON_FONT, padding=10, relief="flat", borderwidth=0)

    style.map("Rounded.TButton", background=[("active", "#44779F")])

    style.configure("TLabel", background=BG_MAIN, foreground="#D9D9D9")

    style.configure("Rounded.TEntry", padding=6, fieldbackground="#1E2E3E",
                    foreground="white", relief="flat")


# ---------- FADE-IN ----------
def fade_in(widget, steps=12):
    r, g, b = (22, 36, 54)

    for i in range(steps):
        factor = i / steps
        new_r = int(r + (255 - r) * factor * 0.15)
        new_g = int(g + (255 - g) * factor * 0.15)
        new_b = int(b + (255 - b) * factor * 0.15)

        color = f"#{new_r:02x}{new_g:02x}{new_b:02x}"
        widget.config(bg=color)
        widget.update()


# ---------- ANIMATION ----------
def animate_roll(callback):
    frames = 12

    def update_frame(n):
        if n >= frames:
            callback()
            return

        face = random.randint(1, 6)
        img_path = f"{DICE_PATH}dice{face}.png"
        base_img = Image.open(img_path).resize((120, 120))

        angle = random.randint(-180, 180)
        spin_img = base_img.rotate(angle, expand=True).filter(
            ImageFilter.GaussianBlur(1.2)
        )

        img = ImageTk.PhotoImage(spin_img)
        anim_label.config(image=img)
        anim_label.image = img

        root.after(70, lambda: update_frame(n + 1))

    update_frame(0)


# ---------- MAIN SIMULATION ----------
def simulate():
    try:
        sample_space = int(entry.get())
        if sample_space <= 0:
            messagebox.showerror("Error", "Enter a positive number!")
            return
    except ValueError:
        messagebox.showerror("Error", "Invalid input!")
        return

    animate_roll(lambda: compute_results(sample_space))


def compute_results(sample_space):
    results = [random.randint(1, 6) for _ in range(sample_space)]

    for widget in results_container.winfo_children():
        widget.destroy()

    for i in range(1, 7):
        root.after(i * 240, lambda i=i: create_result_box(i, results, sample_space))

    root.after(2500, lambda: show_graph(results, sample_space))


# ---------- RESULT BOX ----------
def create_result_box(i, results, total):
    count = results.count(i)
    prob = count / total * 100

    box = tk.Frame(results_container, bg=BLOCK_BG, padx=12, pady=8)
    box.grid(row=(i - 1) % 3, column=0 if i <= 3 else 1, padx=10, pady=8)

    tk.Label(box, text=f"Face {i}",
             font=("Inter", 13, "bold"),
             fg="white", bg=BLOCK_BG,
             bd=0).pack()

    tk.Label(box, text=f"Count: {count}/{total}",
             fg="white", bg=BLOCK_BG,
             bd=0).pack()

    tk.Label(box, text=f"Probability: {prob:.2f}%",
             fg="white", bg=BLOCK_BG,
             bd=0).pack()

    fade_in(box)


# ---------- GRAPH ----------
def show_graph(results, total):
    for w in graph_frame.winfo_children():
        w.destroy()

    if total > 1000:
        messagebox.showinfo("Info", "Graph only works for sample space ≤ 1000")
        return

    x_vals = list(range(1, total + 1))

    fig = plt.Figure(figsize=(5.3, 3.2), dpi=120, facecolor=BG_MAIN)
    ax = fig.add_subplot(111)
    ax.set_facecolor("#1E2E3E")

    colors = ["#F75C4C", "#E8D04D", "#54D36A", "#3D8BFF", "#FF7AF0", "#64F1F1"]

    for i in range(1, 7):
        y_vals = [results[:x].count(i) / x for x in x_vals]
        ax.plot(x_vals, y_vals, linewidth=1, color=colors[i - 1], label=f"Face {i}")

    ax.set_title("Probability vs Rolls", color="white")
    ax.set_xlabel("Roll Count", color="white")
    ax.set_ylabel("Probability", color="white")
    ax.grid(True, linestyle="--", alpha=0.4)
    ax.tick_params(colors="white")
    ax.legend(facecolor="#1E2E3E", labelcolor="white")

    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.get_tk_widget().pack()
    canvas.draw()


# ---------- GUI ----------
root = tk.Tk()
root.title("🎲 Dice Roll Simulator")
root.geometry("800x820")
style_gui(root)

tk.Label(root, text="🎲 Modern Dice Simulator",
         font=TITLE_FONT, fg="white", bg=BG_MAIN,
         bd=0, highlightthickness=0).pack(pady=15)

main_block = tk.Frame(root, bg=BG_MAIN)
main_block.pack(pady=10)

# LEFT BLOCK
left_shadow = tk.Frame(main_block, bg=BLOCK_BG, padx=5, pady=5)
left_shadow.grid(row=0, column=0, padx=15)

left_block = tk.Frame(left_shadow, bg=BLOCK_BG, padx=25, pady=25)
left_block.pack()

tk.Label(left_block, text="Number of Rolls:",
         font=("Inter", 14, "bold"),
         fg="white", bg=BLOCK_BG,
         bd=0, highlightthickness=0).pack()

entry = ttk.Entry(left_block, width=12, font=ENTRY_FONT, style="Rounded.TEntry")
entry.pack(pady=(10, 15))

# Dice animation uses ttk label (no highlight issue)
anim_label = ttk.Label(left_block)
anim_label.pack(pady=10)

run_btn = ttk.Button(left_block, text="Roll Dice!",
                     style="Rounded.TButton", command=simulate)
run_btn.pack(pady=12)

# RIGHT BLOCK
right_shadow = tk.Frame(main_block, bg=BLOCK_BG, padx=5, pady=5)
right_shadow.grid(row=0, column=1, padx=15)

right_block = tk.Frame(right_shadow, bg=BLOCK_BG, padx=25, pady=25)
right_block.pack()

tk.Label(right_block, text="Results:",
         font=("Inter", 15, "bold"),
         fg="white", bg=BLOCK_BG,
         bd=0, highlightthickness=0).pack()

results_container = tk.Frame(right_block, bg=BLOCK_BG)
results_container.pack()

# GRAPH
graph_frame = tk.Frame(root, bg=BG_MAIN)
graph_frame.pack(pady=10)

root.mainloop()




#--------------------------------------------------------------------------------------------------------------------
