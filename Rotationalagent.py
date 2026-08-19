# Simple Rational Agent Example

# Environment
grid = [
    ['R', ' ', 'T'],
    ['X', 'X', ' '],
    [' ', ' ', ' ']
]

# Robot position
row = 0
col = 0

# Target
target = (0,2)

print("Robot Starts at:", (row,col))

# Rational Agent Logic
while (row,col) != target:

    # Move Right if possible
    if col < 2 and grid[row][col+1] != 'X':
        col += 1
        print("Move Right")

    # Otherwise Move Down
    elif row < 2 and grid[row+1][col] != 'X':
        row += 1
        print("Move Down")

print("\nTarget Reached!")