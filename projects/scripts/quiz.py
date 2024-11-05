import random


ESCAPE_COMMANDS = ['q']

TEST = {"Who serves as the speaker of the prologue in Shakespeare's Romeo and Juliet?": "Chorus",
        "What was the cause of death for Freddie Mercury?": "Pneumonia",
        "Which of the following is a major muscle of the back?": "Trapezius",
        "Who played the female lead in the 1933 film 'King Kong'": "Fay Wray",
        "Which of the following was not one of 'The Magnificent Seven'": "Clint Eastwood",
        "Which of the following authors was not born in England?": "Arthur Conan Doyle"}

questions = {}


def read_new(n: int =10):
    """
    Read n questions from user input and save in to questions dict.

    n - number of questions that user should write.
    """
    print()

    global questions
    msg = '''Write new questions in format:
            question; answer
            ";" simbol inside question or answer not required.'''
    
    print('\n'.join(line.lstrip() for line in msg.splitlines()))

    while len(questions) < n:
        question = input('n: ').strip()
        if not question:
            print('Must bee a string.')
            continue
        elif question in ESCAPE_COMMANDS:
            break
        elif question.count(';') > 1 or ';' not in question or not question.split(';')[1]:
            print('Wrong format.')
            continue
        else:
            questions.update(([i.strip() for i in question.split(';')],))


def get_answers(question: tuple, questions: list) -> str:
    """
    Create a string of 4 answers, one of which is true and the others are false.

    question - (question, answer)
    questions - [(question, answer), (question, answer), (question, answer)]
    """
    fake_answers = [i[1] for i in questions if i[1] != question[1]][:4]
    answers = fake_answers[:4]
    answers.append(question[1])
    random.shuffle(answers)

    return ', '.join(answers)


def quiz(name, quiz_data: dict, questions: dict):
    """
    Take answers from user and save rating to dict
    """
    questions = list(questions.items())
    random.shuffle(questions)
    counter = 0

    for i in range(len(questions)):
        question = questions[i]
        print(question[0])
        print(answers:= get_answers(question, questions))

        while True:
            answer = input(f'({name.capitalize()}): ').strip()

            if answer and answer == question[1]:
                counter += 1
                percent = (counter/len(questions))*100
                print(f'Question {i+1}: Correct. {counter}/{len(questions)} ({round(percent, 2)}%)')
                break
            elif answer and answer != questions[1] and answer in answers.split(', '):
                percent = (counter/len(questions))*100
                print(f'Question {i+1}: Wrong. Answer is: {question[1]}. {counter}/{len(questions)} ({round(percent, 2)}%)')
                break
            else:
                # If the user accidentally enters an empty string, the program should give them a chance to correct their answer.
                print('Answer not in list or empty.')
                continue
    
    print(f'{name.capitalize()}: {counter}/{len(questions)}.\n')
    
    quiz_data.update(((name, counter),))


def start_quiz(questions):
    """
    Call quiz for each user and print results
    """
    users_and_score = {}

    while True:
        print('"q" to exite.')
        name = input('Your name: ').strip()
        if name in ESCAPE_COMMANDS:
            break
        elif name in users_and_score:
            print(f'{name.capitalize()} alredy pass the quiz.')
            continue

        quiz(name, users_and_score, questions)

    results = sorted(list(users_and_score.items()), key=lambda x: x[1], reverse=True)
    percentages_list = []

    for name, result in results:
        percent = (result/len(questions))*100
        percentages_list.append(percent)
        print(f'{name.capitalize()}: {result}/{len(questions)} ({round(percent, 2)}%)')
    
    print(f'Average score: {int(sum(users_and_score.values())/len(users_and_score))}/{len(questions)}\
({round(sum(percentages_list)/len(users_and_score), 2)}%)')


print('Quize')
print('"read" for writing new questions. ')
print('"start" for starting quiz.')

# Program main loop
while True:
    print()
    command = input('Q: ').strip()
    
    if command in ESCAPE_COMMANDS:
        break
    elif command == 'read':
        read_new()
    elif 'read' in command and len(command.split()) == 2:
        command = command.split()
        if command[1].isdigit():
            read_new(int(command[1]))
        else:
            print('read arrument should be a number.')
    elif command == 'start':
        if questions or TEST:
            start_quiz(questions or TEST)
        else:
            print('Fill questions list by "read" command before start.')
