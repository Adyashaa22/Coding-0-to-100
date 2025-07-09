#tic tac toe game
import random
def print_board(board):
    print("Current board:")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
def check_winner(board):
    # Check rows, columns, and diagonals for a winner
    for row in board:
        if row.count(row[0]) == 3 and row[0] != " ":
            return row[0]
    for col in range(3):
        
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
        