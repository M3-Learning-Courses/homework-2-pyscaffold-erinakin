import unittest
from unittest.mock import patch
from io import StringIO
from game import TicTacToe

class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        self.game = TicTacToe()

    def test_initialization(self):
        self.assertEqual(self.game.board, [' ' for _ in range(9)])

    def test_make_move(self):
        self.assertTrue(self.game.make_move(0, 'X'))
        self.assertEqual(self.game.board[0], 'X')
        self.assertFalse(self.game.make_move(0, 'O'))  # Attempting to make a move on an occupied position

    def test_check_winner(self):
        self.game.board = ['X', 'X', 'X', 'O', 'O', ' ', ' ', ' ', ' ']
        self.assertEqual(self.game.check_winner(2), 'X')  # X wins by completing top row
        self.game.board = ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X', 'O']
        self.assertEqual(self.game.check_winner(8), 'Draw')  # Game ends in a draw

    def test_print_board(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.game.print_board()
            output = mock_stdout.getvalue().strip()
            expected_output = "  |   |  \n---------\n  |   |  \n---------\n  |   |  "
            self.assertEqual(output, expected_output)

    def test_print_welcome_message(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.game.print_welcome_message()
            output = mock_stdout.getvalue().strip()
            expected_output = "WELCOME TO TIC TAC TOE!"
            self.assertEqual(output, expected_output)

    def test_display_winner_message(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.game.display_winner_message('X')
            output = mock_stdout.getvalue().strip()
            expected_output = " PLAYER X WINS! "
            self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
