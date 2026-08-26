# Exp-12: Water Jug Problem

from collections import deque

capacity1 = 4
capacity2 = 3
target = 2


def get_next_states(state):
    x, y = state

    states = []

    # Fill jug 1
    states.append((capacity1, y))

    # Fill jug 2
    states.append((x, capacity2))

    # Empty jug 1
    states.append((0, y))

    # Empty jug 2
    states.append((x, 0))

    # Pour jug 1 -> jug 2
    amount = min(x, capacity2 - y)
    states.append((x - amount, y + amount))

    # Pour jug 2 -> jug 1
    amount = min(y, capacity1 - x)
    states.append((x + amount, y - amount))

    return states


def solve():
    queue = deque([((0, 0), [])])
    visited = {(0, 0)}

    while queue:
        state, path = queue.popleft()

        x, y = state

        if x == target or y == target:
            return path + [state]

        for next_state in get_next_states(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [state]))

    return None


solution = solve()

if solution:
    print("Solution:\n")

    for state in solution:
        print(state)
else:
    print("No solution found.")