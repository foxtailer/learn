Quiz Program

Overview:
This command-line quiz program allows users to either create a custom quiz by adding their own 
questions or start a quiz using predefined questions. 


Quize
"read" for writing new questions.
"start" for starting quiz.

Q:


Commands:
read <number>: Allows the user to input a specified number of questions and their corresponding answers. 
The format for each question-answer pair is question; answer.
start: Starts the quiz, either with the questions provided by the user or, if no questions have been input 
yet, with a set of predefined questions stored in the TEST dictionary.


Q: read 3

Write new questions in format:
question; answer
";" simbol inside question or answer not required.
n:


Writing Questions:
When using the read <number> command, the user is prompted to write a series of questions. For each question, 
the user must input it in the format question; answer.
Each entry should not contain a semicolon (;) inside the question or answer itself, as it is used to separate 
the question from the answer.


Q: start
"q" to exite.
Your name:


Starting the Quiz:
The user is asked to enter their name before the quiz starts.
For each question, the user must select the correct answer from a list of choices.
After each question, the program will immediately tell the user if their answer is correct or incorrect, and 
display their score.


Q: start
"q" to exite.
Your name: avan
Who serves as the speaker of the prologue in Shakespeare's Romeo and Juliet?
Chorus, Trapezius, Pneumonia, Arthur Conan Doyle, Clint Eastwood
(Avan): Chorus
Question 1: Correct. 1/6 (16.67%)



Exiting the Program:
After completing the quiz, the user can either:
    Start a new quiz with a new name.
    Exit by typing 'q'. If no one is taking the quiz and 'q' is entered, the program will display the final 
    results, including each user's individual score and the average score across all users.

Avan: 2/6 (33.33%)
Average score: 2/6(33.33%)
