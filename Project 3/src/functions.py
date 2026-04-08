import numpy as np
import matplotlib.pyplot as plt
import time

# Path to save figures
PATH = "Project 3/tex/figures/"

# Physical constants
g = 9.81 # Gravitational acceleration
nu = 1 # Kinematic viscosity
Kappa = 1 # Thermal diffusivity
Rho_0 = 1 # Reference density
C_v = 1 # Heat capacity
s = 10 # Prendtl number
b = 8/3 # Rayleigh number
theta_top = 1 # Temperature at H
theta_bot = 0 # Temperature at 0
theta_delta = theta_top - theta_bot # Temperature difference
wave_number = np.pi / np.sqrt(2) # Wave number

# ---Basic functions---
# Functions to convert between t and tau
def tau_from_t(t):
    return t * (wave_number**2 + np.pi**2)

def t_from_tau(tau):
    return tau / (wave_number**2 + np.pi**2)

# ---Euler forward method---
# Calculating the derivatives of the position in phase space
def dpos_dtau(pos, r):
    x, y, z = pos
    dx_dtau = s * (y - x)
    dy_dtau = r * x - y - x * z
    dz_dtau = x * y - b * z
    return np.array([dx_dtau, dy_dtau, dz_dtau])

# Euler forward method to calculate the next position in phase space
def euler_forward(pos, dtau, r):
    return pos + dpos_dtau(pos, r) * dtau

# ---Trajectory simulation---
# Simulate the trajectory in phase space for given initial position, time step, time range, and rescaled reduced Rayleigh number
def simulate_trajectory(initial_pos, dt, t_min, t_max, r):
    num_steps = int((t_max - t_min) / dt) # Number of time steps
    dtau = tau_from_t(dt);
    positions = np.zeros((num_steps, 3))
    positions[0] = initial_pos
    for i in range(1, num_steps):
        positions[i] = euler_forward(positions[i-1], dtau, r)
    return positions

# ---Determining dt---
# Function to calculate the mean squared error between two trajectories
def mean_squared_error(positions_dt1, positions_dt2):
    return np.mean((positions_dt1[:-1:2] - positions_dt2)**2)

# Function to find the lowest possible dt that meets the maximum computation time and error constraints
def find_optimal_dt(initial_pos, dt, max_comp_time, max_error, t_min, t_max, r):
    last_time_exceeded = True
    errors = []
    while True:
        start_time = time.time()
        # Simulate trajectories for dt and 2*dt to calculate the error
        trajectory_dt1 = simulate_trajectory(initial_pos, dt, t_min, t_max, r)
        duration = time.time() - start_time
        trajectory_dt2 = simulate_trajectory(initial_pos, 2 * dt, t_min, t_max, r)
        error = mean_squared_error(trajectory_dt1, trajectory_dt2)
        errors.append((dt, error))
        print(f"Computed trajectory for dt={dt} in {duration:.2f} seconds with Mean Squared Error: {error}")
        # Adjust dt based on computation time and error
        if duration > max_comp_time:
            dt *= duration / max_comp_time # Increase dt to reduce computation time
            if not last_time_exceeded:
                if error > max_error:
                    raise Exception("No suitable dt found within the maximum computation time and error constraints.")
                # Get dt with smallest error that meets the constraints
                optimal_dt = min((d for d, e in errors if e <= max_error), default=None)
                print(f"Optimal dt: {optimal_dt} with Mean Squared Error: {min((e for d, e in errors if e <= max_error), default=None)}")
                return optimal_dt
            last_time_exceeded = True
            continue # Skip this dt if it exceeds the maximum computation time
        last_time_exceeded = False
        dt *= duration / max_comp_time # Decrease dt to improve accuracy

# Plotting
def plot_trajectory(positions, save_fig=False, title='Trajectory in Phase Space'):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(positions[:, 0], positions[:, 1], positions[:, 2])
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.set_title(title)
    if save_fig:
        plt.savefig(PATH + title.replace(" ", "_") + '.png')
    plt.show()

# Function to simulate trajectory with optimised dt and plot it, with error handling for cases where no suitable dt is found
def plot_optimised_trajectory(initial_pos, initial_dt, max_computation_time, max_error, t_min, t_max, r, save_fig=False, title=None, use_initial_dt=False):
    # Error handling if no suitable dt is found
    if not use_initial_dt:
        try:
            dt = find_optimal_dt(initial_pos, initial_dt, max_computation_time, max_error, t_min, t_max, r)
        except Exception as e:
            print(f"Error finding optimal dt: {e}")
            return
    else:
        dt = initial_dt
    # Simulate trajectory with the optimal dt and plot it
    trajectory = simulate_trajectory(initial_pos, dt, t_min, t_max, r)
    if title is None:
        title = f"Trajectory with initial position= {initial_pos} and dt={dt:.5f}"
    else:
        title += f" and dt={dt:.7f}"
    plot_trajectory(trajectory, save_fig, title)