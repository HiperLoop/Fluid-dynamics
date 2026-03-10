from main import plotter_function, plotter, pressure, print_force, question_a, velocity_field, joukowski_velocity
import numpy as np
a = 1.12
z0 = (-0.1, 0.22)
#region a)
question_a(save=True, filename='a_scatter.png')
#endregion
#region b)
plotter(plotter_function(1, 0, a, 0), joukowski=False, draw_shape=True, fig_limit=2.5, contours=100, save=True, filename='b_streamfunction_gamma0.png')
plotter(plotter_function(1, 0, a, -3), joukowski=False, draw_shape=True, fig_limit=2.5, contours=100, save=True, filename='b_streamfunction_gamma-3.png')
#endregion
#region c)
plotter(plotter_function(1, 0, a, 0), joukowski=True, draw_shape=True, fig_limit=2.5, contours=100, save=True, filename='c_streamfunction_gamma0.png')
plotter(plotter_function(1, 0, a, -3), joukowski=True, draw_shape=True, fig_limit=2.5, contours=100, save=True, filename='c_streamfunction_gamma-3.png')
#endregion
#region d)
plotter(plotter_function(1, 0, a, -2.5), joukowski=True, draw_shape=True, fig_limit=0.3, fig_offset=[2.1, -0.2], contours=400, save=True, filename='d_streamfunction_gamma-0.2.png')
#endregion
#region e)
plotter(plotter_function(1, 0, a, -2.5), joukowski=True, draw_shape=True, fig_limit=2.5, contours=100, save=True, filename='e_streamfunction_gamma-2.5.png')
plotter(plotter_function(1, 0, a, -2.5, function='stream'), joukowski=True, draw_shape=True, fig_limit=0.3, fig_offset=[2.1, -0.2], contours=800, save=True, filename='e_zoomed_streamfunction_gamma-2.5.png')
#endregion
#region f)
plotter(plotter_function(1, 0, a, -2.5, function='pressure'), joukowski=True, draw_shape=True, fig_limit=2.5, contours=100, colourmap='turbo', fill=True, save=True, filename='f_pressure.png')
plotter(plotter_function(1, 0, a, -2.5, function='jvelocity'), joukowski=True, draw_shape=True, fig_limit=2.5, contours=100, colourmap='turbo', fill=True, save=True, filename='f_joukowski_velocity.png')
#endregion
#region g)
#print_force(x_vel=1, y_vel=0, a=a, gamma=-2.5)
#endregion