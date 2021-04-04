from brain_games.cli import welcome_user


def begin_game(game):
    name = welcome_user()
    print(game.DESCRIPTION)
    for i in range(3):
        temp = game.get_question_answer()
        if temp[0] is True:
            print('Correct!')
        else:
            print("""'{}' is wrong answer ;(. Correct answer was '{}'.\
            """.format(temp[1], temp[2]))
            print("Let's try again, {}!".format(name))
            break
    else:
        print('Congratulations, {}!'.format(name))
