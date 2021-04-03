import prompt
from brain_games.cli import welcome_user
from random import randint


def question_answer():
    number = randint(1, 100)
    print('Question: {}'.format(str(number)))
    answer = prompt.string('Your answer: ').lower()
    correct_answer = 'yes' if is_simple(number) is True else 'no'
    return (answer == correct_answer, answer, correct_answer)


def game():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
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


def is_simple(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
