from collections import deque
def bfs_shortest_path(graph, start, end):
    queue = deque([start])
    visited = set([start])
    parent = {start: None}
    
    while queue:
        current = queue.popleft()

        if current == end:
            break

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

path = []
cur = end
while cur is not None:
    path.append(cur)
    cur = parent.get(cur)

path.reverse()

if path[0] != start:
    return None

return path


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start = 'A'
end = 'F'

path = bfs_shortest_path(graph, start, end)

if path:
    print("Кратчайший путь:", " -> ".join(path))
else:
    print("Путь не найден")
