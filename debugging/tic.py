#!/usr/bin/python3

def print_board(board):
    """Print the current state of the game board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """Check if a player has won the game."""
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def check_draw(board):
    """Check if the game ended in a draw (no more moves left)."""
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """Main function to play the game."""
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while True:
        print_board(board)
        
        # Get row and column input from player
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
            
            # Input validation
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid input. Row and column must be between 0 and 2.")
                continue
            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue
            
            # Update board
            board[row][col] = player
            
            # Check for winner
            if check_winner(board):
                print_board(board)
                print("Player " + player + " wins!")
                break
            
            # Check for draw
            if check_draw(board):
                print_board(board)
                print("The game is a draw!")
                break
            
            # Switch players
            player = "O" if player == "X" else "X"
        
        except ValueError:
            print("Invalid input. Please enter numeric values for row and column.")

# Start the game
tic_tac_toe()
