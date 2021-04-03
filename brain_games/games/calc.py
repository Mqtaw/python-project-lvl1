import prompt
from brain_games.cli import welcome_user
from random import random
from random import choice


def game():
    name = welcome_user()
    print('What is the result of the expression?')
    for i in range(3):
        temp = question_answer()
        if temp[0] is True:
            print('Correct!')
        else:
            print("""'{}' is wrong answer ;(. Correct answer was '{}'.\
            """.format(temp[1], temp[2]))
            print("Let's try again, {}!".format(name))
            break
    else:
        print('Congratulations, {}!'.format(name))


def question_answer():
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
