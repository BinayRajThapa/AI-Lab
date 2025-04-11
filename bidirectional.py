import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def bidirectional_search(graph, start, goal):
    if start == goal:
        return [start]
    
    forward_queue = deque([start])
    backward_queue = deque([goal])
    forward_visited = {start: None}
    backward_visited = {goal: None}

    def reconstruct_path(forward_visited, backward_visited, intersect):
        path = []
        node = intersect
        while node is not None:
            path.append(node)
            node = forward_visited[node]
        path.reverse()
        node = backward_visited[intersect]
        while node is not None:
            path.append(node)
            node = backward_visited[node]
        return path

    while forward_queue and backward_queue:
        current_forward = forward_queue.popleft()
        for neighbor in graph[current_forward]:
            if neighbor not in forward_visited:
                forward_visited[neighbor] = current_forward
                forward_queue.append(neighbor)
                if neighbor in backward_visited:
                    return reconstruct_path(forward_visited, backward_visited, neighbor)
        
        current_backward = backward_queue.popleft()
        for neighbor in graph[current_backward]:
            if neighbor not in backward_visited:
                backward_visited[neighbor] = current_backward
                backward_queue.append(neighbor)
                if neighbor in forward_visited:
                    return reconstruct_path(forward_visited, backward_visited, neighbor)
    
    return None

def visualize_graph(graph, path):
    G = nx.Graph()
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    pos = nx.spring_layout(G)
    plt.figure(figsize=(10, 7))

    # Draw the graph
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightblue')
    nx.draw_networkx_edges(G, pos, edge_color='gray')
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

    # Highlight the shortest path
    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)
        nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='orange', node_size=700)

    plt.title("Graph with Shortest Path using Bidirectional Search", fontsize=14)
    plt.show()

# Example Graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D', 'F'],
    'F': ['E', 'G', 'H'],
    'G': ['F', 'I'],
    'H': ['F', 'I'],
    'I': ['H', 'G']
}

start = 'A'
goal = 'I'
path = bidirectional_search(graph, start, goal)

if path:
    print("Shortest Path:", " -> ".join(path))
else:
    print("No path exists between the nodes.")

visualize_graph(graph, path)
