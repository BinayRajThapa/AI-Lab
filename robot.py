from collections import deque
import matplotlib.pyplot as plt
import numpy as np

def bfs_path_planning(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    visited = set()
    queue = deque([(start, [start])])  # (current_position, path)

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == goal:  # Goal reached
            return path
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and grid[nx][ny] == 0:
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))
    
    return None  # No path found

def visualize_grid(grid, start, goal, path):
    grid = np.array(grid)
    plt.figure(figsize=(8, 8))

    # Create a visual grid
    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            if grid[x, y] == 1:  # Obstacle
                plt.fill_between([y, y + 1], x, x + 1, color="black")
            else:
                plt.fill_between([y, y + 1], x, x + 1, color="white", edgecolor="gray")

    # Highlight start and goal
    plt.scatter(start[1] + 0.5, start[0] + 0.5, color="green", s=200, label="Start")
    plt.scatter(goal[1] + 0.5, goal[0] + 0.5, color="red", s=200, label="Goal")

    # Highlight path
    if path:
        path_x = [p[1] + 0.5 for p in path]
        path_y = [p[0] + 0.5 for p in path]
        plt.plot(path_x, path_y, color="blue", linewidth=2, label="Path")

    plt.legend()
    plt.gca().invert_yaxis()
    plt.axis("off")
    plt.title("Robot Path Planning with BFS")
    plt.show()

# Example Grid
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)  # Starting point
goal = (4, 4)   # Goal point

# Run BFS Path Planning
path = bfs_path_planning(grid, start, goal)

if path:
    print("Path found:", path)
else:
    print("No path exists.")

# Visualize the result
visualize_grid(grid, start, goal, path)
