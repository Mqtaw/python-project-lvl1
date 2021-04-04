import prompt
from random import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_answer():
    question = int(random() * 100)
    print('Question: {}'.format(str(question)))
    answer = prompt.string('Your answer: ').lower()
    if (((question % 2 == 0) and (answer == 'yes'))) or\
            ((question % 2 != 0) and (answer == 'no')):
        return (True, question, answer)
    else:
        correct_answer = 'no' if answer == 'yes' else 'yes'
        return (False, answer, correct_answer)
