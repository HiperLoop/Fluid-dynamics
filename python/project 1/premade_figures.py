from main import plotter_function, plotter, question_a
a = 1.12
z0 = (-0.1, 0.22)
#region a)
#question_a()
#endregion
#region b)
#plotter(plotter_function(1, 0, a, 0), joukowski=False, draw_shape=True, fig_limit=2.5, contours=100)
#plotter(plotter_function(1, 0, a, -3), joukowski=False, draw_shape=True, fig_limit=2.5, contours=100)
#endregion
#region c)
#plotter(plotter_function(1, 0, a, 0), joukowski=True, draw_shape=True, fig_limit=2.5, contours=100)
#plotter(plotter_function(1, 0, a, -3), joukowski=True, draw_shape=True, fig_limit=2.5, contours=100)
#endregion
#region d)
#plotter(plotter_function(1, 0, a, -0.2), joukowski=True, draw_shape=True, fig_limit=0.5, fig_offset=[2, -0.2], contours=200)
#endregion
#region e)
plotter(plotter_function(1, 0, a, -0.2), joukowski=True, draw_shape=False, fig_limit=0.5, fig_offset=[2, -0.2], contours=400)
#endregion