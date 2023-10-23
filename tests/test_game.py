import unittest
from tic_tac_toe.game import TicTacToe


def test_init():
    # Initialize a TicTacToe instance
    game = TicTacToe()

    # Check initial board state
    assert game.board == [' ' for _ in range(9)]
    assert game.winner == None
    assert game.current_player == 'X'
    assert game.moves_count == 0


def test_welcome_message():
    # Initialize a TicTacToe instance
    game = TicTacToe()

    # Check if welcome message is generated correctly
    expected_message = pyfiglet.figlet_format("Welcome to Tic Tac Toe")
    assert game.welcome_message() == expected_message


def test_make_move(self):
    self.assertTrue(self.game.make_move(0, 'X'))
    self.assertEqual(self.game.board[0], 'X')

def test_invalid_move(self):
    self.assertTrue(self.game.make_move(0, 'X'))
    self.assertFalse(self.game.make_move(0, 'O'))
    self.assertEqual(self.game.board[0], 'X')

def test_check_winner():
    # Test case 1: X wins in a row
    game = TicTacToe()
    game.board = ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
    assert game.check_winner() == True
    assert game.winner == 'X'

    # Test case 2: O wins in a column
    game = TicTacToe()
    game.board = ['O', ' ', ' ', 'O', ' ', ' ', 'O', ' ', ' ']
    assert game.check_winner() == True
    assert game.winner == 'O'

    # Test case 3: X wins in a diagonal
    game = TicTacToe()
    game.board = ['O', 'O', 'X', 'X', 'X', 'O', 'X', 'O', ' ']
    assert game.check_winner() == True
    assert game.winner == 'X'

    # Test case 4: Draw
    game = TicTacToe()
    game.board = ['X', 'O', 'X', 'X', 'O', 'O', 'O', 'X', 'X']
    assert game.check_winner() == True
    assert game.winner == 'Draw'

    # Test case 5: No winner yet
    game = TicTacToe()
    game.board = ['X', ' ', 'O', ' ', 'O', 'X', 'O', 'X', 'O']
    assert game.check_winner() == False
    assert game.winner == None
    
    # Test case 6: X wins after 9 moves
    game = TicTacToe()

    # Simulate a game with a winner
    game.moves_count = 9
    game.winner = 'X'

    # Check if draw is not declared if there's already a winner
    assert game.declare_draw() == False


if __name__ == '__main__':
    import pytest
    pytest.main(['-vv', '--cov=tic_tac_toe'])
