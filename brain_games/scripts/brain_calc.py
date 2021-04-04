#!/usr/bin/env python
from brain_games.engine import begin_game
from brain_games.games import calc


def main():
    begin_game(calc)


if __name__ == '__main__':
    main()
