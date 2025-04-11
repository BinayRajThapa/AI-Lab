import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import numpy as np
import heapq

# Directions for movement (up, down, left, right)
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def heuristic(a, b):
    """Heuristic function for A* (Manhattan Distance)."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def bfs(grid, start, goal):
    """Breadth-First Search algorithm."""
    queue = [start]
    visited = set()
    visited.add(start)
    parent = {start: None}
    
    while queue:
        current = queue.pop(0)
        if current == goal:
            break
        for dx, dy in DIRECTIONS:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]):
                if neighbor not in visited and grid[neighbor[0]][neighbor[1]] == 0:
                    queue.append(neighbor)
                    visited.add(neighbor)
                    parent[neighbor] = current
    return reconstruct_path(parent, goal)

def dfs(grid, start, goal):
    """Depth-First Search algorithm."""
    stack = [start]
    visited = set()
    visited.add(start)
    parent = {start: None}
    
    while stack:
        current = stack.pop()
        if current == goal:
            break
        for dx, dy in DIRECTIONS:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]):
                if neighbor not in visited and grid[neighbor[0]][neighbor[1]] == 0:
                    stack.append(neighbor)
                    visited.add(neighbor)
                    parent[neighbor] = current
    return reconstruct_path(parent, goal)

def a_star(grid, start, goal):
    """A* Search algorithm."""
    open_set = []
    heapq.heappush(open_set, (0, start))
    parent = {start: None}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    
    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            break
        for dx, dy in DIRECTIONS:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                tentative_g_score = g_score[current] + 1
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    parent[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
    return reconstruct_path(parent, goal)

def reconstruct_path(parent, goal):
    """Reconstructs the path from the goal using the parent dictionary."""
    path = []
    while goal is not None:
        path.append(goal)
        goal = parent[goal]
    return path[::-1]

def visualize(grid, path, ax, title):
    """Visualize the grid and the path."""
    grid_copy = np.array(grid, dtype=float)
    for x, y in path:
        grid_copy[x][y] = 0.5
    grid_copy[start[0]][start[1]] = 0.2  # Start as light green
    grid_copy[goal[0]][goal[1]] = 0.8   # Goal as light blue
    
    ax.clear()
    ax.imshow(grid_copy, cmap='cool', origin='upper')
    ax.set_xticks(range(len(grid[0])))
    ax.set_yticks(range(len(grid)))
    ax.grid(which='major', color='black', linestyle='-', linewidth=0.5)
    ax.set_title(title)
    plt.draw()

# Grid and Start/Goal points
grid = [
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
]
start = (0, 0)
goal = (4, 4)

# Interactive Visualization
fig, ax = plt.subplots(figsize=(6, 6))
plt.subplots_adjust(bottom=0.2)

def run_bfs(event):
    path = bfs(grid, start, goal)
    visualize(grid, path, ax, "BFS Path")

def run_dfs(event):
    path = dfs(grid, start, goal)
    visualize(grid, path, ax, "DFS Path")

def run_a_star(event):
    path = a_star(grid, start, goal)
    visualize(grid, path, ax, "A* Path")

# Buttons
ax_bfs = plt.axes([0.1, 0.05, 0.2, 0.075])
ax_dfs = plt.axes([0.4, 0.05, 0.2, 0.075])
ax_a_star = plt.axes([0.7, 0.05, 0.2, 0.075])

btn_bfs = Button(ax_bfs, 'BFS')
btn_dfs = Button(ax_dfs, 'DFS')
btn_a_star = Button(ax_a_star, 'A*')

btn_bfs.on_clicked(run_bfs)
btn_dfs.on_clicked(run_dfs)
btn_a_star.on_clicked(run_a_star)

plt.show()
