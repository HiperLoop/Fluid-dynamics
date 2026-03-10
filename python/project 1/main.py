import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl

# Figure save path
PATH = 'LaTex/figures/'

#circle constants and air constants
R = 1.12
z0 = -0.1 + 0.22j
air_pressure = 101325
air_density = 1.225
joukowski_coefficient = 1

#Function that generates the points of a circle with radius r and center z0, with n points in total
def generate_cylinder(r, z0, n = 100):
    theta = np.linspace(0, 2 * np.pi, n)
    return r * np.exp(1j * theta) + z0

#Joukowski transform function, takes in a complex number z and a constant a, and returns the transformed complex number w
def joukowski_transform(z, a = joukowski_coefficient):
    w = z + a**2 / z
    return w

#Function to transofrm the velocity to the Joukowski plane, takes in a complex number z, a constant U, a constant a,
# and a constant gamma, and returns the velocity at that point in the Joukowski plane
def joukowski_velocity(v, z, a = joukowski_coefficient):
    return v / (1 - (a**2 / z**2))

#Function to calculate the complex potential, takes in a complex number z, a constant U, a constant a,
# and a constant gamma, and returns the real and imaginary parts of the complex potential
def complex_potential(z, U, a, gamma):
    z = (z - z0)
    U_bar = np.conjugate(U)
    f = U*z + ((U_bar * a**2) / z) - (1j * (gamma / (2 * np.pi) * np.log(z)))
    return f.real, f.imag

#Function to calculate the velocity, takes in a complex number z, a constant U, a constant a, and a constant gamma, and returns the velocity at that point
def velocity(z, U, a, gamma):
    z = (z - z0)
    U_bar = np.conjugate(U)
    return U - (U_bar * (a**2 / z**2)) - ((1j * gamma) / (2 * np.pi * z))

#Function to calculate the pressure, takes in a complex number z, a constant U, a constant a, and a constant gamma, and returns the pressure at that point
def pressure(z, U, a, gamma, joukowski=True):
    v = velocity(z, U, a, gamma)
    if joukowski:
        v = joukowski_velocity(v, z)
    v = np.abs(v)
    p =  air_pressure - 0.5 *(air_density * v**2)
    return p

#Function to calculate the force, takes in a complex number z, a constant U, a constant a, and a constant gamma, and returns the force at that point,
# if joukowski is true, it will calculate the force in the Joukowski plane, otherwise it will calculate the force in the original plane
def force(z, U, a, gamma, joukowski=False):
    vel = velocity(z, U, a, gamma)
    if joukowski:
        vel = joukowski_velocity(vel, z)
        z = joukowski_transform(z, 1)
    dz = (np.roll(z, -1) - np.roll(z, 1)) / 2
    return (1j * air_density) / 2 * np.sum((vel**2) * dz)

#Function to print the force values for both the cylinder and the Joukowski wing, takes in a constant U, a constant a, and a constant gamma,
# and prints the force values for both the cylinder and the Joukowski airfoil to the console, and also saves them to a text file in the LaTex/figures folder
def print_force(U, a, gamma, save = False):
    print("cyllinder:")
    z = generate_cylinder(a, z0, n=10000)
    force_value = force(z, U, a, gamma)
    print(f"Fx: {force_value.real:f} N/m\nFy: {-force_value.imag:f} N/m\n")
    print("joukowski:")
    force_value = force(z, U, a, gamma, joukowski=True)
    print(f"Fx: {force_value.real:f} N/m\nFy: {-force_value.imag:f} N/m\n")
    if save:
        with open(PATH + "g_force_values.txt", "a") as f:
            f.write("cyllinder:")
            f.write(f"\nFx: {force_value.real:f} N/m\nFy: {-force_value.imag:f} N/m\n")
            f.write("joukowski:")
            f.write(f"\nFx: {force_value.real:f} N/m\nFy: {-force_value.imag:f} N/m\n\n")

#Function to show a scatter plot of arrays x and y, with limits of fig_lim, and save the plot to a file if save is true,
# with the filename specified by filename
def show_scatter_plot(x, y, fig_lim = 2.5, save = False, filename = 'scatter.png'):
    fig, ax = plt.subplots()
    for i in range(len(x)):
        ax.scatter(x[i], y[i], 2)
    ax.set_xlim(-1 * fig_lim + z0.real, fig_lim + z0.real)
    ax.set_ylim(-1 * fig_lim + z0.imag, fig_lim + z0.imag)
    if save:
        plt.savefig(PATH + filename)
    fig.show()

#Helper function to choose which function to plot, takes in a constant U, a constant a, a constant gamma,
# and a string function, and returns the appropriate function to plot based on the value of function
def plotter_function(U, a, gamma, function = 'stream'):
    if function == 'stream':
        return lambda z: complex_potential(z, U, a, gamma)[1]
    if function == 'velocity_potential':
        return lambda z: complex_potential(z, U, a, gamma)[0]
    if function == 'pressure':
        return lambda z: pressure(z, U, a, gamma, joukowski=False)
    if function == 'jpressure':
        return lambda z: pressure(z, U, a, gamma)
    if function == 'velocity':
        return lambda z: np.abs(velocity(z, U, a, gamma))
    if function == 'jvelocity':
        return lambda z: np.abs(joukowski_velocity(velocity(z, U, a, gamma), z))

#Function to plot the function f, takes in a function f, a boolean joukowski to determine whether to plot in the Joukowski plane or not,
# a boolean draw_shape to determine whether to draw the shape of the cylinder//wing, a constant fig_limit to determine the limits of the plot,
# a list fig_offset to determine the offset of the plot, a constant contours to determine the number of contours to plot,
# a string colourmap to determine the colourmap to use for the contours, a boolean fill to determine whether to fill the contours or not,
# and a boolean save to determine whether to save the plot or not, with the filename specified by filename,
# and a string label to determine the label for the colourbar, and a string units to determine the units for the colourbar,
# and a boolean scale to determine whether to show the colourbar or not
def plotter(f, joukowski=False, draw_shape=False, fig_limit = 2.5, fig_offset = [0, 0], contours = 100, colourmap = 'winter', label = '', units = '', scale = True, fill = False, save = False, filename = 'figure.png'):
    theta = np.linspace(0, 2 * np.pi, 400)
    a = np.linspace(R, 3.5, 400)
    A, Theta = np.meshgrid(a,theta)
    X = z0.real + A * np.cos(Theta)
    Y = z0.imag + A * np.sin(Theta)
    Z = X + 1j * Y
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
    if scale:
        plt.colorbar(cs, ax=ax, label=f'{label} [{units}]')
    cs.changed()
    ax.set_xlim(-1 * fig_limit + z0.real + fig_offset[0], fig_limit + z0.real + fig_offset[0])
    ax.set_ylim(-1 * fig_limit + z0.imag + fig_offset[1], fig_limit + z0.imag + fig_offset[1])
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlabel('x coordinate')
    ax.set_ylabel('y coordinate')
    ax.legend()
    if draw_shape:
        ax.plot(z.real, z.imag, 2, color='red')
    if save:
        plt.savefig(PATH + filename)
    plt.show()

#Function to plot the scatter plot of the points of the cylinder and the Joukowski transform of those points,
# takes in a boolean save to determine whether to save the plot or not, with the filename specified by filename
def question_a(save = False, filename = 'a_scatter.png'):
    z = generate_cylinder(R, z0, n=1000)
    zj = joukowski_transform(z, 1)
    show_scatter_plot([z.real, zj.real], [z.imag, zj.imag], save=save, filename=filename)