import prompt
from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_answer():
    number = randint(1, 100)
    print('Question: {}'.format(str(number)))
    answer = prompt.string('Your answer: ').lower()
    correct_answer = 'yes' if is_simple(number) is True else 'no'
    return (answer == correct_answer, answer, correct_answer)


def is_simple(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
