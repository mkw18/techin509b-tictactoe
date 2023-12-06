# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.

import random
import pandas as pd

def read_games(path):
    try:
        return pd.read_csv(path, index_col=0)
    except FileNotFoundError:
        return pd.DataFrame(columns=[
            "GameID",
            "Player 1",
            "Player 2",
            "Winner",
            "Starting Point",
            "Position",
            "Step",
            "Result of the First Player"
        ])


class Board:
    def __init__(self):
        self._rows = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
        self.row = 3
        self.col = 3

    def __str__(self):
        s = '-------\n'
        for row in self._rows:
            for cell in row:
                s = s + '|'
                if cell == None:
                    s=s+' '
                else:
                    s=s+cell
            s = s + '|\n-------\n'
        return s

    def get(self, x, y):
        return self._rows[x][y]

    def set(self, x, y, value):
        self._rows[x][y] = value

    def get_winner(self):
        for row in self._rows:
            if len(set(row)) == 1 and row[0]:
                return row[0]
        for j in range(len(self._rows[0])):
            if len(set([self._rows[i][j] for i in range(len(self._rows))])) == 1 and self._rows[0][j]:
                return self._rows[0][j]
        if len(set([self._rows[i][i] for i in range(len(self._rows))])) == 1 and self._rows[0][0]:
            return self._rows[0][0]
        if len(set([self._rows[i][len(self._rows)-i-1] for i in range(len(self._rows))])) == 1\
            and self._rows[0][len(self._rows[0])-1]:
            return self._rows[0][len(self._rows[0])-1]

        for row in self._rows:
            if None in row:
                return None
        return 'Draw'


class Game:
    def __init__(self, playerX, playerO):
        self._board = Board()
        self._playerX = playerX
        self._playerO = playerO
        self._current_player = playerX
        if isinstance(playerX, Human) and isinstance(playerO, Human):
            self._player = 2
        else:
            self._player = 1

    def other_player(self):
        """Given the character for a player, returns the other player."""
        if self._current_player == self._playerX:
            return self._playerO
        return self._playerX

    def run(self, logger):
        step = 0
        while self._board.get_winner() == None:
            step += 1
            logger.info(f'Step {step}: {self._current_player.id} take the turn')
            x,y = self._current_player.get_move(self._board)
            print(self._board)
            logger.info(f'Renew the board: \n{self._board}')
            self._current_player = self.other_player()
            if step == 1:
                starting_point = [x,y]
                logger.info(f'Starting point: {starting_point}')

        winner = self._board.get_winner()
        position = starting_point[0]%2 + starting_point[1]%2
        position_map = ['corner', 'middle', 'center']

        df = read_games('logs/database.csv')
        df.loc[len(df)] = {
            "GameID": len(df)+1,
            "Player 1": "X",
            "Player 2": "O",
            "Winner" : winner,
            "Starting Point": starting_point,
            "Position": position_map[position],
            "Step": step,
            "Result of the First Player": 'Win' if winner == 'X' else ('Lose' if winner == 'O' else 'Draw')
        }
        df.to_csv('logs/database.csv')
        if not winner == 'Draw':
            print(f'The winner is: {winner}')
            return f'The winner is: {winner}'
        else:
            print('Draw!')
            return 'Draw!'


class Human:
    def __init__(self, id):
        self.id = id

    def get_move(self, board, x=0, y=0):
        while True:
            movement = input(f'Player {self.id}, please enter your next move, ranging from 0 to 2 (format: x,y): ').split(',')
            x = int(movement[0].strip())
            y = int(movement[1].strip())
            if board.get(x,y) == None:
                board.set(x, y, self.id)
                break
            else:
                print('Occupied position, please try again.')
                return 'Occupied position, please try again.'
        return x,y


class Bot:
    def __init__(self, id):
        self.id = id

    def get_move(self, board):
        available_pos = []
        for i in range(board.row):
            for j in range(board.col):
                if board.get(i,j) == None:
                    available_pos.append((i,j))
        x, y = random.choices(available_pos)[0]
        print(f"Player {self.id}'s next move is {x, y}.")
        board.set(x, y, self.id)
        return x,y
  
