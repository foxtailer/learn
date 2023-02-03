import tkinter as tk
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.minsize(500, 400)
window.config(padx=10, pady=10, bg=YELLOW)

timer_lbl = tk.Label(text="Miles", font=("Arial", 14, "bold"))
timer_lbl.grid(column=2, row=0)

bg_img = tk.PhotoImage(file=r"E:\git\learn\tkinter\pomodoro\tomato.png")
canvas = tk.Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(105, 112, image=bg_img)
canvas.create_text(110, 130, text="00:00", fill="grey", font=("Arial", 24, "bold"))
canvas.grid()

start_btn = tk.Button(text="Start", command=calculate)
start_btn.grid(column=1, row=0)
reset_btn = tk.Button(text="Reset", command=calculate)
reset_btn.grid(column=1, row=2)

window.mainloop()