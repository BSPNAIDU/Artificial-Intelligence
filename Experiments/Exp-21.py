# Exp-21: Tic Tac Toe Game

board = [" "] * 9


def display_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()


def check_winner(player):
    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] == player:
            return True

    return False


def is_full():
    return " " not in board


current_player = "X"

while True:
    display_board()

    try:
        position = int(input(
            f"Player {current_player}, enter position (1-9): "
        )) - 1
    except ValueError:
        print("Enter a valid number.")
        continue

    if position < 0 or position > 8:
        print("Choose a position from 1 to 9.")
        continue

    if board[position] != " ":
        print("Position already occupied.")
        continue

    board[position] = current_player

    if check_winner(current_player):
        display_board()
        print("Player", current_player, "wins!")
        break

    if is_full():
        display_board()
        print("Game Draw!")
        break

    current_player = "O" if current_player == "X" else "X"
    