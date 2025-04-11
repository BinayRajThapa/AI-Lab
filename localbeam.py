import random
import numpy as np

def count_conflicts(state):
    """Calculate the number of conflicts for a given state."""
    conflicts = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def generate_successors(state):
    """Generate all possible successors of the current state."""
    successors = []
    n = len(state)
    for col in range(n):
        for row in range(n):
            if state[col] != row:
                new_state = list(state)
                new_state[col] = row
                successors.append(new_state)
    return successors

def local_beam_search(n, k, max_iterations):
    """
    Perform Local Beam Search to solve the N-Queens Problem.
    
    Args:
        n: Size of the chessboard (N x N).
        k: Number of states to maintain at each step.
        max_iterations: Maximum number of iterations to perform.
    
    Returns:
        Solution state if found, else None.
    """
    # Initialize k random states
    states = [random.sample(range(n), n) for _ in range(k)]
    
    for iteration in range(max_iterations):
        # Calculate conflicts for all states
        state_conflicts = [(state, count_conflicts(state)) for state in states]
        
        # Sort states by number of conflicts (ascending order)
        state_conflicts.sort(key=lambda x: x[1])
        
        # If a solution is found (conflicts = 0), return it
        if state_conflicts[0][1] == 0:
            return state_conflicts[0][0]
        
        # Keep the k best states
        states = [state for state, _ in state_conflicts[:k]]
        
        # Generate all successors of the k best states
        successors = []
        for state in states:
            successors.extend(generate_successors(state))
        
        # Select the k best successors based on conflicts
        successor_conflicts = [(state, count_conflicts(state)) for state in successors]
        successor_conflicts.sort(key=lambda x: x[1])
        states = [state for state, _ in successor_conflicts[:k]]
    
    # If no solution is found within max_iterations, return None
    return None

def visualize_solution(state):
    """Visualize the N-Queens solution on a chessboard."""
    if not state:
        print("No solution found.")
        return
    
    n = len(state)
    board = np.zeros((n, n), dtype=int)
    for col, row in enumerate(state):
        board[row][col] = 1
    
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))

# Main function
def main():
    n = 8  # Size of the chessboard
    k = 3  # Number of states to maintain
    max_iterations = 100  # Maximum iterations
    
    solution = local_beam_search(n, k, max_iterations)
    if solution:
        print("Solution found:")
        print(solution)
        visualize_solution(solution)
    else:
        print("No solution found within the given iterations.")

# Run the main function
main()
