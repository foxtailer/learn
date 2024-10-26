top = 0
prev_top = 0

while True:
    number = int(input('number: '))
    if not number:
        break

    if number > top:
        prev_top = top
        top = number
        continue
    
    if number > prev_top:
        prev_top = number

print(prev_top)
