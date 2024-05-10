try:
    import networkx as nx
    import matplotlib.pyplot as plt
except ImportError:
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "networkx"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "matplotlib"])
    import networkx as nx
    import matplotlib.pyplot as plt

# Створення порожнього графа
G = nx.Graph()

# Додавання вершин (співробітників)
employees = ["Анна", "Борис", "Віра", "Ганна", "Дмитро", "Євген"]
G.add_nodes_from(employees)

# Додавання ребер (робочі взаємини)
relations = [("Анна", "Борис"), ("Анна", "Віра"), ("Борис", "Дмитро"), 
             ("Віра", "Ганна"), ("Ганна", "Дмитро"), ("Дмитро", "Євген"), ("Євген", "Анна")]
G.add_edges_from(relations)

# Візуалізація графа
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)  # Розташування вершин за допомогою spring layout
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='#f50057', node_size=3000, font_size=15, font_weight='bold')
plt.title("Соціальна мережа офісу")
plt.show()

# Основні характеристики графа
number_of_nodes = G.number_of_nodes()
number_of_edges = G.number_of_edges()
degrees = G.degree()

print("Кількість вершин:", number_of_nodes)
print("Кількість ребер:", number_of_edges)
print("Ступені вершин:", dict(degrees))
