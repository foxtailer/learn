txt = ['lambda functions are anonymous functions.',
 'anonymous functions dont have a name.',
 'functions are objects in Python.']

mark = map(lambda x:(True, x) if "anonymous" in x else (False, x), txt)

print(list(mark))