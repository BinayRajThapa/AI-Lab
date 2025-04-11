import networkx as nx
import matplotlib.pyplot as plt

def greedy_graph_coloring(graph):
    """
    Greedy algorithm for graph coloring.
    """
    # Dictionary to store the color assigned to each node
    coloring = {}
    
    # Iterate through nodes in graph order
    for node in graph.nodes():
        # Find colors used by adjacent nodes
        used_colors = {coloring[neighbor] for neighbor in graph.neighbors(node) if neighbor in coloring}
        
        # Assign the smallest available color
        for color in range(len(graph)):
            if color not in used_colors:
                coloring[node] = color
                break
    
    return coloring

def visualize_colored_graph(graph, coloring):
    """
    Visualizes the graph with nodes colored according to the coloring result.
    """
    plt.figure(figsize=(8, 6))

    # Get the colors for each node
    node_colors = [coloring[node] for node in graph.nodes()]
    
    # Draw the graph
    nx.draw(
        graph,
        with_labels=True,
        node_color=node_colors,
        cmap=plt.cm.rainbow,
        node_size=800,
        font_weight="bold",
        font_color="white",
    )
    plt.title("Graph Coloring Result")
    plt.show()

# Example Graph
edges = [
    (0, 1), (0, 2), (1, 2), (1, 3),
    (2, 4), (3, 4), (4, 5), (3, 5)
]

# Create a graph using NetworkX
G = nx.Graph()
G.add_edges_from(edges)

# Apply the greedy graph coloring algorithm
coloring_result = greedy_graph_coloring(G)

# Print and visualize the result
print("Coloring Result:", coloring_result)
visualize_colored_graph(G, coloring_result)
