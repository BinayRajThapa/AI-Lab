import heapq
import networkx as nx
import matplotlib.pyplot as plt

def uniform_cost_search(graph, start, goal):
    pq = []  # Priority queue
    heapq.heappush(pq, (0, start))  # (cost, node)
    visited = set()
    cost_so_far = {start: 0}

    path = []  # To store the explored path

    while pq:
        current_cost, current_node = heapq.heappop(pq)

        if current_node in visited:
            continue
        visited.add(current_node)
        path.append(current_node)

        if current_node == goal:
            return current_cost, path

        for neighbor, weight in graph[current_node]:
            new_cost = current_cost + weight
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor))

    return float("inf"), path  # If no path is found

def a_star_search(graph, start, goal, heuristic):
    pq = []  # Priority queue
    heapq.heappush(pq, (0, start))  # (f(n), node)
    visited = set()
    cost_so_far = {start: 0}

    path = []  # To store the explored path

    while pq:
        current_cost, current_node = heapq.heappop(pq)

        if current_node in visited:
            continue
        visited.add(current_node)
        path.append(current_node)

        if current_node == goal:
            return cost_so_far[current_node], path

        for neighbor, weight in graph[current_node]:
            new_cost = cost_so_far[current_node] + weight
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                f_cost = new_cost + heuristic[neighbor]
                heapq.heappush(pq, (f_cost, neighbor))

    return float("inf"), path  # If no path is found

def visualize_graph(graph, ucs_path, astar_path, start, goal):
    """
    Visualizes the graph and the paths explored by UCS and A*.
    """
    G = nx.DiGraph()
    for node, edges in graph.items():
        for neighbor, weight in edges:
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G)

    # Draw the graph
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightblue")
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d["weight"] for u, v, d in G.edges(data=True)})

    # Highlight UCS path
    ucs_edges = [(ucs_path[i], ucs_path[i + 1]) for i in range(len(ucs_path) - 1)]
    nx.draw_networkx_edges(G, pos, edgelist=ucs_edges, edge_color="blue", width=2, label="UCS Path")

    # Highlight A* path
    astar_edges = [(astar_path[i], astar_path[i + 1]) for i in range(len(astar_path) - 1)]
    nx.draw_networkx_edges(G, pos, edgelist=astar_edges, edge_color="red", width=2, style="dashed", label="A* Path")

    plt.legend(loc="best")
    plt.title(f"Graph Visualization ({start} to {goal})")
    plt.show()

def compare_and_visualize():
    graph = {
        "A": [("B", 1), ("C", 4)],
        "B": [("C", 2), ("D", 5)],
        "C": [("D", 1)],
        "D": []
    }

    heuristic = {
        "A": 7,
        "B": 6,
        "C": 2,
        "D": 0
    }

    start, goal = "A", "D"

    # Uniform-Cost Search
    ucs_cost, ucs_path = uniform_cost_search(graph, start, goal)

    # A* Search
    astar_cost, astar_path = a_star_search(graph, start, goal, heuristic)

    # Display results
    print(f"Uniform-Cost Search: Path cost = {ucs_cost}, Path = {ucs_path}")
    print(f"A* Search: Path cost = {astar_cost}, Path = {astar_path}")

    # Visualize the graph and paths
    visualize_graph(graph, ucs_path, astar_path, start, goal)

# Example usage
compare_and_visualize()
