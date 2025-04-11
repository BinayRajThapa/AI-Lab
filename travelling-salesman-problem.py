import numpy as np
import matplotlib.pyplot as plt
import random
import math

# Function to calculate the total distance of the tour
def calculate_distance(cities, tour):
    total_distance = 0
    for i in range(len(tour)):
        city_a = cities[tour[i]]
        city_b = cities[tour[(i + 1) % len(tour)]]
        total_distance += np.linalg.norm(city_a - city_b)
    return total_distance

# Function to generate a new neighbor (swap two cities in the tour)
def generate_neighbor(tour):
    new_tour = tour.copy()
    i, j = random.sample(range(len(tour)), 2)
    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
    return new_tour

# Simulated Annealing function
def simulated_annealing(cities, initial_temperature, cooling_rate, max_iterations):
    # Initial solution
    current_tour = list(range(len(cities)))
    random.shuffle(current_tour)
    current_distance = calculate_distance(cities, current_tour)

    best_tour = current_tour
    best_distance = current_distance

    temperature = initial_temperature

    distances = [current_distance]  # Track distances for visualization

    for _ in range(max_iterations):
        if temperature <= 0.1:  # Stop when the temperature is low
            break

        # Generate a neighbor solution
        new_tour = generate_neighbor(current_tour)
        new_distance = calculate_distance(cities, new_tour)

        # Accept or reject the new solution
        if new_distance < current_distance or random.random() < math.exp((current_distance - new_distance) / temperature):
            current_tour = new_tour
            current_distance = new_distance

            if current_distance < best_distance:
                best_tour = current_tour
                best_distance = current_distance

        # Cool down
        temperature *= cooling_rate
        distances.append(current_distance)

    return best_tour, best_distance, distances

# Function to visualize the TSP solution with clear coordinates
def visualize_tsp(cities, tour, title):
    plt.figure(figsize=(10, 6))

    # Plot connections between cities
    for i in range(len(tour)):
        city_a = cities[tour[i]]
        city_b = cities[tour[(i + 1) % len(tour)]]
        plt.plot([city_a[0], city_b[0]], [city_a[1], city_b[1]], 'b-')

    # Plot cities with labels
    for i, city in enumerate(cities):
        plt.scatter(city[0], city[1], color='red', s=100)
        plt.text(city[0] + 1, city[1] + 1, f"City {i}", fontsize=10, color='black')

    plt.title(title)
    plt.xlabel("X-coordinate")
    plt.ylabel("Y-coordinate")
    plt.grid()
    plt.show()

# Main function
def main():
    # Randomly generate cities
    np.random.seed(42)
    num_cities = 10
    cities = np.random.rand(num_cities, 2) * 100  # Random cities in a 100x100 grid

    # Simulated Annealing parameters
    initial_temperature = 1000
    cooling_rate = 0.995
    max_iterations = 1000

    # Solve TSP using Simulated Annealing
    best_tour, best_distance, distances = simulated_annealing(cities, initial_temperature, cooling_rate, max_iterations)

    # Visualize the results
    print(f"Best Distance: {best_distance:.2f}")
    print(f"Best Tour: {best_tour}")

    visualize_tsp(cities, best_tour, title=f"TSP Solution (Best Distance: {best_distance:.2f})")

    # Plot distance over iterations
    plt.figure(figsize=(10, 6))
    plt.plot(distances, label='Distance')
    plt.title("Distance Over Iterations")
    plt.xlabel("Iteration")
    plt.ylabel("Distance")
    plt.legend()
    plt.grid()
    plt.show()

# Run the main function
main()
