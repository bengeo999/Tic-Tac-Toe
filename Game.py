def print_board(board):
    """Print the current state of the Tic-Tac-Toe board."""
    for row in board:
        print (" | ".join(row))
        print("_ _ _ _ _ _ _ _ _ _")
def check_winner(board, player):
    """Check if a player has won the game."""
    #Check rows,columns and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
            all(board[i][2 -i] == player for i in range(3)):
                return True
        return False
    
def is_board_full(board):
     """Check if the board is full."""
     return all(cell != " " for row in board for cell in row)

def play_tic_tac_toe():
     """Main function to play the Tic-tac-toe game."""
     board = [[" "for _ in range(3)]for _ in range(3)]
     current_player = "X"

     while True:
        print_board(board)
        row = int(input(f"Player {current_player}, enter row(0-2):"))
        col = int(input(f"Player {current_player}, enter column(0-2):"))

        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                board[row][col] = current_player
                if check_winner(board, current_player):
                     print_board(board)
                     print(f"Player {current_player} wins!")
                     break
                elif is_board_full(board):
                     print_board(board)
                     print("It's a tie!")
                     break
                current_player = "0" if current_player == "X" else "X"
        else:
            print("Invalid move. Try again")
 
if __name__ == "__main__":
    play_tic_tac_toe()