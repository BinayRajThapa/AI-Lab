import random
import matplotlib.pyplot as plt

# Define moves: Up, Down, Left, Right
MOVES = [(0, 1), (0, -1), (-1, 0), (1, 0)]

def generate_initial_state(length):
    """
    Generates an initial straight-line protein configuration.
    """
    return [(i, 0) for i in range(length)]

def calculate_energy(state, sequence):
    """
    Calculates the energy of a given state based on hydrophobic (H) contacts.
    """
    energy = 0
    for i in range(len(sequence)):
        if sequence[i] == "H":
            for j in range(i + 1, len(sequence)):
                if sequence[j] == "H" and abs(state[i][0] - state[j][0]) + abs(state[i][1] - state[j][1]) == 1:
                    energy -= 1
    return energy

def get_neighbors(state):
    """
    Generates neighboring states by trying all valid moves.
    """
    neighbors = []
    for i in range(1, len(state)):
        for move in MOVES:
            new_position = (state[i][0] + move[0], state[i][1] + move[1])
            if new_position not in state:  # Ensure no overlap
                new_state = state[:]
                new_state[i] = new_position
                neighbors.append(new_state)
    return neighbors

def hill_climbing(sequence):
    """
    Hill Climbing algorithm for protein folding.
    """
    current_state = generate_initial_state(len(sequence))
    current_energy = calculate_energy(current_state, sequence)

    while True:
        neighbors = get_neighbors(current_state)
        best_neighbor = None
        best_energy = current_energy

        for neighbor in neighbors:
            energy = calculate_energy(neighbor, sequence)
            if energy < best_energy:  # Looking for lower energy
                best_neighbor = neighbor
                best_energy = energy

        if best_energy < current_energy:
            current_state = best_neighbor
            current_energy = best_energy
        else:
            break

    return current_state, current_energy

def visualize_protein(state, sequence):
    """
    Visualizes the protein folding on a 2D lattice.
    """
    x, y = zip(*state)
    colors = ["blue" if res == "H" else "red" for res in sequence]

    plt.figure(figsize=(6, 6))
    plt.plot(x, y, marker="o", markersize=10, linestyle="-", color="black", zorder=1)
    plt.scatter(x, y, c=colors, s=200, zorder=2)
    for i, (xi, yi) in enumerate(state):
        plt.text(xi, yi, sequence[i], color="white", fontsize=8, ha="center", va="center")
    plt.grid(True)
    plt.title("Protein Folding")
    plt.show()

# Example protein sequence
sequence = "HHPHHHPPHPPH"

# Solve the protein folding problem
final_state, final_energy = hill_climbing(sequence)

# Display results
print("Final Energy:", final_energy)
print("Final State:", final_state)
visualize_protein(final_state, sequence)
