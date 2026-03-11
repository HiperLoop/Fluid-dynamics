import numpy as np
from matplotlib import pyplot as plt 

p_ground = 100000
g = 9.81
R = 8.41
M = 0.029
A = -10
x_0 = 5
v_0 = 50
max_t = 10000
step_n = 10000
dt = max_t / step_n

def temp(z):
    return 288 - (0.7 * z / 100)

""" def temp(z):
    return 288 """

def dp(z_p):
    return (-1 * g * z_p[1] * M)/(R * temp(z_p[0]))

initial_conditions = [p_ground]

equation_set = [dp]
dependency_set = [[0]]

""" def dx(v):
    return v[0]

def dv(x):
    return A

initial_conditions = [v_0, x_0]

equation_set = [dv, dx]
dependency_set = [[], [0]] """

def solve(dt, equation_set, initial_conditions):
    num_of_equations = len(equation_set)
    results = [[] for _ in range(num_of_equations)]
    for i in range(num_of_equations):
        results[i].append(initial_conditions[i])

    for n in range(1, step_n + 1):
        for i in range(num_of_equations):
            results[i].append(results[i][n-1] + equation_set[i]([n * dt] + [results[j][n-1] for j in dependency_set[i]]) * dt)
    
    timeline=[dt * n for n in range(step_n + 1)]
    return results, timeline

def plot_results():
    results, timeline = solve(dt, equation_set, initial_conditions)
    fig, ax = plt.subplots()
    #ax.plot(timeline,results[1],label='x')
    ax.plot(timeline,results[0],label='p')    
    print(results[0][10000])

    ax.set_xlabel('position')
    ax.set_ylabel('pressure')
    ax.set_title('pressure calculation')
    ax.legend(loc='upper right')
    fig.show()
    plt.pause(10)

plot_results()