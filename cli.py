# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import Game, Board, Human, Bot
import logging
import datetime

logging.basicConfig(filename=f'logs/{datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.log',
					format='%(asctime)s %(message)s',
					filemode='a',
          force=True)

logger=logging.getLogger()
logger.setLevel(logging.INFO)

# Reminder to check all the tests

if __name__ == '__main__':
    while True:
        mode = input("Please select the game mode, 1 for single player mode, and 2 for two player mode: ")
        # assert mode == '1' or mode == '2'
        if mode == '1':
            logger.info('Single player mode')
            while True:
                user_player = input("Please select the player you want to be, input X or O: ")
                # assert user_player == 'X' or user_player == 'O'
                if user_player == 'X':
                    playerX = Human('X')
                    playerO = Bot('O')
                    break
                elif user_player == 'O':
                    playerX = Bot('X')
                    playerO = Human('O')
                    break
                else:
                    print('Please input X or O')
            break
        elif mode == '2':
            logger.info('Two player mode')
            playerX = Human('X')
            playerO = Human('O')
            break
        else:
            logger.info('Two player mode')
            playerX = Bot('X')
            playerO = Bot('O')
            break
            # print('Please input 1 or 2')
    game = Game(playerX, playerO)
    winner = game.run(logger)
    logger.info(winner)