# Exp-11: 8-Queen Problem

N = 8

board = [-1] * N


def is_safe(row, col):
    for previous_row in range(row):
        previous_col = board[previous_row]

        if previous_col == col:
            return False

        if abs(previous_col - col) == abs(previous_row - row):
            return False

    return True


def solve(row):
    if row == N:
        return True

    for col in range(N):
        if is_safe(row, col):
            board[row] = col

            if solve(row + 1):
                return True

            board[row] = -1

    return False


if solve(0):
    print("8-Queen Solution:\n")

    for row in range(N):
        for col in range(N):
            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
else:
    print("No solution found.")