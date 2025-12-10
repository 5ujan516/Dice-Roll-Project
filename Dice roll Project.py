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
