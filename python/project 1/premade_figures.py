from main import plotter_function, plotter, pressure, print_force, question_a, velocity, joukowski_velocity
import numpy as np

#Circle, wind and circulation constants
a = 1.12
z0 = -0.1 + 0.22j
correct_gamma = -2.8
U = 1

#region a)
question_a(save=True, filename='a_scatter.png')
#endregion
#region b)
plotter(plotter_function(1, a, 0), joukowski=False, draw_shape=True, fig_limit=2.5, contours=100, save=True, filename='b_streamfunction_gamma0.png', label='Streamfunction', units='m^2/s')
plotter(plotter_function(1, a, -3), joukowski=False, draw_shape=True, fig_limit=2.5, contours=100, save=True, filename='b_streamfunction_gamma-3.png', label='Streamfunction', units='m^2/s')
#endregion
#region c)
plotter(plotter_function(1, a, 0), joukowski=True, draw_shape=True, fig_limit=2.5, contours=100, save=True, filename='c_streamfunction_gamma0.png', label='Streamfunction', units='m^2/s')
plotter(plotter_function(1, a, -3), joukowski=True, draw_shape=True, fig_limit=2.5, contours=100, save=True, filename='c_streamfunction_gamma-3.png', label='Streamfunction', units='m^2/s')
#endregion
#region d)
plotter(plotter_function(1, a, -0.2), joukowski=True, draw_shape=True, fig_limit=0.3, fig_offset=[2.1, -0.2], contours=400, save=True, filename=f'd_streamfunction_gamma-{-0.2}.png', label='Streamfunction', units='m^2/s')
#endregion
#region e)
plotter(plotter_function(1, a, correct_gamma), joukowski=True, draw_shape=True, fig_limit=2.5, contours=100, save=True, filename=f'e_streamfunction_gamma-{correct_gamma}.png', label='Streamfunction', units='m^2/s')
plotter(plotter_function(1, a, correct_gamma), joukowski=True, draw_shape=True, fig_limit=0.3, fig_offset=[2.1, -0.2], contours=800, save=True, filename=f'e_zoomed_streamfunction_gamma-{correct_gamma}.png', label='Streamfunction', units='m^2/s')
#endregion
#region f)
plotter(plotter_function(1, a, correct_gamma, function='jpressure'), joukowski=True, draw_shape=True, fig_limit=2.5, contours=100, colourmap='turbo', fill=True, save=True, filename='f_Cylinder_pressure.png', label='Pressure', units='Pa')
plotter(plotter_function(1, a, correct_gamma, function='pressure'), joukowski=False, draw_shape=True, fig_limit=2.5, contours=100, colourmap='turbo', fill=True, save=True, filename='f_Wing_pressure.png', label='Pressure', units='Pa')
#endregion
#region g)
print_force(1, a=a, gamma=correct_gamma)
#endregion