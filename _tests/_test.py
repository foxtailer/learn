file = open("test.txt", 'a')
i = 5
while i != 0:
   file.write(str(i))
   i-=1

file.close()