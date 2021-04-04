import prompt
from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def get_question_answer():
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
