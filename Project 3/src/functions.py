import numpy as np
import matplotlib.pyplot as plt

# Physical constants
g = 9.81 # Gravitational acceleration
H = 1 # Leyer thickness
nu = 1 # Kinematic viscosity
Kappa = 1 # Thermal diffusivity
Rho_0 = 1 # Reference density
C_v = 1 # Heat capacity
s = 10 # Prendtl number
b = 8/3 # Rayleigh number
theta_top = 1 # Temperature at H
theta_bot = 0 # Temperature at 0
theta_delta = theta_top - theta_bot # Temperature difference
wave_number = 1 # Wave number
raileigh_number = g * theta_delta * H**3 / (nu * Kappa) # Rayleigh number
r = raileigh_number * wave_number**2 / (wave_number**2 + np.pi**2)**3 # Rescaled reduced Rayleigh number

# Initial conditions


# Basic functions
def tau_from_t(t):
    return t * (wave_number**2 + np.pi**2)

def t_from_tau(tau):
    return tau / (wave_number**2 + np.pi**2)

# Euler forward method
def dpos_dtau(pos):
    x, y, z = pos
    dx_dtau = s * (y - x)
    dy_dtau = r * x - y - x * z
    dz_dtau = x * y - b * z
    return np.array([dx_dtau, dy_dtau, dz_dtau])

def euler_forward(pos, dtau):
    return pos + dpos_dtau(pos) * dtau

