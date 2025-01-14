#!/usr/bin/python3
def print_board(board):
    """
    Prints the Tic-Tac-Toe board in a readable format.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Checks if there is a winner on the board.
    Returns True if there's a winner, else False.
    """
    # Check rows for winner
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns for winner
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals for winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_board_full(board):
    """
    Checks if the board is full and no spaces are left.
    """
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """
    Main function to handle the game logic.
    Players take turns to play and the game ends when there's a winner or a tie.
    """
    board = [[" "]*3 for _ in range(3)]  # Initialize an empty board
    player = "X"  # Starting player
    while not check_winner(board) and not is_board_full(board):  # Continue until there is a winner or a tie
        print_board(board)  # Display the current board
        try:
            # Get input for row and column, ensuring they are valid integers within the board range
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
            
            # Check if the row and column are within the valid range
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid input. Please enter row and column as 0, 1, or 2.")
                continue
            
            # Check if the cell is already taken
            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue
            
            # Place the current player's symbol
            board[row][col] = player

            # Switch players
            player = "O" if player == "X" else "X"

        except ValueError:
            # Catch non-integer inputs (invalid input types)
            print("Invalid input. Please enter valid integers for row and column.")
    
    print_board(board)  # Display the final board after game ends

    # Check if the game ended in a win or a tie
    if check_winner(board):
        print(f"Player {player} wins!")
    else:
        print("It's a tie!")

# Start the game
tic_tac_toe()
