import matplotlib.pyplot as plt
import networkx as nx

def draw_graph(graph, deadlock):
    G = nx.DiGraph()
    for u in graph:
        for v in graph[u]:
            G.add_edge(u, v)

    color_map = ['red' if n.startswith('P') else 'skyblue' for n in G.nodes()]
    plt.figure(figsize=(8, 6))
    nx.draw(G, with_labels=True, node_color=color_map, node_size=1500, font_size=12)
    title = "Deadlock Detected!" if deadlock else "No Deadlock Detected"
    plt.title(title)
    plt.show()
