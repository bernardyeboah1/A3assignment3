# Student Name: Bernard Yeboah
# Student Number: 100861980

import random
import math
import sys
from time import time


def quiz_title():
    title = 'Welcome to The Exponents Quiz'
    print('-' * len(title))
    print(title)
    print('-' * len(title))


def quiz():
    correct = 0
    count = 0
    totalquestions = 5
    print("The Quiz Has Begun\n")
    start_time = time()

    while count < 5:
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
        user_answer = int(input(f"What is {num1} ^ {num2}?\n:"))
        answer = math.pow(num1, num2)

        if user_answer == answer:
            print('You are Correct!\n')
            correct = correct + 1
        else:
            if user_answer != answer:
                print(f"You are wrong, the correct answer is {answer}\n")
            count = count + 1

    end_time = time()
    total_time = end_time - start_time
    print(f"You got {correct}/{totalquestions} correct in {(total_time * 10).__round__(2)} seconds\n")
    print(f"Your percentage is {(correct * 100 / count).__round__()}%\n")

    restart = input("""Would you like to take the quiz again?
    If Yes, Please Enter 'y'
    If No, Please Enter 'n'
    :""")
    if restart.lower() == 'y':
        quiz()
    elif restart.lower() == 'n':
        print("Thank you for taking the quiz.")
        sys.exit('Goodbye')


quiz_title()
quiz()













