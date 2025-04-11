import numpy as np
import matplotlib.pyplot as plt

# Define the function to be optimized
def func(x):
    return -x**2 + 5*x + 4  # Example: f(x) = -x^2 + 5x + 4

# Hill Climbing Search Algorithm
def hill_climbing(func, start_point, step_size, max_iterations):
    current_solution = start_point
    current_value = func(current_solution)
    
    values = [current_value]  # Track values for visualization
    
    for _ in range(max_iterations):
        # Generate a neighboring solution
        neighbor_solution = current_solution + step_size
        
        # Evaluate the function at the neighbor
        neighbor_value = func(neighbor_solution)
        
        # If the neighbor is better, move to it
        if neighbor_value > current_value:
            current_solution = neighbor_solution
            current_value = neighbor_value
            
        values.append(current_value)  # Record the current value

    return current_solution, current_value, values

# Main function
def main():
    # Hill Climbing parameters
    start_point = 0  # Starting point (arbitrary)
    step_size = 0.1  # Step size
    max_iterations = 100  # Maximum iterations
    
    # Run Hill Climbing algorithm
    best_solution, best_value, values = hill_climbing(func, start_point, step_size, max_iterations)

    # Print results
    print(f"Best Solution: x = {best_solution}")
    print(f"Best Value: f(x) = {best_value}")

    # Plot the function and the optimization process
    x_vals = np.linspace(-10, 10, 400)
    y_vals = func(x_vals)

    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label='f(x) = -x^2 + 5x + 4', color='blue')
    plt.scatter(best_solution, best_value, color='red', label=f'Optimal Solution at x = {best_solution:.2f}')
    
    # Highlight the hill climbing path
    plt.plot(np.linspace(start_point, best_solution, len(values)), values, color='green', label='Hill Climbing Path')

    plt.title("Hill Climbing Optimization")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()

# Run the main function
main()
