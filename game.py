import random

# Initialize the Tic-Tac-Toe board
def initialize_board():
    return [" " for _ in range(9)]

# Display the Tic-Tac-Toe board
def display_board(board):
    print(" " + board[0] + " | " + board[1] + " | " + board[2] + " ")
    print("-----------")
    print(" " + board[3] + " | " + board[4] + " | " + board[5] + " ")
    print("-----------")
    print(" " + board[6] + " | " + board[7] + " | " + board[8] + " ")

# Check if the game is over
def is_game_over(board):
    return check_winner(board) or " " not in board

# Check for a win
def check_winner(board):
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6)]

    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]

    return None

# Player's move
def player_move(board):
    while True:
        move = input("Enter your move (0-8): ")
        if move.isdigit() and 0 <= int(move) <= 8 and board[int(move)] == " ":
            return int(move)
        else:
            print("Invalid move. Try again.")

# Computer's move using minimax algorithm
def computer_move(board):
    best_score = -float("inf")
    best_move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i

    return best_move

def minimax(board, depth, is_maximizing):
    scores = {"X": -1, "O": 1, "tie": 0}

    winner = check_winner(board)
    if winner:
        return scores[winner]

    if is_maximizing:
        best_score = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

# Main game loop
def play_game():
    board = initialize_board()
    display_board(board)

    while not is_game_over(board):
        # Player's move
        player_turn = True
        move = player_move(board)
        board[move] = "X"
        display_board(board)

        if is_game_over(board):
            break

        # Computer's move
        player_turn = False
        move = computer_move(board)
        board[move] = "O"
        display_board(board)

    winner = check_winner(board)
    if winner:
        print(f"Player {winner} wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_game()
