import threading

x = 0

def add():
    global x
    for _ in range(100000):
        x += 1

threads = [threading.Thread(target=add) for _ in range(2)]
for t in threads: t.start()
for t in threads: t.join()

print(x) 