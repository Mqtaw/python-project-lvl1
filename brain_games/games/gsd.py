import prompt
from brain_games.cli import welcome_user
from random import randint


def question_answer():
    num1 = randint(1, 99)
    num2 = randint(1, 99)

    print('Question: {} {}'.format(str(num1), str(num2)))
    answer = prompt.integer('Your answer: ')
    correct_answer = nod(num1, num2)
    return (answer == correct_answer, answer, correct_answer)


def nod(num1, num2):
    min_num = min(num1, num2)
    i = min_num
    while i > 0:
        if num1 % i == 0 and num2 % i == 0:
            return i
        else:
            i -= 1


def game():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
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
