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

def show_plot(x, y):
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    fig.show()
    plt.pause(20)

x, y = generate_cylinder(1, (0, 0), n=1000)
#x, y = joukowski_transform(x, y, 1)
show_plot(x, y)