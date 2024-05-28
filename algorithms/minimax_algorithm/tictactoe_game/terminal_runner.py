"""
Main runner of the game in terminal
"""
from algorithms.minimax_algorithm.tictactoe_game.tictactoe import TicTacToe


def print_board(board):
    """
    Prints the board in a readable format.
    """
    for row in board:
        print(" | ".join([cell if cell is not None else " " for cell in row]))
        print("-" * 10)


def get_user_action():
    """
    Prompts the user to enter a move.
    """
    while True:
        try:
            row = int(input("Enter row (1, 2, or 3): ")) - 1
            col = int(input("Enter column (1, 2, or 3): ")) - 1
            if (row in range(3)) and (col in range(3)):
                return row, col
            else:
                print("Invalid input. Please enter numbers between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter valid integers.")


def main():
    """
    Main function to run the Tic Tac Toe game.
    """
    user = None
    ttt = TicTacToe()
    while user not in [ttt.X_Player, ttt.O_Player]:
        user = input("Choose your player (X/O): ").upper()
        if user == "X" or user == "x":
            user = ttt.X_Player
        elif user == "O" or user == "o":
            user = ttt.O_Player

    board = ttt.initial_state()

    while not ttt.terminal(board):
        print_board(board)

        if ttt.player(board) == user:
            print(f"Your turn ({user}):")
            while True:
                action = get_user_action()
                if action in ttt.actions(board):
                    board = ttt.result(board, action)
                    break
                else:
                    print("Invalid move. Try again.")
        else:
            print("AI's turn:")
            action = ttt.minimax(board)
            board = ttt.result(board, action)

    print_board(board)
    winner = ttt.winner(board)
    if winner:
        print(f"Game Over: {winner} wins.")
    else:
        print("Game Over: It's a tie.")


if __name__ == "__main__":
    main()
