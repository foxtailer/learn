from tkinter import *


def save_data():
    website = website_name.get()
    email = mail_name.get()
    password = pass_entry.get()
    with open(r"C:\Users\User\Desktop\glovo\git\learn\tkinter\pasvord_manager\data.txt", "a") as data:
        data.write(f"{website} | {email} | {password}\n")


window = Tk()
window.config(padx=20, pady=20)
window.title("Pasvord manager")

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file=r"C:\Users\User\Desktop\glovo\git\learn\tkinter\pasvord_manager\logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


# Website 
website_lbl = Label(text="Website name:")
website_lbl.grid(column=0, row=1)
website_name = Entry(width=35)
website_name.focus()
website_name.grid(column=1, row=1, columnspan=2)

# Email
mail_lbl = Label(text="Email/Username:")
mail_lbl.grid(column=0, row=2)
mail_name = Entry(width=35)
mail_name.insert(0, "yaroslav@gmail.com")
mail_name.grid(column=1, row=2, columnspan=2)

# Pasword
pass_lbl = Label(text="Password:")
pass_lbl.grid(column=0, row=3)
pass_entry = Entry(width=25,)
pass_entry.grid(column=1, row=3)
generate_btn = Button(text="Generate")
generate_btn.grid(column=2, row=3)

# Add
add_btn = Button(text="Add", width=30, command=save_data)
add_btn.grid(column=1, row=4, columnspan=2)



window.mainloop()