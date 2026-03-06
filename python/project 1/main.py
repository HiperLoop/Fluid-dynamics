import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl

#circle constants
a = 1.12
z0 = (-0.1, 0.22)

def generate_cylinder(r, z0, n = 100):
    theta = np.linspace(0, 2 * np.pi, n)
    x = z0[0] +r * np.cos(theta)
    y = z0[1] + r * np.sin(theta)
    
    return x, y

def joukowski_transform(x, y, a):
    z = x + 1j * y
    w = z + a**2 / z
    return w.real, w.imag

def stream_function(x, y, x_vel, y_vel, a, gamma):
    U = x_vel - 1j * y_vel
    r = np.sqrt((x - z0[0])**2 + (y - z0[1])**2)
    theta = np.arctan2(y - z0[1], x - z0[0])
    value = U * r * np.sin(theta) * (1 - a**2 / r**2) - gamma / (2 * np.pi) * np.log(r)
    return value.real

def velocity_potential_function(x, y, x_vel, y_vel, a, gamma):
    U = x_vel - 1j * y_vel
    r = np.sqrt((x - z0[0])**2 + (y - z0[1])**2)
    theta = np.arctan2(y - z0[1], x - z0[0])
    value = U * r * np.cos(theta) * (1 + a**2 / r**2) + gamma / (2 * np.pi) * theta
    return value.real

def calculate_complex_potential(x, y, x_vel, y_vel, a, gamma):
    return velocity_potential_function(x, y, x_vel, y_vel, a, gamma) + 1j * stream_function(x, y, x_vel, y_vel, a, gamma)

def complex_potential(x, y, x_vel, y_vel, a, gamma):
    z = x + 1j * y
    U = x_vel - 1j * y_vel
    U_bar = x_vel + 1j * y_vel
    f = U*z + ((U_bar * a**2) / z) - (1j * (gamma / (2 * np.pi) * np.log(z)))
    return f.real, f.imag

def velocity_field(x, y, x_vel, y_vel, a, gamma):
    z = x + 1j * y
    U = x_vel - 1j * y_vel
    U_bar = x_vel + 1j * y_vel
    f_prime = U - ((U_bar * a**2) / z**2) - (1j * (gamma / (2 * np.pi) * (1/z)))
    return f_prime.real, f_prime.imag

air_pressure = 101325
air_density = 1.225
def pressure(x, y, x_vel, y_vel, a, gamma):
    d = 0.0001
    v = (calculate_complex_potential(x + d, y + d, x_vel, y_vel, a, gamma) - calculate_complex_potential(x, y, x_vel, y_vel, a, gamma)) / (np.sqrt(2) * d)
    v = np.sqrt(v.real**2 + v.imag**2)
    p = air_density * ((air_pressure / air_density) - v**2 / 2)
    return p

def show_plot(x, y, fig_lim = 2.5):
    fig, ax = plt.subplots()
    for i in range(len(x)):
        ax.scatter(x[i], y[i], 2)
    ax.set_xlim(-1 * fig_lim + z0[0], fig_lim + z0[0])
    ax.set_ylim(-1 * fig_lim + z0[1], fig_lim + z0[1])
    fig.set_size_inches(6, 6)
    fig.show()
    plt.pause(20)

def plotter_function(x_vel, y_vel, a, gamma, stream=True):
    return lambda x, y: stream_function(x, y, x_vel, y_vel, a, gamma) if stream else lambda x, y: velocity_potential_function(x, y, x_vel, y_vel, a, gamma)

def plotter(f, joukowski=False, draw_shape=False, fig_limit = 2.5, fig_offset = [0, 0], contours = 100, colourmap = 'winter'):
    theta = np.linspace(0, 2 * np.pi, 400)
    r = np.linspace(a, 3.5, 400)
    x = z0[0] + r * np.cos(theta)
    y = z0[1] + r * np.sin(theta)
    R, Theta = np.meshgrid(r,theta)
    X = z0[0] + R * np.cos(Theta)
    Y = z0[1] + R * np.sin(Theta)
    Z = f(X,Y)
    x, y = generate_cylinder(a, z0, n=1000)
    if joukowski:
        X, Y = joukowski_transform(X, Y, 1)
        x, y = joukowski_transform(x, y, 1)
    fig, ax = plt.subplots()
    cs = ax.contour(X,Y,Z, levels=contours, cmap=mpl.colormaps[colourmap])
    cs.cmap.set_over('red')
    cs.cmap.set_under('blue')
    cs.changed()
    ax.set_xlim(-1 * fig_limit + z0[0] + fig_offset[0], fig_limit + z0[0] + fig_offset[0])
    ax.set_ylim(-1 * fig_limit + z0[1] + fig_offset[1], fig_limit + z0[1] + fig_offset[1])
    if draw_shape:
        ax.plot(x, y, 2, color='red')
    fig.set_size_inches(6, 6)
    plt.show()

plotter(lambda x, y: pressure(x, y, 1, 0, a, -2.5), joukowski=True, draw_shape=True, fig_limit=2.5, contours=1000, colourmap='turbo')

def question_a():
    x, y = generate_cylinder(a, z0, n=1000)
    xj, yj = joukowski_transform(x, y, 1)
    show_plot([x, xj], [y, yj])

