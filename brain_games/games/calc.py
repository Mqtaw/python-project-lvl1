import prompt
from random import random
from random import choice


DESCRIPTION = 'What is the result of the expression?'


def get_question_answer():
    num1 = int(random() * 100)
    num2 = int(random() * 100)
    operator = choice(('+', '-', '*'))
    print('Question: {} {} {}'.format(str(num1), operator, str(num2)))
    answer = prompt.integer('Your answer: ')
    if operator == '+':
        return (((num1 + num2) == answer), answer, (num1 + num2))
    if operator == '-':
        return (((num1 - num2) == answer), answer, (num1 - num2))
    if operator == '*':
        return (((num1 * num2) == answer), answer, (num1 * num2))
