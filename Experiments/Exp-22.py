# Exp-22: Minimax Algorithm for Gaming

board = [" "] * 9


def display_board():
    print()
    for i in range(0, 9, 3):
        print(board[i], "|", board[i + 1], "|", board[i + 2])
        if i < 6:
            print("--+---+--")
    print()


def check_winner(player):
    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 4, 8),
        (2, 4, 6),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8)
    ]

    return any(
        board[a] == board[b] == board[c] == player
        for a, b, c in winning_positions
    )


def minimax(is_maximizing):
    if check_winner("O"):
        return 1

    if check_winner("X"):
        return -1

    if " " not in board:
        return 0

    if is_maximizing:
        best_score = -float("inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(best_score, score)

        return best_score

    else:
        best_score = float("inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(best_score, score)

        return best_score


def best_move():
    best_score = -float("inf")
    move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    return move


while True:
    display_board()

    # Human player
    position = int(input("Enter your position (1-9): ")) - 1

    if position < 0 or position > 8 or board[position] != " ":
        print("Invalid move.")
        continue

    board[position] = "X"

    if check_winner("X"):
        display_board()
        print("You win!")
        break

    if " " not in board:
        display_board()
        print("Draw!")
        break

    # AI player
    move = best_move()
    board[move] = "O"

    print("AI selected position:", move + 1)

    if check_winner("O"):
        display_board()
        print("AI wins!")
        break

    if " " not in board:
        display_board()
        print("Draw!")
        break