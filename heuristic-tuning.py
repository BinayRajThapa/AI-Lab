import heapq

def a_star_with_heuristics(graph, start, goal, heuristic):
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
            return cost_so_far[current_node], path, len(visited)

        for neighbor, weight in graph[current_node]:
            new_cost = cost_so_far[current_node] + weight
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                f_cost = new_cost + heuristic[neighbor]
                heapq.heappush(pq, (f_cost, neighbor))

    return float("inf"), path, len(visited)  # If no path is found

def heuristic_tuning_analysis():
    graph = {
        "A": [("B", 1), ("C", 4)],
        "B": [("C", 2), ("D", 5)],
        "C": [("D", 1)],
        "D": []
    }

    # Admissible Heuristic (Underestimates or exact)
    admissible_heuristic = {
        "A": 7,
        "B": 6,
        "C": 2,
        "D": 0
    }

    # Consistent Heuristic (h(x) <= c(x, y) + h(y))
    consistent_heuristic = {
        "A": 6,
        "B": 4,
        "C": 2,
        "D": 0
    }

    start, goal = "A", "D"

    # Admissible Heuristic
    admissible_cost, admissible_path, admissible_nodes = a_star_with_heuristics(graph, start, goal, admissible_heuristic)

    # Consistent Heuristic
    consistent_cost, consistent_path, consistent_nodes = a_star_with_heuristics(graph, start, goal, consistent_heuristic)

    # Results
    print(f"Admissible Heuristic:")
    print(f"  Path Cost = {admissible_cost}, Path = {admissible_path}, Nodes Explored = {admissible_nodes}")
    print(f"Consistent Heuristic:")
    print(f"  Path Cost = {consistent_cost}, Path = {consistent_path}, Nodes Explored = {consistent_nodes}")

# Example usage
heuristic_tuning_analysis()
