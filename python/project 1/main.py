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
    for i in range(len(x)):
        ax.scatter(x[i], y[i], 2)
    fig.show()
    plt.pause(20)

def stream_function():
    

x, y = generate_cylinder(1.12, (-0.1, 0.22), n=1000)
xj, yj = joukowski_transform(x, y, 1)
show_plot([x, xj], [y, yj])