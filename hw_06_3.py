import networkx as nx
import matplotlib.pyplot as plt

# Створення вагового графа
G = nx.Graph()

# Додавання вершин (співробітників)
employees = ["Анна", "Борис", "Віра", "Ганна", "Дмитро", "Євген"]
G.add_nodes_from(employees)

# Додавання ребер з вагами
relations = [("Анна", "Борис", 2), ("Анна", "Віра", 3), ("Борис", "Дмитро", 4), 
             ("Віра", "Ганна", 1), ("Ганна", "Дмитро", 2), ("Дмитро", "Євген", 5), ("Євген", "Анна", 1)]
G.add_weighted_edges_from(relations)

# Візуалізація графа
pos = nx.spring_layout(G)  # Розташування вершин за допомогою spring layout
plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, edge_color='#f50057', width=2, font_size=15, font_weight='bold')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Ваговий граф співробітників")
plt.show()

# Знаходження найкоротших шляхів від кожної вершини до всіх інших за допомогою алгоритму Дейкстри
all_shortest_paths = dict(nx.all_pairs_dijkstra_path(G))
all_shortest_path_lengths = dict(nx.all_pairs_dijkstra_path_length(G))

print("Найкоротші шляхи між усіма вершинами:")
for source, paths in all_shortest_paths.items():
    for target, path in paths.items():
        print(f"Найкоротший шлях від {source} до {target}: {path}")

print("\nДовжини найкоротших шляхів:")
for source, lengths in all_shortest_path_lengths.items():
    for target, length in lengths.items():
        print(f"Довжина шляху від {source} до {target}: {length}")