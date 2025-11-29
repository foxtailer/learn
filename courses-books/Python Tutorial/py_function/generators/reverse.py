def reverse(data):
    for i in range(len(data)-1, -1, -1):
        yield data[i]

print(dir(reverse("gg")))
        
for char in reverse("golf"):
    print(char)

print()
reverse_generator = reverse("golf")
while True:
    try:
        print(next(reverse_generator))
    except:
        break

# Generator expression
print(list(('golf'[i] for i in range(len('golf')-1, -1, -1))))