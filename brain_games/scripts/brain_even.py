#!/usr/bin/env python
from brain_games.engine import begin_game
from brain_games.games import even


def main():
    begin_game(even)


if __name__ == '__main__':
    main()
