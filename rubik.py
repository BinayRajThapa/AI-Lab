from queue import PriorityQueue

# Define the goal state
goal_state = (
    "W", "W", "W", "W",  # Top
    "O", "O", "O", "O",  # Front
    "G", "G", "G", "G",  # Right
    "R", "R", "R", "R",  # Back
    "B", "B", "B", "B",  # Left
    "Y", "Y", "Y", "Y"   # Bottom
)

# Example heuristic: Number of misplaced tiles
def heuristic(state):
    return sum(1 for i in range(len(state)) if state[i] != goal_state[i])

# Apply a move to the state
def apply_move(state, move):
    # Moves are simple rotations (e.g., U, F, R for top, front, right)
    new_state = list(state)
    if move == "U":
        # Rotate the top layer clockwise
        new_state[0], new_state[1], new_state[2], new_state[3] = state[1], state[2], state[3], state[0]
    elif move == "F":
        # Rotate the front layer clockwise
        new_state[4], new_state[5], new_state[6], new_state[7] = state[5], state[6], state[7], state[4]
    elif move == "R":
        # Rotate the right layer clockwise
        new_state[8], new_state[9], new_state[10], new_state[11] = state[9], state[10], state[11], state[8]
    # Add more moves as necessary (L, B, D, etc.)
    return tuple(new_state)

# A* algorithm
def rubiks_solver(start_state):
    open_set = PriorityQueue()
    open_set.put((0, start_state, []))
    visited = set()

    while not open_set.empty():
        _, current_state, path = open_set.get()

        if current_state in visited:
            continue
        visited.add(current_state)

        # Check if the goal is reached
        if current_state == goal_state:
            return path

        # Generate possible moves
        for move in ["U", "F", "R"]:  # Add more moves as necessary
            next_state = apply_move(current_state, move)
            if next_state not in visited:
                cost = len(path) + 1 + heuristic(next_state)
                open_set.put((cost, next_state, path + [move]))
    
    return None  # No solution found

# Example scrambled state (for 2x2 cube representation)
start_state = (
    "W", "W", "G", "G",
    "O", "B", "O", "B",
    "R", "Y", "R", "Y",
    "B", "O", "B", "O",
    "G", "R", "G", "R",
    "Y", "Y", "W", "W"
)

# Solve the Rubik's Cube
solution = rubiks_solver(start_state)

if solution:
    print("Solution found:", " -> ".join(solution))
else:
    print("No solution found.")
