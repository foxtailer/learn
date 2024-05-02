from tkinter import *
import requests

def get_quote():
    endpoint = "https://api.kanye.rest"
    quote = eval(requests.get(url=endpoint).text)["quote"]
    canvas.itemconfig(quote_text, text=quote)
    return quote
    

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file=r"C:\Users\yaroslav\Desktop\python\GIT\learn\100day_of_code\33\005 kanye-quotes-start\background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file=r"C:\Users\yaroslav\Desktop\python\GIT\learn\100day_of_code\33\005 kanye-quotes-start\kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()