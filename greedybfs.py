from queue import PriorityQueue

# Graph representation
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

# Heuristic values
heuristic = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 5,
    'E': 3,
    'F': 1,
    'G': 0
}

def greedy_best_first_search(start, goal):
    visited = set()
    pq = PriorityQueue()

    # Insert start node with its heuristic value
    pq.put((heuristic[start], start))

    while not pq.empty():
        h, current = pq.get()

        if current in visited:
            continue

        print("Visited:", current)
        visited.add(current)

        if current == goal:
            print("\nGoal Reached!")
            return

        for neighbor in graph[current]:
            if neighbor not in visited:
                pq.put((heuristic[neighbor], neighbor))

# Run the algorithm
greedy_best_first_search('A', 'G')

