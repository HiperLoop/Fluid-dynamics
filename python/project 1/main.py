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
    z = (x - z0[0]) + 1j * (y - z0[1])
    U = x_vel - 1j * y_vel
    U_bar = x_vel + 1j * y_vel
    f = U*z + ((U_bar * a**2) / z) - (1j * (gamma / (2 * np.pi) * np.log(z)))
    return f.real, f.imag

def velocity_field(x, y, x_vel, y_vel, a, gamma):
    """ d = 0.0001
    v = (calculate_complex_potential(x + d, y + d, x_vel, y_vel, a, gamma) - calculate_complex_potential(x, y, x_vel, y_vel, a, gamma)) / (np.sqrt(2) * d)
    v = np.sqrt(v.real**2 + v.imag**2)
    return v """
    z = (x - z0[0]) + 1j * (y - z0[1])
    U = x_vel - 1j * y_vel
    U_bar = x_vel + 1j * y_vel
    return U - (U_bar * (a**2 / z**2)) - ((1j * gamma) / (2 * np.pi * z))

def joukowski_velocity(v, x, y, b = 1):
    #x, y = joukowski_transform(x, y, 1)
    z = x + 1j * (y)
    return v / (1 - (b**2 / z**2))

air_pressure = 101325
air_density = 1.225
def pressure(x, y, x_vel, y_vel, a, gamma):
    d = 0.0001
    #v = (calculate_complex_potential(x + d, y + d, x_vel, y_vel, a, gamma) - calculate_complex_potential(x, y, x_vel, y_vel, a, gamma)) / (np.sqrt(2) * d)
    #v_squared = v.real**2 + v.imag**2
    v = np.abs(joukowski_velocity(velocity_field(x, y, x_vel, y_vel, a, gamma), x, y))
    p =  air_pressure - 0.5 *(air_density * v**2)
    return p

def force(x, y, x_vel, y_vel, a, gamma, joukowski=False):
    vel = velocity_field(x, y, x_vel, y_vel, a, gamma)
    if joukowski:
        vel = joukowski_velocity(vel, x, y)      
    z = x + 1j * y
    dz = (np.roll(z, -1) - np.roll(z, 1)) / 2
    return (1j * air_density) / 2 * np.sum((vel**2) * dz)

def print_force(x_vel, y_vel, a, gamma):
    print("cyllinder:")
    x, y = generate_cylinder(a, z0, n=1000)
    force_value = force(x, y, x_vel, y_vel, a, gamma)
    print(f"Fx: {force_value.real:f} N\nFy: {-force_value.imag:f} N\n")
    print("joukowski:")
    force_value = force(x, y, x_vel, y_vel, a, gamma, joukowski=True)
    print(f"Fx: {force_value.real:f} N\nFy: {-force_value.imag:f} N\n")

def show_scatter_plot(x, y, fig_lim = 2.5):
    fig, ax = plt.subplots()
    for i in range(len(x)):
        ax.scatter(x[i], y[i], 2)
    ax.set_xlim(-1 * fig_lim + z0[0], fig_lim + z0[0])
    ax.set_ylim(-1 * fig_lim + z0[1], fig_lim + z0[1])
    fig.set_size_inches(6, 6)
    fig.show()

def plotter_function(x_vel, y_vel, a, gamma, function = 'stream'):
    if function == 'stream':
        return lambda x, y: complex_potential(x, y, x_vel, y_vel, a, gamma)[1]
    if function == 'velocity_potential':
        return lambda x, y: complex_potential(x, y, x_vel, y_vel, a, gamma)[0]
    if function == 'pressure':
        return lambda x, y: pressure(x, y, x_vel, y_vel, a, gamma)
    if function == 'velocity':
        return lambda x, y: np.abs(velocity_field(x, y, x_vel, y_vel, a, gamma))
    if function == 'jvelocity':
        return lambda x, y: np.abs(joukowski_velocity(velocity_field(x, y, x_vel, y_vel, a, gamma), x, y))

def plotter(f, joukowski=False, draw_shape=False, fig_limit = 2.5, fig_offset = [0, 0], contours = 100, colourmap = 'winter', fill = False):
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
    if fill:
        cs = ax.contourf(X,Y,Z, levels=contours, cmap=mpl.colormaps[colourmap])
    else:
        cs = ax.contour(X,Y,Z, levels=contours, cmap=mpl.colormaps[colourmap])
    plt.colorbar(cs, ax=ax)
    cs.changed()
    ax.set_xlim(-1 * fig_limit + z0[0] + fig_offset[0], fig_limit + z0[0] + fig_offset[0])
    ax.set_ylim(-1 * fig_limit + z0[1] + fig_offset[1], fig_limit + z0[1] + fig_offset[1])
    if draw_shape:
        ax.plot(x, y, 2, color='red')
    fig.set_size_inches(6, 6)
    plt.show()

def question_a():
    x, y = generate_cylinder(a, z0, n=1000)
    xj, yj = joukowski_transform(x, y, 1)
    show_scatter_plot([x, xj], [y, yj])