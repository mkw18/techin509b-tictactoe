# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board


if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    current_user = 'X'
    while winner == None:
        print(f"TODO: {current_user} take a turn!")
        # TODO: Show the board to the user.
        for row in board:
            print(row)
        # TODO: Input a move from the player.
        movement = input('Your next move (format: x,y): ').split(',')
        x = int(movement[0].strip())
        y = int(movement[1].strip())
        # TODO: Update the board.
        board[x][y] = current_user
        # TODO: Update who's turn it is.
        current_user = 'XO'.replace(current_user, '')
        winner = 'X'  # FIXME
