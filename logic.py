# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.


def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]


def get_winner(board):
    """Determines the winner of the given board.
    Returns 'X', 'O', or None."""
    # Decide if 'O' won
    if board[0] == ['O', 'O', 'O'] or board[1] == ['O', 'O', 'O'] or board[2] == ['O', 'O', 'O']\
    or [board[0][0], board[1][0], board[2][0]] == ['O', 'O', 'O'] or [board[0][1], board[1][1], board[2][1]] == ['O', 'O', 'O'] or [board[0][2], board[1][2], board[2][2]] == ['O', 'O', 'O']\
    or [board[0][0], board[1][1], board[2][2]] == ['O', 'O', 'O'] or [board[0][2], board[1][1], board[2][0]] == ['O', 'O', 'O']:
        return 'O'
    # Decide if 'X' won
    elif board[0] == ['X', 'X', 'X'] or board[1] == ['X', 'X', 'X'] or board[2] == ['X', 'X', 'X']\
    or [board[0][0], board[1][0], board[2][0]] == ['X', 'X', 'X'] or [board[0][1], board[1][1], board[2][1]] == ['X', 'X', 'X'] or [board[0][2], board[1][2], board[2][2]] == ['X', 'X', 'X']\
    or [board[0][0], board[1][1], board[2][2]] == ['X', 'X', 'X'] or [board[0][2], board[1][1], board[2][0]] == ['X', 'X', 'X']:
        return 'X'
    # Otherwise draw
    else:
        return None


def other_player(player):
    """Given the character for a player, returns the other player."""
    return "XO".replace(player, '')
