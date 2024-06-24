import heapq


def astar(graph, start, goal, heuristic):
    # La file de priorité utilise un tuple (coût total, état)
    open_set = [(0, start)]
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    while open_set:
        current_cost, current_node = heapq.heappop(open_set)

        if current_node == goal:
            path = reconstruct_path(came_from, start, goal)
            return path

        for neighbor, cost in graph[current_node]:
            tentative_g_score = g_score[current_node] + cost

            if tentative_g_score < g_score[neighbor]:
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score, neighbor))
                came_from[neighbor] = current_node

    return None  # Pas de chemin trouvé

def reconstruct_path(came_from, start, goal):
    path = [goal]
    current = goal
    while current != start:
        current = came_from[current]
        path.append(current)
    return list(reversed(path))

# Exemple d'utilisation
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('A', 1), ('D', 2)],
    'C': [('A', 3), ('D', 1)],
    'D': [('B', 2), ('C', 1)]
}

heuristic = {'A': 4, 'B': 2, 'C': 1, 'D': 0}  # Exemple d'une fonction heuristique admissible

start_node = 'B'
goal_node = 'C'

result_path = astar(graph, start_node, goal_node, heuristic.get)
print("Chemin trouvé en A*:", result_path)
