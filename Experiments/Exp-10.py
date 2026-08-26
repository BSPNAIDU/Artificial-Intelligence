# Exp-10: 8-Puzzle Problem using BFS

from collections import deque

def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

def get_neighbors(state):
    neighbors = []

    zero = state.index(0)
    row = zero // 3
    col = zero % 3

    moves = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_zero = new_row * 3 + new_col

            new_state = list(state)
            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]

            neighbors.append(tuple(new_state))

    return neighbors


def solve(start, goal):
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path

        for next_state in get_neighbors(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))

    return None


start = tuple(map(int, input(
    "Enter initial state (9 numbers, use 0 for blank): "
).split()))

goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

solution = solve(start, goal)

if solution:
    print("\nSolution found!")
    print("Number of moves:", len(solution) - 1)

    for state in solution:
        print_state(state)
else:
    print("No solution exists.")