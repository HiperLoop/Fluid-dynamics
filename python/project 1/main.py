import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl

#circle constants
R = 1.12
z0 = -0.1 + 0.22j

def generate_cylinder(r, z0, n = 100):
    theta = np.linspace(0, 2 * np.pi, n)
    return r * np.exp(1j * theta) + z0

def joukowski_transform(z, a):
    w = z + a**2 / z
    return w

def complex_potential(z, U, a, gamma):
    z = (z - z0)
    U_bar = np.conjugate(U)
    f = U*z + ((U_bar * a**2) / z) - (1j * (gamma / (2 * np.pi) * np.log(z)))
    return f.real, f.imag

def velocity_field(z, U, a, gamma):
    z = (z - z0)
    U_bar = np.conjugate(U)
    return U - (U_bar * (a**2 / z**2)) - ((1j * gamma) / (2 * np.pi * z))

def joukowski_velocity(v, z, b = 1):
    return v / (1 - (b**2 / z**2))

air_pressure = 101325
air_density = 1.225
def pressure(z, U, a, gamma):
    v = np.abs(joukowski_velocity(velocity_field(z, U, a, gamma), z))
    p =  air_pressure - 0.5 *(air_density * v**2)
    return p

def force(z, U, a, gamma, joukowski=False):
    vel = velocity_field(z, U, a, gamma)
    if joukowski:
        vel = joukowski_velocity(vel, z)
        z = joukowski_transform(z, 1)
    dz = (np.roll(z, -1) - np.roll(z, 1)) / 2
    return (1j * air_density) / 2 * np.sum((vel**2) * dz)

def print_force(U, a, gamma):
    print("cyllinder:")
    z = generate_cylinder(a, z0, n=10000)
    force_value = force(z, U, a, gamma)
    print(f"Fx: {force_value.real:f} N/m\nFy: {-force_value.imag:f} N/m\n")
    print("joukowski:")
    force_value = force(z, U, a, gamma, joukowski=True)
    print(f"Fx: {force_value.real:f} N/m\nFy: {-force_value.imag:f} N/m\n")
    with open("LaTex/figures/g_force_values.txt", "a") as f:
        f.write("cyllinder:")
        f.write(f"\nFx: {force_value.real:f} N/m\nFy: {-force_value.imag:f} N/m\n")
        f.write("joukowski:")
        f.write(f"\nFx: {force_value.real:f} N/m\nFy: {-force_value.imag:f} N/m\n\n")

def show_scatter_plot(x, y, fig_lim = 2.5, save = False, filename = 'scatter.png'):
    fig, ax = plt.subplots()
    for i in range(len(x)):
        ax.scatter(x[i], y[i], 2)
    ax.set_xlim(-1 * fig_lim + z0.real, fig_lim + z0.real)
    ax.set_ylim(-1 * fig_lim + z0.imag, fig_lim + z0.imag)
    if save:
        PATH = 'LaTex/figures/'
        plt.savefig(PATH + filename)
    fig.show()

def plotter_function(U, a, gamma, function = 'stream'):
    if function == 'stream':
        return lambda z: complex_potential(z, U, a, gamma)[1]
    if function == 'velocity_potential':
        return lambda z: complex_potential(z, U, a, gamma)[0]
    if function == 'pressure':
        return lambda z: pressure(z, U, a, gamma)
    if function == 'velocity':
        return lambda z: np.abs(velocity_field(z, U, a, gamma))
    if function == 'jvelocity':
        return lambda z: np.abs(joukowski_velocity(velocity_field(z, U, a, gamma), z))

def plotter(f, joukowski=False, draw_shape=False, fig_limit = 2.5, fig_offset = [0, 0], contours = 100, colourmap = 'winter', fill = False, save = False, filename = 'figure.png'):
    theta = np.linspace(0, 2 * np.pi, 400)
    a = np.linspace(R, 3.5, 400)
    A, Theta = np.meshgrid(a,theta)
    X = z0.real + A * np.cos(Theta)
    Y = z0.imag + A * np.sin(Theta)
    Z = X + 1j * Y
    print(Z)
    val = f(Z)
    z = generate_cylinder(R, z0, n=1000)
    if joukowski:
        Z = joukowski_transform(Z, 1)
        z = joukowski_transform(z, 1)
    fig, ax = plt.subplots()
    if fill:
        cs = ax.contourf(Z.real, Z.imag, val, levels=contours, cmap=mpl.colormaps[colourmap])
    else:
        cs = ax.contour(Z.real, Z.imag, val, levels=contours, cmap=mpl.colormaps[colourmap])
    plt.colorbar(cs, ax=ax)
    cs.changed()
    ax.set_xlim(-1 * fig_limit + z0.real + fig_offset[0], fig_limit + z0.real + fig_offset[0])
    ax.set_ylim(-1 * fig_limit + z0.imag + fig_offset[1], fig_limit + z0.imag + fig_offset[1])
    if draw_shape:
        ax.plot(z.real, z.imag, 2, color='red')
    if save:
        PATH = 'LaTex/figures/'
        plt.savefig(PATH + filename)
    plt.show()

def question_a(save = False, filename = 'a_scatter.png'):
    z = generate_cylinder(R, z0, n=1000)
    zj = joukowski_transform(z, 1)
    show_scatter_plot([z.real, zj.real], [z.imag, zj.imag], save=save, filename=filename)