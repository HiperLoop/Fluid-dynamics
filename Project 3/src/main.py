from functions import plot_optimal_trajectory
import numpy as np

# Simulation parameters
t_min = 0 # Minimum time
t_max = 50 # Maximum time
max_computation_time = 1 # Maximum computation time in seconds
max_error = 1 # Maximum acceptable mean squared error

# Initial conditions
initial_pos = np.array([1, 1, 1]) # Initial position in phase space
initial_dt = 0.1 # Initial guess for dt
r = 10 # Rescaled reduced Rayleigh number as given in the problem statement

# Main execution
if __name__ == "__main__":
    # a) Simulate trajectory
    plot_optimal_trajectory(initial_pos, initial_dt, max_computation_time, max_error, t_min, t_max)

    # b) Plot different regimes
    # i)
    