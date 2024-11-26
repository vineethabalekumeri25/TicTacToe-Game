# Tic Tac Toe Game in Python

# Function to display the board
def display_board(board):
    print("\n")
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---|---|---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---|---|---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print("\n")

# Function to check if there's a winner
def check_winner(board, player):
    win_conditions = [
        [0, 1, 2],  # Top row
        [3, 4, 5],  # Middle row
        [6, 7, 8],  # Bottom row
        [0, 3, 6],  # Left column
        [1, 4, 7],  # Middle column
        [2, 5, 8],  # Right column
        [0, 4, 8],  # Diagonal 1
        [2, 4, 6],  # Diagonal 2
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Function to check if the board is full (a draw)
def is_draw(board):
    return " " not in board

# Main function to run the game
def tic_tac_toe():
    print("Welcome to Tic Tac Toe!")
    board = [" "] * 9  # Empty board
    current_player = "X"  # Player X starts

    # Game loop
    while True:
        display_board(board)
        print(f"Player {current_player}'s turn.")

        # Input validation
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move >= 9 or board[move] != " ":
                print("Invalid move. Try again.")
                continue
        except ValueError:
            print("Please enter a valid number between 1 and 9.")
            continue

        # Make the move
        board[move] = current_player

        # Check for winner
        if check_winner(board, current_player):
            display_board(board)
            print(f"Congratulations! Player {current_player} wins!")
            break

        # Check for draw
        if is_draw(board):
            display_board(board)
            print("It's a draw!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"

# Run the game
if __name__ == "__main__":
    tic_tac_toe()