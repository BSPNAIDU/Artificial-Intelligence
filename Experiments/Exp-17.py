# Exp-17: Depth First Search

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

visited = set()


def dfs(node):
    if node in visited:
        return

    print(node, end=" ")
    visited.add(node)

    for neighbour in graph[node]:
        dfs(neighbour)


print("DFS Traversal:")
dfs("A")