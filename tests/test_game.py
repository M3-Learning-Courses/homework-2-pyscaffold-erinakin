from tic_tac_toe.game import TicTacToe
import unittest
import pytest
import pyfiglet
from io import StringIO
from unittest.mock import patch

def test_init():
    # Initialize a TicTacToe instance
    game = TicTacToe()

    # Check initial board state
    assert game.board == [' ' for _ in range(9)]
    assert game.winner == None
    assert game.current_player == 'X'
    assert game.moves_count == 0


def test_make_move():
    game = TicTacToe()
    game.make_move(0, 'X')
    assert game.board[0]== 'X'

def test_invalid_move():
    game = TicTacToe()
    game.make_move(0, 'X')
    assert game.make_move(0, 'O') == False
    #assert game.make_move() == False   

def test_check_winner():
    # Test case 1: X wins in a row
    game = TicTacToe()
    game.board = ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
    assert game.check_winner() == True
    assert game.winner == 'X'

    # Test case 2: O wins in a column
    game = TicTacToe()
    game.board = [' ', ' ', 'O', ' ', ' ', 'O', ' ', ' ', 'O']
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
    assert game.check_winner() == False
    assert game.winner == None

    # Test case 5: No winner yet
    game = TicTacToe()
    game.board = ['X', ' ', 'O', ' ', 'O', 'X', 'X', 'X', 'O']
    assert game.check_winner() == False
    assert game.winner == None
    
def test_print_board():
    game = TicTacToe()
    expected_output = "  |   |  \n--|---|--\n  |   |  \n--|---|--\n  |   |  \n"

    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        game.print_board()
        assert mock_stdout.getvalue() == expected_output



if __name__ == '__main__':
    import pytest
    pytest.main(['-vv', '--cov=game'])
