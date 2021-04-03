import prompt
from brain_games.cli import welcome_user
from random import random


def game():
    def question_answer():
        question = int(random() * 100)
        print('Question: {}'.format(str(question)))
        answer = prompt.string('Your answer: ').lower()
        if (((question % 2 == 0) and (answer == 'yes'))) or\
                ((question % 2 != 0) and (answer == 'no')):
            return (True, question, answer)
        else:
            correct_answer = 'no' if answer == 'yes' else 'yes'
            return (False, question, correct_answer)

    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

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
