"""
This is a skeleton file that can serve as a starting point for a Python
console script. To run this script uncomment the following lines in the
``[options.entry_points]`` section in ``setup.cfg``::

    console_scripts =
         fibonacci = tic_tac_toe.skeleton:run

Then run ``pip install .`` (or ``pip install -e .`` for editable mode)
which will install the command ``fibonacci`` inside your current environment.

Besides console scripts, the header (i.e. until ``_logger``...) of this file can
also be used as template for Python modules.

Note:
    This file can be renamed depending on your needs or safely removed if not needed.

References:
    - https://setuptools.pypa.io/en/latest/userguide/entry_point.html
    - https://pip.pypa.io/en/stable/reference/pip_install
"""

import argparse
import logging
import sys

from tic_tac_toe import __version__

__author__ = "Erin Akinjide"
__copyright__ = "Erin Akinjide"
__license__ = "MIT"

_logger = logging.getLogger(__name__)

# My attempt at creating this.

from game import TicTacToe

class TicTacToeAPI:
    """
    A class to handle the Tic Tac Toe game logic through an API.
    """
    def __init__(self):
        self.game = TicTacToe()

    def make_move(self, position, player):
        """
        Makes a move on the board.

        Args:
            position (int): The position on the board where the move is made (0-8).
            player (str): The player making the move ('X' or 'O').

        Returns:
            str: The result message indicating if the move was successful or not.
        """
        if self.game.make_move(position, player):
            return f"Player {player} successfully made a move at position {position}."
        else:
            return f"Position {position} is already taken. Please choose an empty position."

    def check_winner(self, position):
        """
        Checks if there is a winner after a move is made.

        Args:
            position (int): The position on the board where the last move was made (0-8).

        Returns:
            str: The result message indicating the winner or draw.
        """
        winner = self.game.check_winner(position)
        if winner:
            if winner == 'Draw':
                return "It's a draw!"
            else:
                return f"Player {winner} wins!"
        else:
            return "No winner yet."

class TicTacToeCLI:
    """
    A class to handle the command-line interface for the Tic Tac Toe game.
    """
    def __init__(self):
        self.api = TicTacToeAPI()

    def start_game(self):
        """
        Starts the Tic Tac Toe game.
        """
        self.api.game.print_welcome_message()

        while True:
            self.api.game.print_board()
            position = int(input("Player X, enter position (0-8): "))
            result = self.api.make_move(position, 'X')

            print(result)

            if 'wins' in result or 'draw' in result:
                break

            self.api.game.print_board()
            position = int(input("Player O, enter position (0-8): "))
            result = self.api.make_move(position, 'O')

            print(result)

            if 'wins' in result or 'draw' in result:
                break

if __name__ == "__main__":
    cli = TicTacToeCLI()
    cli.start_game()



