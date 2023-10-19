import pyfiglet

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.winner = None
        self.current_player = 'X'
        self.moves_count = 0

        # Display welcome message
        print(pyfiglet.figlet_format("Welcome to Tic Tac Toe"))

    def print_board(self):
        print(f'{self.board[0]} | {self.board[1]} | {self.board[2]}')
        print('--|---|--')
        print(f'{self.board[3]} | {self.board[4]} | {self.board[5]}')
        print('--|---|--')
        print(f'{self.board[6]} | {self.board[7]} | {self.board[8]}')

    def make_move(self, position, player):
        if self.board[position] == ' ':
            self.board[position] = player
            self.moves_count += 1
            return True
        else:
            print(f"Position {position} is already taken. Please choose another position.")
            return False

    def check_winner(self):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != ' ':
                self.winner = self.board[condition[0]]
                return True

        if self.moves_count == 9 and self.winner is None:
            self.winner = 'Draw'
            return True

        return False

