N = 8

board = [[0 for _ in range(N)] for _ in range(N)]


def is_safe(row, col):
    # Check same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False

        i -= 1
        j -= 1

    # Check upper-right diagonal
    i = row - 1
    j = col + 1

    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False

        i -= 1
        j += 1

    return True


def solve_queens(row):
    # All 8 queens are placed
    if row == N:
        return True

    # Try every column in the current row
    for col in range(N):

        if is_safe(row, col):
            board[row][col] = 1

            # Place queen in next row
            if solve_queens(row + 1):
                return True

            # Backtracking
            board[row][col] = 0

    return False


def print_board():
    for row in board:
        for value in row:
            if value == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")

        print()


if solve_queens(0):
    print("Solution for 8-Queens Problem:\n")
    print_board()
else:
    print("No solution exists.")