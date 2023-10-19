class TicTacToe:
    def __init__(self):
        """
        Initializes a new instance of the Tic Tac Toe game.

        The game board is represented as a list of 9 empty spaces.
        """
        # Initialize the game board by creating a list of 9 empty spaces.
        self.board = [' ' for _ in range(9)]  

    # Create a method called print_board that prints the current state of the board.
    def print_board(self):
        
        # Start a new line for every 3 spaces in the board.
        for i in range(0, 9, 3):
            # Print the current row of the board.
            print(f'{self.board[i]} | {self.board[i + 1]} | {self.board[i + 2]}')
            # Print a line of dashes after every row except the last.
            if i < 6:
                print('-' * 5)

    # Create a method called make_move that takes a position and a player 'X' or 'O' as arguments.
    def make_move(self, position, player):
        # Check if the position is empty.
        if self.board[position] == ' ':
            # If the position is empty, set the position to the player.
            self.board[position] = player
            return True
        # If the position is not empty, return False.
        else:
            return False
    
    """ Create a method called check_winner that determines the winner by checking the rows columns 
    and diagonals that contain the last move made on the board."""

    def check_winner(self, position):
        
        # Extract the row and column from the position on the board.
        row = position // 3
        col = position % 3
        # Use the position to extract the player from the board.
        player = self.board[position]

        # Check row to show if it matches the player from the position.
        if self.board[row * 3] == self.board[row * 3 + 1] == self.board[row * 3 + 2] == player:
            return player

        # Check column to show if it matches the player from the position.
        if self.board[col] == self.board[col + 3] == self.board[col + 6] == player:
            return player

        # Check diagonal to show if it matches the player from the position.
        if position % 2 == 0:
            if self.board[0] == self.board[4] == self.board[8] == player or self.board[2] == self.board[4] == self.board[6] == player:
                return player

        # Show that there is a draw if there are no empty spaces left on the board.
        if ' ' not in self.board:
            return 'Draw'

    return None

