import random
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk, ImageOps
import time
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ---------- FONTS ----------
TITLE_FONT = ("Inter", 18, "bold")
LABEL_FONT = ("Poppins", 11)
BUTTON_FONT = ("Inter", 12, "bold")
RESULT_FONT = ("Poppins", 12)
ENTRY_FONT = ("Poppins", 11)

# Custom dice image folder (CHANGE THIS IF NEEDED)
DICE_PATH = r"C:/Users/sujan/OneDrive/Desktop/python/"   # keep the r prefix

# ---------- THEME ----------
BG_MAIN = "#0E1A2A"
BLOCK_BG = "#162436"
BLOCK_SHADOW = "#0A141F"


def style_gui(root):
    root.configure(bg=BG_MAIN)
    style = ttk.Style()
    style.theme_use("clam")

    # Rounded button
    style.configure("Rounded.TButton",
                    background="#335C81",
                    foreground="white",
                    font=BUTTON_FONT,
                    padding=10,
                    relief="flat",
                    borderwidth=0)
    style.map("Rounded.TButton",
              background=[("active", "#44779F")])

    # Entry styling
    style.configure("Rounded.TEntry",
                    padding=6,
                    fieldbackground="#1E2E3E",
                    foreground="white",
                    relief="flat")

    style.configure("TLabel", background=BG_MAIN, foreground="#D9D9D9")


# ---------- DICE ANIMATION WITH SPIN ----------
def animate_roll():
    for _ in range(10):   # more frames → smoother
        face = random.randint(1, 6)
        img_path = f"{DICE_PATH}dice{face}.png"

        # Open original image
        base_img = Image.open(img_path).resize((120, 120))

        # SPIN EFFECT  → rotate the image randomly every frame
        angle = random.randint(-45, 45)
        spin_img = base_img.rotate(angle)

        # Convert to Tkinter image
        img = ImageTk.PhotoImage(spin_img)
        anim_label.config(image=img)
        anim_label.image = img

        anim_label.update()
        time.sleep(0.10)   # slower animation (more realistic)


# ---------- SMOOTH FADE-IN EFFECT ----------
def fade_in(widget, steps=10):
    for i in range(steps):
        widget.update()
        widget.tk.call(widget, "config", "-alpha", i / steps)
        time.sleep(0.02)


# ---------- SIMULATION ----------
def simulate():
    try:
        sample_space = int(entry.get())
        if sample_space <= 0:
            messagebox.showerror("Error", "Enter a positive number!")
            return
    except ValueError:
        messagebox.showerror("Error", "Invalid input!")
        return

    results = []

    animate_roll()

    for _ in range(sample_space):
        results.append(random.randint(1, 6))

    # Clear boxes
    for widget in results_container.winfo_children():
        widget.destroy()

    # Create boxes with animation
    for i in range(1, 7):
        root.after(i * 120, lambda i=i: create_result_box(i, results, sample_space))

    # Show graph after 1.5 sec
    root.after(1500, lambda: show_graph(results, sample_space))


# ---------- CREATE RESULT BOX ----------
def create_result_box(i, results, total):
    count = results.count(i)
    prob = count / total * 100

    box = tk.Frame(results_container, bg=BLOCK_BG, padx=12, pady=8)
    box.grid(row=(i - 1) % 3, column=0 if i <= 3 else 1, padx=10, pady=8)

    title = tk.Label(box, text=f"Face {i}", font=("Inter", 13, "bold"), fg="white", bg=BLOCK_BG)
    title.pack(anchor="center")

    tk.Label(box, text=f"Count: {count}/{total}", font=("Poppins", 11), fg="white",
             bg=BLOCK_BG).pack()

    tk.Label(box, text=f"Probability: {prob:.2f}%", font=("Poppins", 11),
             fg="white", bg=BLOCK_BG).pack()

    fade_in(box)


# ---------- GRAPH ----------
def show_graph(results, total):
    for widget in graph_frame.winfo_children():
        widget.destroy()

    if total > 1000:
        messagebox.showinfo("Info", "Graph only works for sample space ≤ 1000")
        return

    x_vals = list(range(1, total + 1))
    fig = plt.Figure(figsize=(5.3, 3.2), dpi=120, facecolor=BG_MAIN)
    ax = fig.add_subplot(111)

    ax.set_facecolor("#1E2E3E")
    colors = ["#F75C4C", "#E8D04D", "#54D36A", "#3D8BFF", "#FF7AF0", "#64F1F1"]

    for i in range(1, 7):
        prob_values = [results[:x].count(i) / x for x in x_vals]
        ax.plot(x_vals, prob_values, linewidth=1, color=colors[i - 1], label=f"Face {i}")

    ax.set_title("Probability vs Rolls", color="white")
    ax.set_xlabel("Roll Count", color="white")
    ax.set_ylabel("Probability", color="white")
    ax.grid(True, linestyle="--", alpha=0.4)
    ax.tick_params(colors="white")
    ax.legend(facecolor="#1E2E3E", edgecolor="white", labelcolor="white")

    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.get_tk_widget().pack()
    canvas.draw()


# ---------- GUI LAYOUT ----------
root = tk.Tk()
root.title("🎲Dice Roll Simulator")
root.geometry("800x820")
style_gui(root)

ttk.Label(root, text="🎲 Modern Dice Simulator", font=TITLE_FONT).pack(pady=15)

# ---------- MAIN HORIZONTAL CONTAINER ----------
main_block = tk.Frame(root, bg=BG_MAIN)
main_block.pack(pady=10)

# ---------- LEFT BLOCK ----------
left_shadow = tk.Frame(main_block, bg=BLOCK_SHADOW, padx=5, pady=5)
left_shadow.grid(row=0, column=0, padx=15)

left_block = tk.Frame(left_shadow, bg=BLOCK_BG, padx=25, pady=25)
left_block.pack()

# UPDATED label → bigger + bold
ttk.Label(left_block, text="Number of Rolls:", font=("Inter", 14, "bold")).pack(pady=(0, 5))

entry = ttk.Entry(left_block, width=12, font=ENTRY_FONT, style="Rounded.TEntry")
entry.pack(pady=(0, 15))

anim_label = ttk.Label(left_block)
anim_label.pack(pady=10)

run_btn = ttk.Button(left_block, text="Roll Dice!", command=simulate, style="Rounded.TButton")
run_btn.pack(pady=12)

# Hover animation
def on_enter(e): run_btn.configure(style="", background="#4B7DAC")
def on_leave(e): run_btn.configure(style="Rounded.TButton")

run_btn.bind("<Enter>", on_enter)
run_btn.bind("<Leave>", on_leave)

# ---------- RIGHT BLOCK ----------
right_shadow = tk.Frame(main_block, bg=BLOCK_SHADOW, padx=5, pady=5)
right_shadow.grid(row=0, column=1, padx=15)

right_block = tk.Frame(right_shadow, bg=BLOCK_BG, padx=25, pady=25)
right_block.pack()

ttk.Label(right_block, text="Results:", font=("Inter", 15, "bold")).pack(pady=(0, 10))

results_container = tk.Frame(right_block, bg=BLOCK_BG)
results_container.pack()

# ---------- GRAPH SECTION ----------
graph_frame = tk.Frame(root, bg=BG_MAIN)
graph_frame.pack(pady=10)

root.mainloop()

