# Exp-14: Missionaries and Cannibals Problem

from collections import deque

# State:
# (missionaries_left, cannibals_left, boat_side)
# boat_side = 0 means left
# boat_side = 1 means right

initial = (3, 3, 0)
goal = (0, 0, 1)


def is_valid(state):
    m_left, c_left, boat = state

    m_right = 3 - m_left
    c_right = 3 - c_left

    if not (0 <= m_left <= 3 and 0 <= c_left <= 3):
        return False

    if m_left > 0 and m_left < c_left:
        return False

    if m_right > 0 and m_right < c_right:
        return False

    return True


def get_neighbors(state):
    m, c, boat = state

    moves = [
        (1, 0),
        (2, 0),
        (0, 1),
        (0, 2),
        (1, 1)
    ]

    result = []

    for missionaries, cannibals in moves:

        if boat == 0:
            new_state = (
                m - missionaries,
                c - cannibals,
                1
            )
        else:
            new_state = (
                m + missionaries,
                c + cannibals,
                0
            )

        if is_valid(new_state):
            result.append(new_state)

    return result


def solve():
    queue = deque([(initial, [initial])])
    visited = {initial}

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path

        for next_state in get_neighbors(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))

    return None


solution = solve()

if solution:
    print("Solution:\n")

    for state in solution:
        print(state)
else:
    print("No solution found.")