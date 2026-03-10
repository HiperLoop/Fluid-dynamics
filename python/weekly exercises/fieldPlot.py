import numpy as np
from matplotlib import pyplot as plt

""" def velocity_local (x,y,t,a,om):
    #this function gives the velocity in position (x,y) and time t
    #a is the amplitude, om the frequency
    
    pi=np.pi   #define some auxiliary variable that we will not return 
    f=2*pi*om
    
    u=a*   x*np.cos(f*t) * t  #velocity in x-direction
    v=a*(-y)*np.cos(f*t) + x # and y-direction
    
    return u,v """

def velocity_local (x,y,t,a,om):
    u= a * (np.e**(m * y)) * np.cos(k * t - m*x)
    v= -1 * a * (np.e**(m * y)) * np.sin(k * t - m * x)
    return u,v

def drawField(xRange, yRange, count, time, nskip=15):
    lins = makePointGrid(xRange, yRange, count)  #make 1D arrays of x and y values
    xx, yy = np.meshgrid(lins[0], lins[1])      #combine to 2 matrices holding x and y values for each grid point
        
    (uu,vv) = velocity_local(xx,yy,time,a,om)  #use the velocity function to generate velocity values
   
    uur=uu[0:count:nskip,0:count:nskip]   #only keep every nskip-th value 
    vvr=vv[0:count:nskip,0:count:nskip]
    xxr=xx[0:count:nskip,0:count:nskip]
    yyr=yy[0:count:nskip,0:count:nskip]

    fig, ax = plt.subplots()  #make fig with 1 item (called ax)
    ax.quiver(xxr,yyr, uur, vvr)
    fig.show()
    plt.pause(20)

def makePointGrid(xRange, yRange, count):
    nx = ny = count
    xmin, xmax = xRange
    ymin, ymax = yRange
    xlin = np.linspace(xmin, xmax, nx)
    ylin = np.linspace(ymin, ymax, ny)
    print(ylin)
    return [xlin, ylin]

def drawTrajectories(points, t_count, t_max, t_start, draw=True):
    dt = t_max / t_count
    count = len(points[0])
    xlin = points[0]
    ylin = points[1]
    xx, yy = np.meshgrid(xlin, ylin)
    x_coords = [xx]
    y_coords = [yy]
        
    for i in range(1, t_count + 1):
        (uu,vv) = velocity_local(x_coords[i - 1],y_coords[i - 1],t_start + i*dt,a,om)

        x_coords.append(x_coords[i - 1] + uu * dt)
        y_coords.append(y_coords[i - 1] + vv * dt)


    if(draw):
        fig, ax = plt.subplots()
        for i in range(count):
            ax.plot([x_coords[n][i] for n in range( t_count + 1)], [y_coords[n][i] for n in range( t_count + 1)])

        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('trajectories')
        #ax.legend(loc='upper right')
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
        x_vals, y_vals = drawTrajectories([[x], [y]], t_count, t_max, t_start=i * dt, draw=False)
        x_coords.append(x_vals)
        y_coords.append(y_vals)
        ax.plot([x_coords[i][n][0] for n in range(t_count - i)], [y_coords[i][n][0] for n in range(t_count - i)])

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('streakline')
    #ax.legend(loc='upper right')
    fig.show()
    plt.pause(20)

a=1
om=1
m = 1
k = 1
drawField(xRange=[-10, 10], yRange=[-23, -3], count=21, nskip=1, time=0)
drawTrajectories(makePointGrid(xRange=[-10, 10], yRange=[-20, 0], count=21), t_count=2000, t_max=10, t_start=0)
drawStreakline(1, -3, t_count=20, t_max=100)