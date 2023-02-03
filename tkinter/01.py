import tkinter

window = tkinter.Tk()
window.minsize(500, 500)
window.title("My first GUI")
window.config(padx=10, pady=10)

counter = 0
def increse_count():
    global counter
    counter += 1
    my_lable["text"] = input.get() + str(counter)


my_lable = tkinter.Label(text=f"{counter}", font=("Arial", 24, "bold"))
my_lable.grid(column=0, row=0)

button = tkinter.Button(text="Click ne!", command=increse_count)
button.grid(column=2, row=0)

input = tkinter.Entry()
input.grid(column=3, row=0)



window.mainloop()