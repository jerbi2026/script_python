def dfs(graph, current, goal, path=[]):
    path = path + [current]

    if current == goal:
        return path

    for neighbor in graph[current]:
        if neighbor not in path:
            new_path = dfs(graph, neighbor, goal, path)
            if new_path:
                return new_path



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

start_node = 'H'
goal_node = 'F'


# Exemple d'utilisation
result_path_dfs = dfs(graph, start_node, goal_node)
print("Chemin trouvé en DFS:", result_path_dfs)
