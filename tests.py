import unittest
from logic import Board, Game, Human, Bot


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_init(self):
        for x in range(3):
            for y in range(3):
                self.assertIsNone(self.board.get(x,y))
    
    def test_set_get(self):
        self.board.set(1, 0, 'O')
        self.assertEqual(self.board.get(1, 0), 'O')

    def test_get_winner(self):
        self.board.set(0, 0, 'X')
        self.board.set(0, 1, 'X')
        self.board.set(0, 2, 'X')
        self.assertEqual(self.board.get_winner(), 'X')
        self.board.set(0, 1, 'O')
        self.board.set(1, 0, 'O')
        self.board.set(1, 1, 'O')
        self.board.set(1, 2, 'O')
        self.assertEqual(self.board.get_winner(), 'O')
        self.board.set(1, 2, 'X')
        self.assertIsNone(self.board.get_winner())
        self.board.set(2, 0, 'O')
        self.board.set(2, 1, 'X')
        self.board.set(2, 2, 'O')
        self.assertEqual(self.board.get_winner(), 'Draw')
    

class TestGame(unittest.TestCase):
    def setUp(self):
        self.playerX = Human('X')
        self.playerO = Human('O')
        self.game = Game(self.playerX, self.playerO)

    def test_init(self):
        self.assertIsInstance(self.game._board, Board)
        self.assertEqual(self.game._current_player, self.playerX)

    def test_other_player(self):
        self.assertEqual(self.game.other_player(), self.playerO)

    def test_run(self):
        self.game._board.set(0, 0, 'X')
        self.game._board.set(0, 1, 'X')
        self.game._board.set(0, 2, 'X')
        self.assertEqual(self.game.run(), 'The winner is: X')
        self.game._board.set(0, 1, 'O')
        self.game._board.set(1, 0, 'O')
        self.game._board.set(1, 1, 'O')
        self.game._board.set(1, 2, 'O')
        self.assertEqual(self.game.run(), 'The winner is: O')
        self.game._board.set(1, 2, 'X')
        self.game._board.set(2, 0, 'O')
        self.game._board.set(2, 1, 'X')
        self.game._board.set(2, 2, 'O')
        self.assertEqual(self.game.run(), 'Draw!')


if __name__ == '__main__':
    unittest.main()
