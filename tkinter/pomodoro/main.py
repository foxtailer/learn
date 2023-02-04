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

def tryy():
    pass

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer(minutes):
    countdown(minutes)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(minutes):
    a = minutes // 10
    b = minutes % 10
    c = 5
    d = 9
    canvas.itemconfig(timer_text, text = f"{a}{b} : {c}{d}")
# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.minsize(300, 300)
window.config(padx=10, pady=10, bg=YELLOW)


timer_lbl = tk.Label(text="Time", font=("Arial", 14, "bold"), fg=GREEN)
timer_lbl.grid(column=1, row=0)


bg_img = tk.PhotoImage(file=r"E:\git\learn\tkinter\pomodoro\tomato.png")
canvas = tk.Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(105, 112, image=bg_img)
timer_text = canvas.create_text(110, 130, text="00:00", fill="grey", font=("Arial", 24, "bold"))
canvas.grid(column=1, row=1)


start_btn = tk.Button(text="Start", command=start_timer(15), highlightthickness=0)
start_btn.grid(column=0, row=2)

reset_btn = tk.Button(text="Reset", command=tryy, highlightthickness=0)
reset_btn.grid(column=2, row=2)


pomodoros_lbl = tk.Label(text="*", font=("Arial", 14, "bold"))
pomodoros_lbl.grid(column=1,row=3)

window.mainloop()