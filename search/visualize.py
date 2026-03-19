import matplotlib.pyplot as plt
import networkx as nx


def visualize_simple_graph(graph, path=None, title="Простой граф"):
    """
    Визуализация простого графа (задание 1)
    """
    G = nx.Graph()

    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    pos = nx.spring_layout(G, seed=42)

    plt.figure(figsize=(10, 8))

    nx.draw_networkx_nodes(
        G,
        pos,
        node_size=700,
        node_color="lightblue",
        edgecolors="black",
        linewidths=2,
    )

    nx.draw_networkx_edges(G, pos, width=2, alpha=0.7, edge_color="gray")

    if path and len(path) > 1:
        path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]

        nx.draw_networkx_nodes(
            G,
            pos,
            nodelist=path,
            node_size=800,
            node_color="red",
            edgecolors="black",
            linewidths=2,
        )

        nx.draw_networkx_edges(
            G, pos, edgelist=path_edges, width=4, alpha=0.9, edge_color="red"
        )

    nx.draw_networkx_labels(G, pos, font_size=14, font_weight="bold")

    plt.title(title, fontsize=16, fontweight="bold")
    plt.axis("off")
    plt.tight_layout()
    plt.show()


def visualize_romania_graph(graph, path=None, title="Карта дорог Румынии"):
    """
    Визуализация графа Румынии (задание 4)
    """
    G = nx.Graph()

    for city, connections in graph.items():
        for neighbor, weight in connections:
            G.add_edge(city, neighbor, weight=weight)

    pos = nx.spring_layout(G, seed=42, k=2, iterations=50)

    plt.figure(figsize=(14, 10))

    nx.draw_networkx_nodes(
        G,
        pos,
        node_size=700,
        node_color="lightblue",
        edgecolors="black",
        linewidths=2,
    )

    nx.draw_networkx_edges(G, pos, width=1.5, alpha=0.5, edge_color="gray")

    if path and len(path) > 1:
        path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]

        nx.draw_networkx_nodes(
            G,
            pos,
            nodelist=path,
            node_size=800,
            node_color="red",
            edgecolors="black",
            linewidths=2,
        )

        nx.draw_networkx_edges(
            G, pos, edgelist=path_edges, width=3, alpha=0.8, edge_color="red"
        )

    nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold")

    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

    plt.title(title, fontsize=16, fontweight="bold")
    plt.axis("off")
    plt.tight_layout()

    plt.savefig("romania_graph.png", dpi=300, bbox_inches="tight")
    print("\nГраф сохранен в файл 'romania_graph.png'")
    plt.show()


def visualize_path_in_graph(
    graph, path, graph_type="simple", title="Граф с найденным путем"
):
    """
    Универсальная функция визуализации графа с путем

    Параметры:
    - graph: словарь графа
    - path: список узлов пути
    - graph_type: "simple" или "romania"
    - title: заголовок графика
    """
    if graph_type == "simple":
        visualize_simple_graph(graph, path, title)
    elif graph_type == "romania":
        visualize_romania_graph(graph, path, title)
    else:
        print(f"Тип графа {graph_type} не поддерживается.")
