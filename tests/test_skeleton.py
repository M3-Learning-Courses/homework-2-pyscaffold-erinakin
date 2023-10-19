import pytest

from tic_tac_toe.skeleton import fib, main

__author__ = "Erin Akinjide"
__copyright__ = "Erin Akinjide"
__license__ = "MIT"


def test_fib():
    """API Tests"""
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)


def test_main(capsys):
    """CLI Tests"""
    # capsys is a pytest fixture that allows asserts against stdout/stderr
    # https://docs.pytest.org/en/stable/capture.html
    main(["7"])
    captured = capsys.readouterr()
    assert "The 7-th Fibonacci number is 13" in captured.out
import unittest
from unittest.mock import patch
from io import StringIO
from tictactoe import TicTacToeAPI, TicTacToeCLI

class TestTicTacToeAPI(unittest.TestCase):

    def setUp(self):
        self.api = TicTacToeAPI()

    def test_make_move(self):
        result = self.api.make_move(0, 'X')
        self.assertEqual(result, "Player X successfully made a move at position 0.")
        result = self.api.make_move(0, 'O')
        self.assertEqual(result, "Position 0 is already taken. Please choose an empty position.")

    def test_check_winner(self):
        self.api.game.board = ['X', 'X', 'X', 'O', 'O', ' ', ' ', ' ', ' ']
        result = self.api.check_winner(2)
        self.assertEqual(result, "Player X wins!")

        self.api.game.board = ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X', 'O']
        result = self.api.check_winner(8)
        self.assertEqual(result, "It's a draw!")

class TestTicTacToeCLI(unittest.TestCase):

    def setUp(self):
        self.cli = TicTacToeCLI()

    @patch('builtins.input', side_effect=['0', '0', '1', '1', '2', '2'])
    def test_start_game(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cli.start_game()
            output = mock_stdout.getvalue().strip()

        expected_output = [
            "WELCOME TO TIC TAC TOE!",
            "  |   |  \n---------\n  |   |  \n---------\n  |   |  ",
            "Player X, enter position (0-8): Player O, enter position (0-8): ",
            "  |   |  \n---------\nX |   |  \n---------\n  |   |  ",
            "Player X, enter position (0-8): Player O, enter position (0-8): ",
            "  |   |  \n---------\nX | O |  \n---------\n  |   | X",
            "Player X, enter position (0-8): Player O, enter position (0-8): "
        ]

        for line, expected in zip(output.split('\n'), expected_output):
            self.assertEqual(line.strip(), expected)

if __name__ == '__main__':
    unittest.main()
