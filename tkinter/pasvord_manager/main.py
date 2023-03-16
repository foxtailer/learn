from tkinter import *
from tkinter import messagebox
import random
import pyperclip

def insert_field():
    y = generate()
    pass_entry.delete(0, END)
    pass_entry.insert(0, y)
    pyperclip.copy(y)

def generate():
    result = []
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    result += [random.choice(letters) for _ in range(random.randint(8, 10))]
    result += [random.choice(numbers) for _ in range(random.randint(2, 4))]
    result += [random.choice(symbols) for _ in range(random.randint(2, 4))]

    random.shuffle(result)
    return ''.join(result)

def save_data():
    website = website_name.get()
    email = mail_name.get()
    password = pass_entry.get()

    if website and password:
        its_ok = messagebox.askokcancel(title=website, message=f'Email: {email}\n\
            Pass: {password}')
        
        if its_ok:
            with open(r"C:\Users\User\Desktop\glovo\git\learn\tkinter\pasvord_manager\data.txt", "a") as data:
                data.write(f"{website} | {email} | {password}\n")
                website_name.delete(0, END)
                pass_entry.delete(0, END)
    else:
        messagebox.showerror(title='Error!', message='All fields must be full.')

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
generate_btn = Button(text="Generate", command=insert_field)
generate_btn.grid(column=2, row=3)

# Add
add_btn = Button(text="Add", width=30, command=save_data)
add_btn.grid(column=1, row=4, columnspan=2)



window.mainloop()