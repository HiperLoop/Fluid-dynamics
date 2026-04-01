from functions import plot_optimised_trajectory, t_from_tau
import numpy as np
from random import randint

# a) Simulate trajectory with optimised dt
def a(save=False):
    # Initial paramters for a)
    t_min = 0 # Minimum time
    t_max = 50 # Maximum time
    max_computation_time = 2 # Maximum computation time in seconds
    max_error = 1 # Maximum acceptable mean squared error
    initial_dt = 0.1 # Initial guess for dt
    initial_pos = np.array([1, 1, 1]) # Initial position in phase space
    r = 10 # Rescaled reduced Rayleigh number as given in the problem statement

    # Show plot for a)
    plot_title = f"Plot of a)\nTrajectory with initial position= {initial_pos}, r = {r},"
    plot_optimised_trajectory(initial_pos, initial_dt, max_computation_time, max_error, t_min, t_max, r, save_fig=save, title=plot_title)


# b) Plot figures for i) to iv)
# i)
def b_i(save=False):
    # Initial paramters for b.i)
    tau_min = 0 # Minimum time
    tau_max = 50 # Maximum time
    max_computation_time = 2 # Maximum computation time in seconds
    max_error = 1 # Maximum acceptable mean squared error
    initial_dt = 0.1 # Initial guess for dt
    num_of_plots = 2
    random_bound = 20
    initial_positions = [np.array([randint(-random_bound, random_bound), randint(-random_bound, random_bound), randint(-random_bound, random_bound)]) for _ in range(num_of_plots)]
    r = 0.5 # Rescaled reduced Rayleigh number for b.i)
    t_min = t_from_tau(tau_min)
    t_max = t_from_tau(tau_max)

    # Show plots for b.i)
    for idx, pos in enumerate(initial_positions):
        plot_title = f"Plot of b.i) ({idx+1})\nTrajectory with initial position= {pos}, r = {r},"
        plot_optimised_trajectory(pos, initial_dt, max_computation_time, max_error, t_min, t_max, r, save_fig=save, title=plot_title)

# ii)
def b_ii(save=False):
    # Initial paramters for b.ii)
    tau_min = 0 # Minimum time
    tau_max = 50 # Maximum time
    max_computation_time = 2 # Maximum computation time in seconds
    max_error = 1 # Maximum acceptable mean squared error
    initial_dt = 0.1 # Initial guess for dt
    num_of_plots = 2
    random_bound = 20
    initial_positions = [np.array([randint(-random_bound, random_bound), randint(-random_bound, random_bound), randint(-random_bound, random_bound)]) for _ in range(num_of_plots)]
    r = 10 # Rescaled reduced Rayleigh number for b.ii)
    t_min = t_from_tau(tau_min)
    t_max = t_from_tau(tau_max)

    # Show plots for b.ii)
    for idx, pos in enumerate(initial_positions):
        plot_title = f"Plot of b.ii) ({idx+1})\nTrajectory with initial position= {pos}, r = {r},"
        plot_optimised_trajectory(pos, initial_dt, max_computation_time, max_error, t_min, t_max, r, save_fig=save, title=plot_title)

# iii)
def b_iii(save=False):
    # Initial parameters for b.iii)
    tau_min = 0 # Minimum time
    tau_max = 50 # Maximum time
    max_computation_time = 10 # Maximum computation time in seconds
    max_error = 120 # Increased maximum acceptable mean squared error for b.iii) due to increased complexity of the trajectories
    initial_dt = 0.1 # Initial guess for dt
    num_of_plots = 2
    random_bound = 20
    initial_positions = [np.array([randint(-random_bound, random_bound), randint(-random_bound, random_bound), randint(-random_bound, random_bound)]) for _ in range(num_of_plots)]
    r = 28 # Rescaled reduced Rayleigh number for b.iii)
    t_min = t_from_tau(tau_min)
    t_max = t_from_tau(tau_max)
    
    # Show plots for b.iii)
    for idx, pos in enumerate(initial_positions):
        plot_title = f"Plot of b.iii) ({idx+1})\nTrajectory with initial position= {pos}, r = {r},"
        plot_optimised_trajectory(pos, initial_dt, max_computation_time, max_error, t_min, t_max, r, save_fig=False, title=plot_title)

# iv)
def b_iv(save=False):
    # Initial parameters for b.iv)
    tau_min = 0 # Minimum time
    tau_max = 50 # Maximum time
    max_computation_time = 10 # Maximum computation time in seconds
    max_error = 120 # Increased maximum acceptable mean squared error for b.iv) due to increased complexity of the trajectories
    initial_dt = 0.1 # Initial guess for dt
    initial_pos = np.array([1, 1, 1])
    delta = 0.001
    delta_initial_pos = initial_pos + np.array([delta, 0, 0]) # Perturbation of the initial position
    initial_positions = [initial_pos, delta_initial_pos]
    r = 28 # Rescaled reduced Rayleigh number for b.iv)
    t_min = t_from_tau(tau_min)
    t_max = t_from_tau(tau_max)

    # Show plots for b.iv)
    for idx, pos in enumerate(initial_positions):
        plot_title = f"Plot of b.iv) ({idx+1})\nTrajectory with initial position= {pos}, r = {r},"
        plot_optimised_trajectory(pos, initial_dt, max_computation_time, max_error, t_min, t_max, r, save_fig=False, title=plot_title)

# Main execution
if __name__ == "__main__":
    # a)
    a(save=False)

    # b)
    b_i(save=False)
    b_ii(save=False)
    b_iii(save=False)
    b_iv(save=False)