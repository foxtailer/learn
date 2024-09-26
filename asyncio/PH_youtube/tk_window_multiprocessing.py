from tkinter import ttk
import tkinter as tk
import time
import multiprocessing

root = tk.Tk()
root.geometry('300x300+150+150')

def sleep_func(queue):
    time.sleep(10)
    #lab['text'] = 'After sleep.'
    queue.put('After sleep.') 


def run_multiprocessing_task():
    queue = multiprocessing.Queue()  # Create a queue for communication
    process = multiprocessing.Process(target=sleep_func, args=(queue,))
    process.start()

    root.after(100, check_queue, queue)

def check_queue(queue):
    try:
        # Check if there is a message in the queue
        message = queue.get_nowait()  # Non-blocking get
        lab['text'] = message  # Update the label text
    except:
        pass  # Ignore the exception if the queue is empty

    # Schedule the next check
    root.after(100, check_queue, queue)

button = ttk.Button(root, text='Run', command=run_multiprocessing_task)
button.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

lab = ttk.Label(root, text='Before start.')
lab.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

root.mainloop()
