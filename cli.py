# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import Game, Board, Human, Bot


# Reminder to check all the tests

if __name__ == '__main__':
    mode = input("Please select the game mode, 1 for single player mode, and 2 for two player mode: ")
    assert mode == '1' or mode == '2'
    if mode == '1':
        user_player = input("Please select the player you want to be, input X or O: ")
        assert user_player == 'X' or user_player == 'O'
        if user_player == 'X':
            playerX = Human('X')
            playerO = Bot('O')
        else:
            playerX = Bot('X')
            playerO = Human('O')
    else:
        playerX = Human('X')
        playerO = Human('O')
    game = Game(playerX, playerO)
    game.run()
    