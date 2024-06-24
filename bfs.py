from collections import deque

def bfs(graph, start, goal):
    queue = deque([(start, [])])

    while queue:
        current, path = queue.popleft()

        if current == goal:
            return path + [current]

        for neighbor in graph[current]:
            if neighbor not in path:
                queue.append((neighbor, path + [current]))

graph = {
    'A': ['B', 'C'],
    'B':[],
    'C': ['B', 'E', 'F'],
    'E': ['G'],
    
    'F': ['H','D'], 
    'G':['H'],
    'H':[], 
    'D':['E','G'], 
}

start_node = 'A'
goal_node = 'H'

result_path = bfs(graph, start_node, goal_node)
print("Chemin trouvé en BFS:", result_path)
