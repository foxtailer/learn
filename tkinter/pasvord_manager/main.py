from tkinter import *

window = Tk()
window.config(padx=20, pady=20)
window.title("Pasvord manager")

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file=r"C:\Users\User\Desktop\glovo\git\learn\tkinter\pasvord_manager\logo.png")
canvas.create_image(200, 190, image=logo_img)
canvas.grid(column=0, row=0)



window.mainloop()