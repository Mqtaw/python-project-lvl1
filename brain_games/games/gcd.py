import prompt
from random import randint


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_question_answer():
    num1 = randint(1, 99)
    num2 = randint(1, 99)

    print('Question: {} {}'.format(str(num1), str(num2)))
    answer = prompt.integer('Your answer: ')
    correct_answer = get_nod(num1, num2)
    return (answer == correct_answer, answer, correct_answer)


def get_nod(num1, num2):
    min_num = min(num1, num2)
    i = min_num
    while i > 0:
        if num1 % i == 0 and num2 % i == 0:
            return i
        else:
            i -= 1
