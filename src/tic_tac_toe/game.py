import pyfiglet

class TicTacToe:
    """
    A class representing the Tic Tac Toe game.

    Attributes:
    -----------
    board : list
        A list representing the game board.
    winner : str
        A string representing the winner of the game.
    current_player : str
        A string representing the current player.
    moves_count : int
        An integer representing the number of moves made in the game.
    """

    def __init__(self):
        """
        Initializes a new instance of the TicTacToe class.
        """
        self.board = [' ' for _ in range(9)]
        self.winner = None
        self.current_player = 'X'
        self.moves_count = 0

        # Display welcome message
        return pyfiglet.figlet_format("Welcome to Tic Tac Toe")

    def print_board(self):# chech the test coverage for this function
        """
        Prints the current state of the game board.
        """
        print(f'{self.board[0]} | {self.board[1]} | {self.board[2]}')
        print('--|---|--')
        print(f'{self.board[3]} | {self.board[4]} | {self.board[5]}')
        print('--|---|--')
        print(f'{self.board[6]} | {self.board[7]} | {self.board[8]}')

    def make_move(self, position, player):
        """
        Makes a move on the game board.

        Parameters:
        -----------
        position : int
            An integer representing the position on the board where the move is to be made.
        player : str
            A string representing the player making the move.

        Returns:
        --------
        bool
            True if the move was made successfully, False otherwise.
        """
        if self.board[position] == ' ':
            self.board[position] = player
            self.moves_count += 1
            return True
        else:
            print(f"Position {position} is already taken. Please choose another position.")
            return False

    def check_winner(self): #Check the
        """
        Checks if there is a winner in the game.

        Returns:
        --------
        bool
            True if there is a winner, False otherwise.
        """
        # Define the win conditions
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

        for condition in win_conditions:
            # Check if any of the win conditions are satisfied.
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != ' ':
                self.winner = self.board[condition[0]]
                return True
        # Check if the game has ended in a draw
        if self.moves_count == 9 and self.winner is None:
            self.winner = 'Draw'
            return True
        else:
            return False

        return False

