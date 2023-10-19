import pyfiglet

class TicTacToe:
    def __init__(self):
        """
        Initializes a new instance of the Tic Tac Toe game.

        The game board is represented as a list of 9 empty spaces.
        """
        self.board = [' ' for _ in range(9)]  

    def print_board(self):
        """
        Prints the current state of the board.
        """
        
        # Start a new line for every 3 spaces in the board.
        for i in range(0, 9, 3):

            # Print the current row of the board.
            print(f'{self.board[i]} | {self.board[i + 1]} | {self.board[i + 2]}')
            # Print a line of dashes after every row except the last
            if i < 6:
                print('-' * 9)

    def make_move(self, position, player):
        """
        Makes a move on the board.

        Args:
            position (int): The position on the board where the move is made (0-8).
            player (str): The player making the move ('X' or 'O').

        Returns:
            bool: True if the move was successful, False if the position is already taken.
        """

        # Check if the position is empty.
        if self.board[position] == ' ':
            
            # If the position is empty, set the position to the player.
            self.board[position] = player
            return True
        else:
            return False
    
    def check_winner(self, position):
        """
        Determines the winner by checking the rows, columns, and diagonals that contain the last move made on the board.

        Args:
            position (int): The position on the board where the last move was made (0-8).

        Returns:
            str or None: The winning player ('X' or 'O'), 'Draw' for a draw, or None if no winner yet.
        """
          # Extract the row and column from the position on the board.
        row = position // 3
        col = position % 3
        # Use the position to extract the player from the board.
        player = self.board[position]

        # Check row to see if it matches the player from the position.
        if self.board[row * 3] == self.board[row * 3 + 1] == self.board[row * 3 + 2] == player:
            return player

        # Check column to see if it matches the player from the position.
        if self.board[col] == self.board[col + 3] == self.board[col + 6] == player:
            return player

        # Check diagonal to see if it matches the player from the position.
        if position % 2 == 0:
            if self.board[0] == self.board[4] == self.board[8] == player or self.board[2] == self.board[4] == self.board[6] == player:
                return player

        # Show that there is a draw if there are no empty spaces left on the board.
        if ' ' not in self.board:
            return 'Draw'

        return None

    def print_welcome_message(self):
        """
        Prints a welcome message using pyfiglet.
        """
        welcome_message = pyfiglet.figlet_format('Welcome to Tic Tac Toe!', font='standard')
        print(welcome_message)

    def display_winner_message(self, winner):
        """
        Display a stylized message announcing the winner.

        Args:
            winner (str): The winning player ('X' or 'O').
        """
        if winner == 'Draw':
            message = pyfiglet.figlet_format('It\'s a Draw!', font='standard')
        else:
            message = pyfiglet.figlet_format(f'Player {winner} Wins!', font='standard')
        print(message)
