import numpy as np
from matplotlib import pyplot as plt

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

def show_plot(x, y):
    fig, ax = plt.subplots()
    for i in range(len(x)):
        ax.scatter(x[i], y[i], 2)
    fig.show()
    plt.pause(20)

def plotter(f, c):
    theta = np.linspace(0, 2 * np.pi, 400)
    r = np.linspace(a, 3, 400)
    #x = np.linspace(-2, 2, 100)
    #y = np.linspace(-2, 2, 100)
    x = z0[0] + r * np.cos(theta)
    y = z0[1] + r * np.sin(theta)
    R, Theta = np.meshgrid(r,theta)
    X = z0[0] + R * np.cos(Theta)
    Y = z0[1] + R * np.sin(Theta)
    Z = f(X,Y)
    x, y = generate_cylinder(a, z0, n=1000)
    fig, ax = plt.subplots()
    #ax.scatter(X, Y, 2)
    cs = ax.contour(X,Y,Z, levels=40)
    ax.set_xlim(-2 + z0[0], 2 + z0[0])
    ax.set_ylim(-2 + z0[1], 2 + z0[1])
    ax.scatter(x, y, 2)
    fig.set_size_inches(6, 6)
    plt.show()

c = 0
a = 1.12
z0 = (-0.1, 0.22)
plotter(lambda x, y: stream_function(x, y, 1, 0, a, -3), c)
plotter(lambda x, y: velocity_potential_function(x, y, 1, 0, a, -3), c)

x, y = generate_cylinder(a, z0, n=1000)
xj, yj = joukowski_transform(x, y, 1)
#show_plot([x, xj], [y, yj])