# Breadth First Search (BFS)

from collections import deque

# Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

# BFS Function
def bfs(graph, start):
    visited = set()          # Stores visited nodes
    queue = deque([start])   # Queue for BFS

    print("BFS Traversal:")

    while queue:
        node = queue.popleft()   # Remove first element

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            # Add neighbours to queue
            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)

# Function Call
bfs(graph, 'A')