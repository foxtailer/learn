import random

names = ["Alex", "Inna", "Mari", "Brendon", "Zoy"]

students_score = {name : random.randint(50, 100) for name in names}

passed_student = {key:value for (key , value) in students_score.items() if value > 60}

print(passed_student)

# Task: create dict where key is word from sentence and value is len of this word
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word : len(word) for word in sentence.split()}
print(result)

