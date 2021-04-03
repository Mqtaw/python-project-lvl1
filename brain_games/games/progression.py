import prompt
from brain_games.cli import welcome_user
from random import randint


def question_answer():
    progression_length = randint(5, 10)
    progression_start = randint(0, 100)
    progression_step = randint(1, 5)
    missing_element = randint(0, (progression_length - 1))
    progression = [progression_start]
    for i in range(1, progression_length):
        progression.append(progression[i - 1] + progression_step)
    correct_answer = progression[missing_element]
    progression[missing_element] = '..'
    print('Question: ', end='')
    print(*progression)
    answer = prompt.integer('Your answer: ')
    return (answer == correct_answer, answer, correct_answer)


def game():
    name = welcome_user()
    print('What number is missing in the progression?')
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
