from tkinter import *\

BG_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BG_COLOR)
window.minsize(300, 300)

bg_img = PhotoImage(file=r"C:\Users\yaroslav\Desktop\python\GIT\learn\100day_of_code\31\images\card_front.png")
canvas = Canvas(width=210, height=224, highlightthickness=0)
canvas.create_image(105, 112, image=bg_img)
canvas.grid(column=1, row=1)


window.mainloop()
