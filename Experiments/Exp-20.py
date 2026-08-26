# Exp-20: Map Coloring using CSP

colors = ["Red", "Green", "Blue"]

# Map of neighboring regions
neighbors = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D"],
    "D": ["B", "C"]
}

assignment = {}


def is_valid(region, color):
    for neighbor in neighbors[region]:

        if neighbor in assignment:
            if assignment[neighbor] == color:
                return False

    return True


def solve():
    if len(assignment) == len(neighbors):
        return True

    # Select an unassigned region
    region = None

    for r in neighbors:
        if r not in assignment:
            region = r
            break

    for color in colors:

        if is_valid(region, color):

            assignment[region] = color

            if solve():
                return True

            del assignment[region]

    return False


if solve():
    print("Map Coloring Solution:\n")

    for region, color in assignment.items():
        print(region, "->", color)

else:
    print("No solution found.")