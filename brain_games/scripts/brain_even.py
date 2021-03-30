import prompt
from brain_games.scripts.brain_games import greet
from random import random


def main():
    name = greet()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for i in range(3):
        question = int(random() * 100)
        print('Question: {}'.format(question))
        answer = prompt.string('Your answer: ').lower()
        if (((question % 2 == 0) and (answer == 'yes'))) or\
                ((question % 2 != 0) and (answer == 'no')):
            print('Correct!')
        else:
            correct_answer = 'no' if answer == 'yes' else 'yes'
            print("""'{}' is wrong answer ;(. Correct answer was '{}'.\
            """.format(answer, correct_answer))
            print("Let's try again, {}!".format(name))
            break
    else:
        print('Congratulations, {}!'.format(name))


if __name__ == '__main__':
    main()
