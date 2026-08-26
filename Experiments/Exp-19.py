# Exp-19: A* Algorithm

import heapq

graph = {
    "A": [("B", 1), ("C", 3)],
    "B": [("D", 3), ("E", 1)],
    "C": [("F", 2)],
    "D": [("G", 2)],
    "E": [("G", 3)],
    "F": [("G", 1)],
    "G": []
}

# Heuristic values
h = {
    "A": 6,
    "B": 4,
    "C": 4,
    "D": 2,
    "E": 2,
    "F": 1,
    "G": 0
}


def a_star(start, goal):

    priority_queue = []
    heapq.heappush(priority_queue, (h[start], 0, start, [start]))

    visited = set()

    while priority_queue:

        f, g, node, path = heapq.heappop(priority_queue)

        if node == goal:
            return path, g

        if node in visited:
            continue

        visited.add(node)

        for neighbour, cost in graph[node]:

            new_g = g + cost
            new_f = new_g + h[neighbour]

            heapq.heappush(
                priority_queue,
                (new_f, new_g, neighbour, path + [neighbour])
            )

    return None, float("inf")


start = "A"
goal = "G"

path, cost = a_star(start, goal)

print("A* Path:", " -> ".join(path))
print("Total Cost:", cost)