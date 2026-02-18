import numpy as np
from matplotlib import pyplot as plt

def velocity_local (x,y,t,a,om):
    #this function gives the velocity in position (x,y) and time t
    #a is the amplitude, om the frequency
    
    pi=np.pi   #define some auxiliary variable that we will not return 
    f=2*pi*om
    
    u=a*   x*np.cos(f*t)  #velocity in x-direction
    v=a*(-y)*np.cos(f*t) + x # and y-direction
    
    return u,v

def drawField(xRange, yRange, count, nskip=15):
    xmin, xmax = xRange
    ymin, ymax = yRange
    nx, ny = count
    xlin = np.linspace(xmin, xmax, nx)    #generate vectors of x and y values
    ylin = np.linspace(ymin, ymax, ny)
    xx, yy = np.meshgrid(xlin, ylin)      #combine to 2 matrices holding x and y values for each grid point
        
    (uu,vv) = velocity_local(xx,yy,t,a,om)  #use the velocity function to generate velocity values
   
    uur=uu[0:nx:nskip,0:ny:nskip]   #only keep every nskip-th value 
    vvr=vv[0:nx:nskip,0:ny:nskip]
    xxr=xx[0:nx:nskip,0:ny:nskip]
    yyr=yy[0:nx:nskip,0:ny:nskip]

    fig, ax = plt.subplots()  #make fig with 1 item (called ax)
    ax.quiver(xxr,yyr, uur, vvr)
    fig.show()
    plt.pause(10)

def makePointGrid(xRange, yRange, count):
    nx = ny = count
    xmin, xmax = xRange
    ymin, ymax = yRange
    xlin = np.linspace(xmin, xmax, nx)
    ylin = np.linspace(ymin, ymax, ny)
    return [xlin, ylin]

def drawTrajectories(points, t_count, t_max, draw=True):
    dt = t_max / t_count
    count = len(points[0])
    xlin = points[0]
    ylin = points[1]
    xx, yy = np.meshgrid(xlin, ylin)
    x_coords = [xx]
    y_coords = [yy]
        
    for i in range(1, t_count + 1):
        (uu,vv) = velocity_local(x_coords[i - 1],y_coords[i - 1],t + i*dt,a,om)

        x_coords.append(x_coords[i - 1] + uu * dt)
        y_coords.append(y_coords[i - 1] + vv * dt)


    if(draw):
        fig, ax = plt.subplots()
        for i in range(count):
            ax.plot([x_coords[n][i] for n in range( t_count + 1)], [y_coords[n][i] for n in range( t_count + 1)])

        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('trajectories')
        ax.legend(loc='upper right')
        fig.show()
        plt.pause(20)
    else:
        return x_coords, y_coords

def drawStreakline(x, y, t_count, t_max):
    dt = t_max / t_count
    fig, ax = plt.subplots()
    x_coords = []
    y_coords = []
    for i in range(t_count):
        x_vals, y_vals = drawTrajectories([[x], [y]], t_count, t_max, False)
        x_coords.append(x_vals)
        y_coords.append(y_vals)
        ax.plot([x_coords[i][n][0] for n in range(len(x_coords[i][0]))], [y_coords[i][n][0] for n in range(len(y_coords[i][0]))])

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('streakline')
    ax.legend(loc='upper right')
    fig.show()
    plt.pause(20)

a=1
om=1
t = 1
drawField(xRange=[-10, 10], yRange=[-10, 10], count=[20, 20], nskip=1)
drawTrajectories(makePointGrid(xRange=[-10, 10], yRange=[-10, 10], count=20), t_count=20, t_max=1)
drawStreakline(1, 3, t_count=20, t_max=1)