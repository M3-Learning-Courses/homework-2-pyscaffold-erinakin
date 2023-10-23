from tictactoe import TicTacToe

def main():

    """ Runs the game in Command Line Interface (CLI) mode."""
    game = TicTacToe()
    game.print_board()

    while not game.check_winner():
        position = int(input(f"Player {game.current_player}, enter position (0-8): "))
        if position < 0 or position > 8:
            print("Invalid position. Please enter a number between 0 and 8.")
            continue

        if game.make_move(position, game.current_player):
            game.print_board()
            game.current_player = 'O' if game.current_player == 'X' else 'X'

    if game.winner == 'Draw':
        print("It's a Draw!")
    else:
        print(f"Player {game.winner} wins!")

if __name__ == '__main__':
    main()
