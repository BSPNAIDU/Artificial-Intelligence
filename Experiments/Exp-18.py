# Exp-18: Travelling Salesman Problem

from itertools import permutations

cities = ["A", "B", "C", "D"]

distance = {
    "A": {"A": 0, "B": 10, "C": 15, "D": 20},
    "B": {"A": 10, "B": 0, "C": 35, "D": 25},
    "C": {"A": 15, "B": 35, "C": 0, "D": 30},
    "D": {"A": 20, "B": 25, "C": 30, "D": 0}
}

start = "A"

remaining = [city for city in cities if city != start]

minimum_distance = float("inf")
best_route = None

for route in permutations(remaining):

    current_route = (start,) + route + (start,)

    total_distance = 0

    for i in range(len(current_route) - 1):
        total_distance += distance[
            current_route[i]
        ][
            current_route[i + 1]
        ]

    if total_distance < minimum_distance:
        minimum_distance = total_distance
        best_route = current_route


print("Best Route:", " -> ".join(best_route))
print("Minimum Distance:", minimum_distance)