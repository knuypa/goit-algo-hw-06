import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()
employees = ["Анна", "Борис", "Віра", "Ганна", "Дмитро", "Євген"]
relations = [("Анна", "Борис"), ("Анна", "Віра"), ("Борис", "Дмитро"), 
             ("Віра", "Ганна"), ("Ганна", "Дмитро"), ("Дмитро", "Євген"), ("Євген", "Анна")]
G.add_nodes_from(employees)
G.add_edges_from(relations)

# Вибір початкової та кінцевої вершини
start_vertex = "Анна"
end_vertex = "Дмитро"

# BFS
def bfs_path(graph, start, goal):
    visited = []
    queue = [[start]]
    
    if start == goal:
        return queue[0]
    
    while queue:
        path = queue.pop(0)
        node = path[-1]
        
        if node not in visited:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                
                if neighbour == goal:
                    return new_path
            visited.append(node)
    return None

# DFS
def dfs_path(graph, start, goal, path=None):
    if path is None:
        path = [start]
    
    if start == goal:
        return path
    
    for neighbour in graph[start]:
        if neighbour not in path:
            new_path = dfs_path(graph, neighbour, goal, path + [neighbour])
            if new_path:
                return new_path
    return None

# Знаходження шляхів
path_bfs = bfs_path(G, start_vertex, end_vertex)
path_dfs = dfs_path(G, start_vertex, end_vertex)

print("BFS path:", path_bfs)
print("DFS path:", path_dfs)

# Порівняння результатів
plt.figure(figsize=(12, 5))

plt.subplot(121)
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='#f50057', node_size=3000, font_size=15, font_weight='bold')
plt.title("BFS Path")

plt.subplot(122)
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='#f50057', node_size=3000, font_size=15, font_weight='bold')
plt.title("DFS Path")

plt.show()