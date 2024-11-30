import numpy as np

def print_board(board):
    """Prints the Tic Tac Toe board in a user-friendly format."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    """Checks if there is a winner."""
    # Check rows and columns
    for i in range(3):
        if all(board[i, :] == "X") or all(board[i, :] == "O"):
            return board[i, 0]
        if all(board[:, i] == "X") or all(board[:, i] == "O"):
            return board[0, i]
    # Check diagonals
    if all(np.diag(board) == "X") or all(np.diag(board) == "O"):
        return board[0, 0]
    if all(np.diag(np.fliplr(board)) == "X") or all(np.diag(np.fliplr(board)) == "O"):
        return board[0, 2]
    return None


def is_full(board):
    """Checks if the board is full."""
    return not any(" " in row for row in board)


def get_move():
    """Prompts the player for a valid move."""
    while True:
        try:
            move = input("Enter your move as row,column (e.g., 1,2): ")
            row, col = map(int, move.split(","))
            if row in [1, 2, 3] and col in [1, 2, 3]:
                return row - 1, col - 1
            else:
                print("Invalid input! Row and column must be between 1 and 3.")
        except ValueError:
            print("Invalid input format! Please enter as row,column.")


def play_tic_tac_toe():
    """Main function to play the Tic Tac Toe game."""
    board = np.full((3, 3), " ")
    current_player = "X"
    winner = None

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while not is_full(board) and winner is None:
        print(f"Player {current_player}'s turn:")
        row, col = get_move()

        if board[row, col] == " ":
            board[row, col] = current_player
            print_board(board)
            winner = check_winner(board)
            if winner is None:
                current_player = "O" if current_player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")

    if winner:
        print(f"Player {winner} wins!")
    else:
        print("It's a tie!")


if __name__ == "__main__":
    play_tic_tac_toe()
