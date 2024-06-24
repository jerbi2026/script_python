def iddfs(graph, start, goal, max_depth):
    for depth in range(max_depth):
        result = dls(graph, start, goal, depth)
        if result:
            return result

def dls(graph, current, goal, depth, path=[]):
    path = path + [current]

    if depth == 0 and current == goal:
        return path

    if depth > 0:
        for neighbor in graph[current]:
            if neighbor not in path:
                new_path = dls(graph, neighbor, goal, depth - 1, path)
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

start_node = 'E'
goal_node = ' H'

# Exemple d'utilisation
max_depth = 4
result_path_iddfs = iddfs(graph, start_node, goal_node, max_depth)
print("Chemin trouvé en IDDFS:", result_path_iddfs)
